#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from sklearn.model_selection import train_test_split # <-- CPU version
from sklearn.preprocessing import StandardScaler as SklearnScaler # <-- CPU version
from sklearn.svm import SVC # <-- CPU version
from sklearn.metrics import accuracy_score # <-- CPU version
from tqdm import tqdm

# --- MODIFICATION: Import PyTorch ---
# (--- 修改：导入 PyTorch ---)
try:
    import torch
    import torch.nn as nn
    import torch.optim as optim
    from torch.utils.data import TensorDataset, DataLoader
    TORCH_AVAILABLE = True
except ImportError:
    print("Error: 'torch' (PyTorch) not found. This script requires them.")
    print("Please install it first: pip install torch")
    TORCH_AVAILABLE = False

# --- NEW: Define the MLPClassifier Model in PyTorch ---
# (--- 新增：用 PyTorch 定义 MLPClassifier 模型 ---)
class SupervisedMLP(nn.Module):
    def __init__(self, input_dim, hidden_dim_1=100, hidden_dim_2=50):
        """
        Defines the architecture of the supervised feature extractor.
        (定义“有监督”特征提取器的架构。)
        """
        super(SupervisedMLP, self).__init__()
        
        # Encoder (编码器) - This is our Feature Extractor
        # (这部分是我们的特征提取器)
        self.feature_extractor = nn.Sequential(
            nn.Linear(input_dim, hidden_dim_1),
            nn.ReLU(),
            nn.Linear(hidden_dim_1, hidden_dim_2), # <-- This is our "bottleneck"
            nn.ReLU()
        )
        
        # Classifier Head (分类头) - This part will be "chopped off"
        # (这部分将被“砍掉”)
        self.classifier_head = nn.Sequential(
            nn.Linear(hidden_dim_2, 1),
            nn.Sigmoid() # (For binary classification)
        )

    def forward(self, x):
        """
        Run data through the full MLP (for training).
        (运行数据通过完整的 MLP（用于训练）。)
        """
        features = self.feature_extractor(x)
        output = self.classifier_head(features)
        return output
    
    def get_latent_features(self, x):
        """
        Run data *only* through the Encoder (for transformation).
        (运行数据*仅*通过编码器（用于变换）。)
        """
        return self.feature_extractor(x)

