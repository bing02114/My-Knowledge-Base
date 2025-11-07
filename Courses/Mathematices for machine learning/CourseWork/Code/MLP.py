#!/usr/bin/env python
# coding: utf-8

import numpy as np
# --- MODIFICATION: Removed cupy and cudf ---
# (--- 修改：移除了 cupy 和 cudf ---)
from sklearn.model_selection import train_test_split # <-- MODIFICATION: Using sklearn
from sklearn.preprocessing import StandardScaler # <-- MODIFICATION: Using sklearn
from sklearn.neural_network import MLPClassifier # <-- MODIFICATION: Using sklearn
from sklearn.metrics import accuracy_score # <-- MODIFICATION: Using sklearn
from tqdm import tqdm
import matplotlib.pyplot as plt
import scienceplots  
import seaborn as sns
import numpy as np
import os 

# --- MODIFICATION: Function now accepts MLP parameters and runs on CPU ---
# (--- 修改：函数现在接受 MLP 的参数并在 CPU 上运行 ---)
def run_cpu_mlp(n, hidden_layer_sizes_param, alpha_param, learning_rate_init_param):
    """
    CPU-ONLY version using sklearn's MLPClassifier.
    (使用 sklearn 的 MLPClassifier 的仅 CPU 版本。)
    
    NOTE: StandardScaler is REQUIRED.
    (注意：StandardScaler 是必需的。)
    """
    
    # --- 1. Load Data (on CPU) ---
    X_path = f'../Datasets/kryptonite-{n}-X.npy'
    y_path = f'../Datasets/kryptonite-{n}-y.npy'
    
    if not (os.path.exists(X_path) and os.path.exists(y_path)):
        print(f"Error: Data files not found at {X_path}. Skipping run.")
        return 0.5, 0.5, 0.5, 0 # (Return dummy values)
        
    X_cpu = np.load(X_path)
    y_cpu = np.load(y_path)

    X = X_cpu
    y = y_cpu

    # Split data (on CPU)
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    
    features = X_train.shape[1] 

    # --- 2. REMOVED PolynomialFeatures ---
    
    # --- 3. MODIFICATION: StandardScaler is CRITICAL for MLPs (using sklearn) ---
    # (--- 修改：StandardScaler 对 MLP 至关重要 (使用 sklearn) ---)
    print("Applying StandardScaler...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)
    print("StandardScaler applied.")
    
    # --- 4. MODIFICATION: Single-Call MLP Training (using sklearn) ---
    # (--- 修改：一次性调用 MLP 训练 (使用 sklearn) ---)
    
    # Initialize the CPU MLP
    # (初始化 CPU MLP)
    mlp_model = MLPClassifier(
        hidden_layer_sizes=hidden_layer_sizes_param,
        solver='adam',
        learning_rate_init=learning_rate_init_param,
        alpha=alpha_param, # (L2 penalty strength)
        
        max_iter=1000,       # (Max epochs)
        early_stopping=True, # (Stop when val score stops improving)
        validation_fraction=0.2, 
        tol=1e-4,            
        random_state=42
    )
    
    # (Print statement moved to main loop)
    
    # Train on the SCALED, original features
    mlp_model.fit(X_train_scaled, y_train)
    
    # (Fit Model complete.)

    # --- 5. Calculate Final Accuracy ---
    y_train_pred = mlp_model.predict(X_train_scaled) 
    train_accuracy = accuracy_score(y_train, y_train_pred)

    y_val_pred = mlp_model.predict(X_val_scaled) 
    val_accuracy = accuracy_score(y_val, y_val_pred)

    y_test_pred = mlp_model.predict(X_test_scaled) 
    test_accuracy = accuracy_score(y_test, y_test_pred)
    
    # (Print statements moved to main loop)
    
    return train_accuracy, val_accuracy, test_accuracy, features
        
# Main execution block
# (主执行模块)
def main():
    # --- From Cell 1 ---
    possible_n_vals = [10, 12, 14, 16, 18, 20] 
    
    # --- NEW: Define the Hyperparameter Grid for MLP ---
    # (--- 新增：为 MLP 定义超参数网格 ---)
    
    # --- WARNING: THIS GRID SEARCH WILL BE VERY SLOW ON CPU ---
    # (--- 警告：此网格搜索在 CPU 上会非常慢 ---)
    # (--- Consider reducing this list for a faster first test ---)
    # (--- 考虑减少此列表以进行更快的首次测试 ---)
    grid_hidden_layer_sizes = [(300,),(400,) ]
    grid_alpha = [0.1, 0.01] 
    grid_learning_rate_init = [0.01, 0.001]
    
    print(f"Starting MLP Grid Search (on CPU)...")
    print(f"n values: {possible_n_vals}")
    print(f"hidden_layer_sizes values: {grid_hidden_layer_sizes}")
    print(f"alpha (L2) values: {grid_alpha}")
    print(f"learning_rate: {grid_learning_rate_init}")
    
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
        best_result_for_n = (0.5, 0.5, 0.5, n) # (train_acc, val_acc, test_acc, feat)

        # --- NEW: Inner loops for Grid Search (MLP params) ---
        for hls_val in tqdm(grid_hidden_layer_sizes, desc=f"n={n} - Architecture Loop", leave=False):
            for alpha_val in tqdm(grid_alpha, desc=f"n={n} hls={hls_val} - alpha Loop", leave=False):
                lr_val = grid_learning_rate_init[0] 
                
                print(f"\n--- Running: n={n}, hls={hls_val}, alpha={alpha_val}, lr={lr_val} ---")
                
                # --- MODIFICATION: Call the CPU function ---
                # (--- 修改：调用 CPU 函数 ---)
                train_acc, val_acc, test_acc, feat = run_cpu_mlp(n, hls_val, alpha_val, lr_val)
                
                print(f"Result: Train={train_acc:.4f}, Val={val_acc:.4f}, Test={test_acc:.4f}")

                # Check if this is the new best model *for this n*
                if val_acc > best_val_score_for_n:
                    best_val_score_for_n = val_acc
                    best_params_for_n = {'hls': hls_val, 'alpha': alpha_val, 'lr': lr_val}
                    best_result_for_n = (train_acc, val_acc, test_acc, feat)
                    print(f"*** New Best for n={n}: Val Acc={val_acc:.4f} with params={best_params_for_n} ***")
        
        # --- End of Grid Search for 'n' ---
        print(f"--- Best parameters for n={n}: {best_params_for_n} (Val Acc: {best_val_score_for_n:.4f}) ---")
        
        # Store the accuracies from the best model
        best_train_acc_by_n.append(best_result_for_n[0])
        best_val_acc_by_n.append(best_result_for_n[1])
        best_test_acc_by_n.append(best_result_for_n[2])
        best_feat_by_n.append(best_result_for_n[3])
        
    print("--- Grid Search Complete ---")
    print("Best Train Accuracy results (by n):", best_train_acc_by_n)
    print("Best Validation Accuracy results (by n):", best_val_acc_by_n) 
    print("Best Test Accuracy results (by n):", best_test_acc_by_n)
    print("Feature counts (by n):", best_feat_by_n)

    # --- From Cell 4 (MODIFIED FOR MLP PLOT) ---
    print("Plotting Figure: MLP Accuracy (Optimized on CPU)...")
    
    # Plot style
    plt.style.use('science')
    sns.set_context("poster", font_scale=2.0)
    colors = sns.color_palette("pastel", 3)

    success_hlines = [0.94, 0.93, 0.92, 0.91, 0.80, 0.75]  
    
    # --- Create a SINGLE plot for all n ---
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    
    ax.plot(best_feat_by_n, best_test_acc_by_n, marker='o', label='Test (Best)', color=colors[0],
            lw=7, markersize=20)
            
    ax.plot(best_feat_by_n, best_train_acc_by_n, marker='x', label='Train (Best)', color=colors[1],
            linestyle='--', lw=5, markersize=12)
    
    ax.plot(best_feat_by_n, best_val_acc_by_n, marker='^', label='Val (Best)', color=colors[2],
            linestyle=':', lw=5, markersize=12)
    
    for i, n in enumerate(best_feat_by_n):
        if i < len(success_hlines): 
            ax.hlines(success_hlines[i], xmin=n-0.5, xmax=n+0.5, color='gray', linestyle='--', lw=4)
    
    # Customizing the plot
    ax.set_title('Optimized MLP Performance (on CPU)')
    ax.set_xlabel("Number of Original Features (n)")
    ax.set_ylabel("Accuracy")
    
    ax.set_xticks(possible_n_vals) 
    ax.set_xscale('linear') 
    
    ax.legend(loc='lower right', fontsize='medium') 
        
    # Adjust layout
    plt.tight_layout()
    plt.ylim((0.45, 1.0))

    plt.savefig("Figs/MLP/mlp_accuracy_gridsearch_CPU.png")
    print("Saved 'mlp_accuracy_gridsearch_CPU.png' to disk.")
    plt.clf() 
    
    print("--- Script Finished ---")

# Standard Python entry point
if __name__ == "__main__":
    main()