#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from sklearn.model_selection import train_test_split # <-- CPU version
from sklearn.preprocessing import StandardScaler as SklearnScaler # <-- CPU version
from sklearn.metrics import accuracy_score # <-- CPU version
from sklearn.manifold import TSNE # <-- NEW: Import t-SNE for visualization
from tqdm import tqdm

# --- MODIFICATION: Import PyTorch for Feature Extractor ---
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
TORCH_AVAILABLE = True


# --- MODIFICATION: Import Logistic Regression for Classifier ---
from sklearn.linear_model import LogisticRegression # <-- NEW
# import xgboost as xgb <-- REMOVED
XGB_AVAILABLE = False # <-- MODIFICATION


# --- NEW: Define the MLPClassifier Model in PyTorch ---
class SupervisedMLP(nn.Module):
    def __init__(self, input_dim, hidden_dim_1=100, hidden_dim_2=50):
        super(SupervisedMLP, self).__init__()
        self.feature_extractor = nn.Sequential(
            nn.Linear(input_dim, hidden_dim_1),
            nn.ReLU(),
            nn.Linear(hidden_dim_1, hidden_dim_2), # <-- This is our "bottleneck"
            nn.ReLU()
        )
        self.classifier_head = nn.Sequential(
            nn.Linear(hidden_dim_2, 1),
            nn.Sigmoid() 
        )
    def forward(self, x):
        features = self.feature_extractor(x)
        output = self.classifier_head(features)
        return output
    def get_latent_features(self, x):
        return self.feature_extractor(x)