# --- MODIFICATION: Function now runs the full MLP -> SVM pipeline ---
# (--- 修改：函数现在运行完整的 MLP -> SVM 流水线 ---)
def run_mlp_svm_pipeline(n, k_components, C_param, gamma_param):
    """
    Runs a 2-stage pipeline on CPU:
    1. (CPU) Train a *Supervised MLP* to create k features (de-noising).
    2. (CPU) Train an RBF SVM on the new k features.
    (在 CPU 上运行一个 2 阶段流水线：
     1. (CPU) 训练一个*有监督 MLP* 来创建 k 维特征（降噪）。
     2. (CPU) 在新的 k 维特征上训练 RBF SVM。)
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
    
    # --- 2. (CPU) Pre-processing for MLP ---
    # (--- (CPU) 为 MLP 进行预处理 ---)
    scaler_mlp = SklearnScaler()
    X_scaled_cpu = scaler_mlp.fit_transform(X_cpu)
    
    # --- 3. (CPU) Split data for MLP Training ---
    # (--- (CPU) 为 MLP 训练分割数据 ---)
    # (We need a separate split to train the feature extractor)
    # (我们需要一个单独的分割来训练特征提取器)
    X_train_mlp, X_test_mlp, y_train_mlp, y_test_mlp = train_test_split(
        X_scaled_cpu, y_cpu, test_size=0.3, random_state=42
    )

    # --- 4. (CPU) Train the Supervised MLP (Feature Extractor) ---
    # (--- (CPU) 训练“有监督 MLP”（特征提取器） ---)
    print(f"  Training Supervised MLP to reduce {n}-D -> {k_components}-D...")
    
    X_tensor = torch.tensor(X_train_mlp, dtype=torch.float32)
    y_tensor = torch.tensor(y_train_mlp, dtype=torch.float32).reshape(-1, 1) # (Target)
    
    dataset = TensorDataset(X_tensor, y_tensor) # (Target is now y)
    train_loader = DataLoader(dataset, batch_size=64, shuffle=True)
    
    model_mlp = SupervisedMLP(input_dim=n, hidden_dim_2=k_components)
    criterion = nn.BCELoss() # (Binary Cross-Entropy Loss, for classification)
    optimizer = optim.Adam(model_mlp.parameters(), lr=0.001)
    
    N_EPOCHS = 30
    model_mlp.train()
    for epoch in range(N_EPOCHS):
        for data in train_loader:
            inputs, targets = data # (inputs are X, targets are y)
            optimizer.zero_grad()
            outputs = model_mlp(inputs) # (Run through full model)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
    print("  MLP (Feature Extractor) Training complete.")

    # --- 5. (CPU) Extract New Features (from ALL data) ---
    # (--- (CPU) 提取新特征（从所有数据中） ---)
    model_mlp.eval()
    with torch.no_grad():
        # (Transform the *entire* scaled dataset)
        # (变换*整个*缩放后的数据集)
        X_full_scaled_tensor = torch.tensor(X_scaled_cpu, dtype=torch.float32)
        X_new_features_tensor = model_mlp.get_latent_features(X_full_scaled_tensor)
        
    X_new_features_cpu = X_new_features_tensor.numpy()
    
    print(f"  New feature space created. Shape: {X_new_features_cpu.shape}")
    
    # --- 6. (CPU) Move New Features to SVM ---
    # (--- (CPU) 将新特征送入 SVM ---)
    X_new = X_new_features_cpu
    y_new = y_cpu # (Use the original full y)

    # Split the NEW k-dimensional data (on CPU)
    # (分割新的 k 维数据 (在 CPU 上))
    X_train, X_temp, y_train, y_temp = train_test_split(X_new, y_new, test_size=0.6, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    
    features = X_train.shape[1] # (This will be 'k_components')

    # --- 7. (CPU) Scale the NEW k-dimensional features ---
    # (This is still critical for SVM)
    scaler_svm = SklearnScaler() 
    X_train_scaled = scaler_svm.fit_transform(X_train)
    X_val_scaled = scaler_svm.transform(X_val)
    X_test_scaled = scaler_svm.transform(X_test)
    
    # --- 8. (CPU) Train the RBF SVM ---
    # (--- (CPU) 训练 RBF SVM ---)
    print(f"  Fitting sklearn.svm.SVC... (This may be slow)")
    svm = SVC(
        kernel='rbf', 
        C=C_param,
        gamma=gamma_param,
        cache_size=2048,  
        random_state=42 
    )
    
    svm.fit(X_train_scaled, y_train)
    print("  SVM Fit complete.")

    # --- 9. Calculate Final Accuracy ---
    y_train_pred = svm.predict(X_train_scaled) 
    train_accuracy = accuracy_score(y_train, y_train_pred) 

    y_val_pred = svm.predict(X_val_scaled) 
    val_accuracy = accuracy_score(y_val, y_val_pred)

    y_test_pred = svm.predict(X_test_scaled) 
    test_accuracy = accuracy_score(y_test, y_test_pred) 
    
    return train_accuracy, val_accuracy, test_accuracy, features
        
# Main execution block
def main():
    # --- From Cell 1 ---
    possible_n_vals = [10, 12, 14, 16, 18, 20] 
    
    # --- Define the Hyperparameter Grid for SVM (as before) ---
    grid_C_vals = [10.0, 1.0]
    grid_gamma_vals = ['auto', 0.1, 0.01]
    
    # --- NEW: Define the bottleneck dimension for the MLP Extractor ---
    # (--- 新增：为 MLP 提取器定义瓶颈维度 ---)
    K_COMPONENTS = 50 # (The size of the last hidden layer)
    
    print(f"--- Starting MLP(k={K_COMPONENTS}) -> SVM Grid Search (CPU-Only) ---")
    print(f"n values: {possible_n_vals}")
    print(f"C values: {grid_C_vals}")
    print(f"gamma values: {grid_gamma_vals}")
    
    # --- MODIFICATION: These lists will store the BEST result for each 'n' ---
    best_train_acc_by_n = [] 
    best_val_acc_by_n = [] 
    best_test_acc_by_n = []  
    best_feat_by_n = []
    
    # --- Outer loop for 'n' (number of features) ---
    for n in tqdm(possible_n_vals, desc="n_vals Loop"):
        
        # Track the best model for THIS 'n'
        best_val_score_for_n = -1.0
        best_params_for_n = {}
        best_result_for_n = (0.5, 0.5, 0.5, n) 

        # --- Inner loops for Grid Search (C and gamma) ---
        for C_val in tqdm(grid_C_vals, desc=f"n={n} - C Loop", leave=False):
            for gamma_val in tqdm(grid_gamma_vals, desc=f"n={n} C={C_val} - gamma Loop", leave=False):
                
                print(f"\n--- Running: n={n} -> MLP(k={K_COMPONENTS}) -> SVM(C={C_val}, g={gamma_val}) ---")
                
                # --- MODIFICATION: Call the CPU pipeline function ---
                train_acc, val_acc, test_acc, feat = run_mlp_svm_pipeline(n, K_COMPONENTS, C_val, gamma_val)
                
                print(f"Result: Train={train_acc:.4f}, Val={val_acc:.4f}, Test={test_acc:.4f}")

                # Check if this is the new best model *for this n*
                if val_acc > best_val_score_for_n:
                    best_val_score_for_n = val_acc
                    best_params_for_n = {'C': C_val, 'gamma': gamma_val}
                    best_result_for_n = (train_acc, val_acc, test_acc, feat)
                    print(f"*** New Best for n={n}: Val Acc={val_acc:.4f} with C={C_val}, gamma={gamma_val} ***")
        
        # --- End of Grid Search for 'n' ---
        print(f"--- Best parameters for n={n}: {best_params_for_n} (Val Acc: {best_val_score_for_n:.4f}) ---")
        
        # Store the accuracies from the best model
        best_train_acc_by_n.append(best_result_for_n[0])
        best_val_acc_by_n.append(best_result_for_n[1])
        best_test_acc_by_n.append(best_result_for_n[2])
        best_feat_by_n.append(best_result_for_n[3]) # (This will be 'k_components')
        
    print("--- Grid Search Complete ---")
    print("Best Train Accuracy results (by n):", best_train_acc_by_n)
    print("Best Validation Accuracy results (by n):", best_val_acc_by_n) 
    print("Best Test Accuracy results (by n):", best_test_acc_by_n)

    # --- From Cell 4 (MODIFIED FOR SVM PLOT) ---
    print("Plotting Figure: (MLP -> SVM) Pipeline Accuracy (CPU-Only)...")
    
    # Plot style
    sns.set_context("poster", font_scale=2.0)
    colors = sns.color_palette("pastel", 3)

    success_hlines = [0.94, 0.93, 0.92, 0.91,0.80,0.75]  
    
    # --- Create a SINGLE plot for all n ---
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    
    # (The x-axis is now the original 'n' value)
    x_axis_n = possible_n_vals 
    
    ax.plot(x_axis_n, best_test_acc_by_n, marker='o', label='Test (Best)', color=colors[0],
            lw=7, markersize=20)
            
    ax.plot(x_axis_n, best_train_acc_by_n, marker='x', label='Train (Best)', color=colors[1],
            linestyle='--', lw=5, markersize=12)
    
    ax.plot(x_axis_n, best_val_acc_by_n, marker='^', label='Val (Best)', color=colors[2],
            linestyle=':', lw=5, markersize=12)
    
    # (Adding horizontal lines based on 'n' index)
    for i, n in enumerate(x_axis_n):
        if i < len(success_hlines): 
            ax.hlines(success_hlines[i], xmin=n-0.5, xmax=n+0.5, color='gray', linestyle='--', lw=4)
    
    # Customizing the plot
    ax.set_title(f'Optimized SVM Performance after Supervised MLP(k={K_COMPONENTS}) FE', fontsize=18)
    ax.set_xlabel("Number of Original Features (n)", fontsize=16)
    ax.set_ylabel("Accuracy", fontsize=16)
    
    ax.set_xticks(possible_n_vals) 
    ax.set_xscale('linear') 
    
    ax.legend(loc='lower right', fontsize='medium') 
        
    # Adjust layout
    plt.tight_layout()
    plt.ylim((0.45, 1.0))

    plt.savefig("Figs/SVM/mlp_svm_pipeline_accuracy_CPU.png", dpi=300)
    print("Saved 'mlp_svm_pipeline_accuracy_CPU.png' to disk.")
    plt.clf() 
    
    print("--- Script Finished ---")

# Standard Python entry point
if __name__ == "__main__":
    main()