# --- MODIFICATION: Function now runs the full MLP -> Logistic Regression pipeline ---
def run_mlp_lr_pipeline(n, k_components, lr_C_param, pre_trained_mlp=None, pre_scaled_X=None):
    """
    Runs a 2-stage pipeline on CPU:
    1. (CPU) *Receives* a pre-trained MLP to create k features.
    2. (CPU) Train a Logistic Regression on the new k features.
    (在 CPU 上运行一个 2 阶段流水线：
     1. (CPU) *接收*一个预训练的 MLP 来创建 k 维特征。
     2. (CPU) 在新的 k 维特征上训练逻辑回归。)
    """
    
    if not TORCH_AVAILABLE:
        print("PyTorch not found, skipping run.")
        return 0.5, 0.5, 0.5, 0

    # --- 1. Load Data (on CPU) ---
    X_path = f'../Datasets/kryptonite-{n}-X.npy'
    y_path = f'../Datasets/kryptonite-{n}-y.npy'
    
    if not (os.path.exists(X_path) and os.path.exists(y_path)):
        print(f"Error: Data files not found at {X_path}. Skipping run.")
        return 0.5, 0.5, 0.5, 0
        
    X_cpu = np.load(X_path)
    y_cpu = np.load(y_path)
    
    # --- 2. (CPU) Use pre-scaled data ---
    if pre_scaled_X is None:
        print("Warning: Pre-scaled data not provided. Scaling X_cpu...")
        scaler_mlp = SklearnScaler()
        X_scaled_cpu = scaler_mlp.fit_transform(X_cpu)
    else:
        X_scaled_cpu = pre_scaled_X

    # --- 3. (CPU) Train the Supervised MLP (Feature Extractor) ---
    if pre_trained_mlp is None:
        print(f"  Training Supervised MLP to reduce {n}-D -> {k_components}-D...")
        
        X_tensor = torch.tensor(X_scaled_cpu, dtype=torch.float32)
        y_tensor = torch.tensor(y_cpu, dtype=torch.float32).reshape(-1, 1) # (Target)
        
        dataset = TensorDataset(X_tensor, y_tensor) # (Target is now y)
        train_loader = DataLoader(dataset, batch_size=64, shuffle=True)
        
        model_mlp = SupervisedMLP(input_dim=n, hidden_dim_2=k_components)
        criterion = nn.BCELoss() 
        optimizer = optim.Adam(model_mlp.parameters(), lr=0.001)
        
        N_EPOCHS = 30
        model_mlp.train()
        for epoch in range(N_EPOCHS):
            for data in train_loader:
                inputs, targets = data 
                optimizer.zero_grad()
                outputs = model_mlp(inputs)
                loss = criterion(outputs, targets)
                loss.backward()
                optimizer.step()
        print("  MLP (Feature Extractor) Training complete.")
    else:
        print(f"  Using pre-trained MLP feature extractor...")
        model_mlp = pre_trained_mlp

    # --- 4. (CPU) Extract New Features (from ALL data) ---
    model_mlp.eval()
    with torch.no_grad():
        X_full_scaled_tensor = torch.tensor(X_scaled_cpu, dtype=torch.float32)
        X_new_features_tensor = model_mlp.get_latent_features(X_full_scaled_tensor)
        
    X_new_features_cpu = X_new_features_tensor.numpy()
    
    # --- 5. (CPU) Move New Features to Classifier ---
    X_new = X_new_features_cpu
    y_new = y_cpu 

    # Split the NEW k-dimensional data (on CPU)
    X_train, X_temp, y_train, y_temp = train_test_split(X_new, y_new, test_size=0.4, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    
    features = X_train.shape[1] 

    # --- 6. (CPU) Scale the NEW k-dimensional features ---
    # (!!! CRITICAL: Logistic Regression NEEDS scaled features !!!)
    # (!!! 关键：逻辑回归需要缩放后的特征 !!!)
    print("  Scaling new k-dimensional features for Logistic Regression...")
    scaler_lr = SklearnScaler()
    X_train_scaled = scaler_lr.fit_transform(X_train)
    X_val_scaled = scaler_lr.transform(X_val)
    X_test_scaled = scaler_lr.transform(X_test)
    
    # --- 7. (CPU) Train the Logistic Regression Classifier ---
    print(f"  Fitting Logistic Regression (C={lr_C_param})...")
    
    lr_model = LogisticRegression(
        C=lr_C_param,
        solver='lbfgs',      # (A good default solver)
        max_iter=1000,       # (Increase iterations for convergence)
        random_state=42,
        n_jobs=-1 
    )
    
    lr_model.fit(X_train_scaled, y_train) 
    print("  Logistic Regression Fit complete.")

    # --- 8. Calculate Final Accuracy ---
    y_train_pred = lr_model.predict(X_train_scaled) 
    train_accuracy = accuracy_score(y_train, y_train_pred) 

    y_val_pred = lr_model.predict(X_val_scaled) 
    val_accuracy = accuracy_score(y_val, y_val_pred)

    y_test_pred = lr_model.predict(X_test_scaled) 
    test_accuracy = accuracy_score(y_test, y_test_pred) 
    
    return train_accuracy, val_accuracy, test_accuracy, features


# --- NEW FUNCTION: Visualization of MLP Feature Engineering ---
# (--- 这个函数不需要改变，因为它只依赖于 MLP 提取器 ---)
def visualize_mlp_engineering(n, k_components, mlp_model, X_scaled_cpu, y_cpu):
    """
    Receives a trained MLP and visualizes the "Before" (original)
    and "After" (MLP-transformed) feature spaces using t-SNE.
    """
    print("\n" + "="*50)
    print("--- 1. VISUALIZATION: Running t-SNE on 'BEFORE' (Original) data... ---")
    print("(This is slow, please wait...)")
    tsne_before = TSNE(n_components=2, perplexity=30, random_state=42, n_jobs=-1)
    X_tsne_before = tsne_before.fit_transform(X_scaled_cpu)
    print("  'BEFORE' t-SNE finished.")

    # --- Extract "AFTER" features ---
    print("--- 2. VISUALIZATION: Extracting 'AFTER' (MLP) features... ---")
    mlp_model.eval()
    with torch.no_grad():
        X_full_scaled_tensor = torch.tensor(X_scaled_cpu, dtype=torch.float32)
        X_new_features_tensor = mlp_model.get_latent_features(X_full_scaled_tensor)
    X_new_features_cpu = X_new_features_tensor.numpy()

    print("--- 3. VISUALIZATION: Running t-SNE on 'AFTER' (MLP) data... ---")
    tsne_after = TSNE(n_components=2, perplexity=30, random_state=42, n_jobs=-1)
    X_tsne_after = tsne_after.fit_transform(X_new_features_cpu)
    print("  'AFTER' t-SNE finished.")

    # --- 4. Prepare Data for Plotting ---
    print("--- 4. VISUALIZATION: Preparing data for plotting... ---")
    df_tsne_before = pd.DataFrame(X_tsne_before, columns=['Component 1', 'Component 2'])
    df_tsne_after = pd.DataFrame(X_tsne_after, columns=['Component 1', 'Component 2'])

    df_target = pd.DataFrame(y_cpu, columns=['Target_val'])
    df_target['Target'] = df_target['Target_val'].map({0: 'Label 0', 1: 'Label 1'})

    df_plot_before = pd.concat([df_tsne_before, df_target], axis=1)
    df_plot_after = pd.concat([df_tsne_after, df_target], axis=1)

    # --- 5. Visualize the "Before vs After" ---
    print("--- 5. VISUALIZATION: Generating 'Before vs After' comparison plot... ---")
    # (Make sure 'Figs/LogReg' directory exists)
    os.makedirs('Figs/LogReg', exist_ok=True)
    
    sns.set_context("poster", font_scale=1.2)
    fig, axes = plt.subplots(1, 2, figsize=(24, 10))
    
    sns.scatterplot(
        data=df_plot_before, x='Component 1', y='Component 2',
        hue='Target', style='Target', palette='husl', s=15, alpha=0.5, ax=axes[0]
    )
    axes[0].set_title(f'BEFORE: t-SNE on Original {n}-D Features', fontsize=20)
    axes[0].set_xlabel('t-SNE Component 1', fontsize=14)
    axes[0].set_ylabel('t-SNE Component 2', fontsize=14)
    axes[0].grid(True, linestyle='--', alpha=0.6)
    axes[0].legend(loc='best')

    sns.scatterplot(
        data=df_plot_after, x='Component 1', y='Component 2',
        hue='Target', style='Target', palette='husl', s=15, alpha=0.5, ax=axes[1]
    )
    axes[1].set_title(f'AFTER: t-SNE on New {k_components}-D MLP Features', fontsize=20)
    axes[1].set_xlabel('t-SNE Component 1 (from MLP)', fontsize=14)
    axes[1].set_ylabel('t-SNE Component 2 (from MLP)', fontsize=14)
    axes[1].grid(True, linestyle='--', alpha=0.6)
    axes[1].legend(loc='best')

    plt.suptitle(f'Visualizing MLP Feature Engineering (n={n})', fontsize=24, y=1.03)
    plt.tight_layout()
    plt.savefig(f"Figs/LogReg/mlp_feature_engineering_visualization_n{n}.png", dpi=300)
    plt.show()
    plt.clf()
    print(f"Visualization saved as 'mlp_feature_engineering_visualization_n{n}.png'.")
    print("="*50 + "\n")


# Main execution block
def main():
    # --- From Cell 1 ---
    possible_n_vals = [10, 12, 14, 16, 18, 20] 
    
    # --- MODIFICATION: Define the Hyperparameter Grid for Logistic Regression ---
    grid_C = [0.01, 0.1, 1.0, 10.0] # (C is the inverse of regularization strength)
    
    # --- Define the bottleneck dimension for the MLP Extractor ---
    K_COMPONENTS = 30 
    
    print(f"--- Starting MLP(k={K_COMPONENTS}) -> Logistic Regression Grid Search (CPU-Only) ---")
    
    # (Make sure 'Figs/LogReg' directory exists for the final plot)
    os.makedirs('Figs/LogReg', exist_ok=True)
    
    # --- MODIFICATION: These lists will store the BEST result for each 'n' ---
    best_train_acc_by_n = [] 
    best_val_acc_by_n = [] 
    best_test_acc_by_n = []  
    best_feat_by_n = []
    
    # --- Outer loop for 'n' (number of features) ---
    for n in tqdm(possible_n_vals, desc="n_vals Loop"):
        
        # --- MODIFICATION: Pre-train the MLP *once* for each 'n' ---
        print(f"\n--- Pre-training MLP Feature Extractor for n={n} ---")
        
        # 1. Load data
        X_cpu = np.load(f'../Datasets/kryptonite-{n}-X.npy')
        y_cpu = np.load(f'../Datasets/kryptonite-{n}-y.npy')
        
        # 2. Scale data
        scaler_mlp = SklearnScaler()
        X_scaled_cpu = scaler_mlp.fit_transform(X_cpu)

        # 3. Train MLP
        print(f"  Training Supervised MLP to reduce {n}-D -> {K_COMPONENTS}-D...")
        X_tensor = torch.tensor(X_scaled_cpu, dtype=torch.float32)
        y_tensor = torch.tensor(y_cpu, dtype=torch.float32).reshape(-1, 1)
        
        dataset = TensorDataset(X_tensor, y_tensor)
        train_loader = DataLoader(dataset, batch_size=64, shuffle=True)
        
        mlp_extractor = SupervisedMLP(input_dim=n, hidden_dim_1=200, hidden_dim_2=K_COMPONENTS) 
        criterion = nn.BCELoss() 
        optimizer = optim.Adam(mlp_extractor.parameters(), lr=0.001)
        
        N_EPOCHS = 50 # (Train for longer to get a good representation)
        mlp_extractor.train()
        for epoch in range(N_EPOCHS):
            for data in train_loader:
                inputs, targets = data 
                optimizer.zero_grad()
                outputs = mlp_extractor(inputs)
                loss = criterion(outputs, targets)
                loss.backward()
                optimizer.step()
        print(f"  MLP Extractor for n={n} is trained.")
        
        # --- (Optional) Call the visualization function ---
        # visualize_mlp_engineering(n, K_COMPONENTS, mlp_extractor, X_scaled_cpu, y_cpu)
        
        # --- Now, proceed with the Logistic Regression Grid Search ---
        
        best_val_score_for_n = -1.0
        best_params_for_n = {}
        best_result_for_n = (0.5, 0.5, 0.5, n) 

        # --- MODIFICATION: Loop over 'C' values ---
        for C_val in tqdm(grid_C, desc=f"n={n} - C_val Loop", leave=False):
            
            print(f"\n--- Running: n={n} -> MLP(k={K_COMPONENTS}) -> LogReg(C={C_val}) ---")
            
            # --- MODIFICATION: Call the new pipeline function ---
            train_acc, val_acc, test_acc, feat = run_mlp_lr_pipeline(
                n, K_COMPONENTS, C_val,
                pre_trained_mlp=mlp_extractor,
                pre_scaled_X=X_scaled_cpu
            )
            
            print(f"Result: Train={train_acc:.4f}, Val={val_acc:.4f}, Test={test_acc:.4f}")

            if val_acc > best_val_score_for_n:
                best_val_score_for_n = val_acc
                best_params_for_n = {'C': C_val} # <-- MODIFICATION
                best_result_for_n = (train_acc, val_acc, test_acc, feat)
                print(f"*** New Best for n={n}: Val Acc={val_acc:.4f} with params={best_params_for_n} ***")
        
        # --- End of Grid Search for 'n' ---
        print(f"--- Best parameters for n={n}: {best_params_for_n} (Val Acc: {best_val_score_for_n:.4f}) ---")
        
        best_train_acc_by_n.append(best_result_for_n[0])
        best_val_acc_by_n.append(best_result_for_n[1])
        best_test_acc_by_n.append(best_result_for_n[2])
        best_feat_by_n.append(best_result_for_n[3]) 
        
    print("--- Grid Search Complete ---")
    print("Best Train Accuracy results (by n):", best_train_acc_by_n)
    print("Best Validation Accuracy results (by n):", best_val_acc_by_n) 
    print("Best Test Accuracy results (by n):", best_test_acc_by_n)

    # --- MODIFICATION: Update Plot for Logistic Regression ---
    print("Plotting Figure: (MLP -> Logistic Regression) Pipeline Accuracy (CPU-Only)...")
    
    # Plot style
    sns.set_context("poster", font_scale=2.0)
    colors = sns.color_palette("pastel", 3)

    success_hlines = [0.94, 0.93, 0.92, 0.91, 0.80, 0.75]  
    
    # --- Create a SINGLE plot for all n ---
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    
    x_axis_n = possible_n_vals 
    
    ax.plot(x_axis_n, best_test_acc_by_n, marker='o', label='Test (Best)', color=colors[0],
            lw=7, markersize=20)
            
    ax.plot(x_axis_n, best_train_acc_by_n, marker='x', label='Train (Best)', color=colors[1],
            linestyle='--', lw=5, markersize=12)
    
    ax.plot(x_axis_n, best_val_acc_by_n, marker='^', label='Val (Best)', color=colors[2],
            linestyle=':', lw=5, markersize=12)
    
    for i, n in enumerate(x_axis_n):
        if i < len(success_hlines): 
            ax.hlines(success_hlines[i], xmin=n-0.5, xmax=n+0.5, color='gray', linestyle='--', lw=4)
    
    # Customizing the plot
    ax.set_title(f'Optimized Logistic Regression Performance after Supervised MLP(k={K_COMPONENTS}) FE', fontsize=18)
    ax.set_xlabel("Number of Original Features (n)", fontsize=16)
    ax.set_ylabel("Accuracy", fontsize=16)
    
    ax.set_xticks(possible_n_vals) 
    ax.set_xscale('linear') 
    
    ax.legend(loc='lower right', fontsize='medium') 
        
    # Adjust layout
    plt.tight_layout()
    plt.ylim((0.45, 1.0))

    plt.savefig("Figs/LogReg/mlp_lr_pipeline_accuracy_CPU.png", dpi=300)
    print("Saved 'mlp_lr_pipeline_accuracy_CPU.png' to disk.")
    plt.clf() 
    
    print("--- Script Finished ---")

# Standard Python entry point
if __name__ == "__main__":
    main()