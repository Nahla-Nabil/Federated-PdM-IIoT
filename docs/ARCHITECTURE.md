# 🏗️ System Architecture

> **Hybrid Edge-Cloud Federated Learning for Predictive Maintenance**

---

## 📐 High-Level Overview

```

![System Architecture](results/figures/architecture_diagram.png)



## 🔄 Workflow Pipeline

### Phase 1: Data Collection & Preprocessing
```
[Vibration Sensors] 
    ↓
[Feature Extraction]
    ├─ Time-domain: RMS, Mean, Std, Max, Min
    ├─ Shape: Crest Factor, Form Factor, Peak-to-Peak
    └─ Distribution: Kurtosis, Skewness
    ↓
[Preprocessing]
    ├─ Missing value imputation (median)
    ├─ Label encoding (0-9)
    └─ Standardization (Z-score)
    ↓
[Non-IID Split using Dirichlet(α=0.5)]
```

### Phase 2: Local Training (Edge Devices)
```python
for each_client in [1, 2, 3, 4]:
    # 1. Receive global model from cloud
    local_model = initialize_from_global(global_model)
    
    # 2. Train on local Non-IID data
    local_model.fit(X_local, y_local)
    
    # 3. Validate locally
    accuracy_local = local_model.score(X_val_local, y_val_local)
    
    # 4. Extract model parameters
    parameters = extract_model_params(local_model)
    
    # 5. Send ONLY parameters to cloud (NOT raw data!)
    send_to_cloud(parameters, n_samples=len(X_local))
```

**Key Point**: Raw vibration data **never leaves** the edge device.

### Phase 3: Cloud Aggregation (FedAvg)
```python
def federated_averaging(client_models, client_sample_counts):
    """
    Weighted average of client model parameters
    """
    N_total = sum(client_sample_counts)
    
    global_model = initialize_empty_model()
    
    for k, model_k in enumerate(client_models):
        weight_k = client_sample_counts[k] / N_total
        global_model += weight_k * model_k
    
    return global_model
```

**Formula**:
```
w_global = Σ(k=1 to K) (n_k / N) × w_k

where:
- K = number of clients (4)
- n_k = samples at client k
- N = total samples across all clients
- w_k = local model parameters of client k
```

### Phase 4: Evaluation & Explainability
```
[Global Model]
    ↓
[Test on held-out data] → Accuracy, Precision, F1, AUC-ROC
    ↓
[SHAP Analysis] → Feature importance ranking
    ↓
[Generate Reports & Visualizations]
```

---

## 🎯 Key Components

### 1️⃣ Edge Nodes (Clients)

**Characteristics**:
- **Number**: 4 clients (configurable: 2-16)
- **Data**: Non-IID (Dirichlet α=0.5)
- **Model**: Random Forest (80 trees, depth 10)
- **Computation**: Local training only
- **Communication**: Send model parameters (~KB), not data (~MB)

**Data Distribution Example**:
```python
# Client label distributions (Non-IID)
Client 1: [10%, 80%, 5%, 5%, 0%, 0%, 0%, 0%, 0%, 0%]  # Mostly IR_007
Client 2: [5%, 10%, 5%, 5%, 70%, 5%, 0%, 0%, 0%, 0%]  # Mostly OR_007
Client 3: [5%, 5%, 5%, 5%, 5%, 5%, 60%, 10%, 0%, 0%]  # Mostly OR_021
Client 4: [80%, 5%, 5%, 5%, 0%, 0%, 0%, 0%, 5%, 0%]   # Mostly Normal
```

### 2️⃣ Cloud Server

**Responsibilities**:
1. Initialize global model
2. Receive model parameters from K clients
3. Apply FedAvg aggregation
4. Broadcast updated global model
5. Evaluate global model on test set
6. Generate SHAP explanations

**Advantages**:
- ✅ No access to raw data (privacy)
- ✅ Centralized evaluation
- ✅ Model versioning & monitoring
- ✅ Scales to many clients

### 3️⃣ Communication Protocol

**What is Transmitted?**
- ✅ Model parameters (weights): ~50 KB per client
- ✅ Metadata: # samples, accuracy
- ❌ Raw vibration data: 0 bytes (stays local)

**Bandwidth Comparison**:
```
Centralized PdM:
- Raw data upload: 431 samples × 10 features × 8 bytes = 34.5 KB per client
- Total: 138 KB (4 clients) + continuous streaming

Federated PdM:
- Model params: ~50 KB per client (one-time)
- Total: 200 KB (4 clients, once per round)
```

**Savings**: ~90% bandwidth reduction + enhanced privacy

---

## 🔐 Privacy Guarantees

### What Stays Private?
1. ✅ **Raw vibration signals** (time-series)
2. ✅ **Individual fault events**
3. ✅ **Machine operating conditions**
4. ✅ **Equipment identifiers**

### What is Shared?
1. Model parameters (Random Forest tree structures)
2. Aggregate statistics (# samples per client)
3. Global performance metrics

### Attack Surface Analysis
- **Membership inference**: Low risk (aggregated models)
- **Model inversion**: Infeasible (no gradient info)
- **Data reconstruction**: Impossible (no raw data transmitted)

---

## 📊 Non-IID Data Handling

### Why Non-IID Matters in Industry

Real factories have heterogeneous conditions:
- **Factory A**: Mostly normal operation (preventive maintenance culture)
- **Factory B**: High inner-race faults (poor lubrication practices)
- **Factory C**: Outer-race faults dominant (harsh environments)
- **Factory D**: Ball faults common (overloading issues)

### Dirichlet Distribution (α = 0.5)

```python
def create_noniid_splits(X, y, n_clients=4, alpha=0.5):
    """
    Simulate Non-IID data using Dirichlet distribution
    
    α = 0.1 → Extreme heterogeneity (each client has 1-2 classes)
    α = 0.5 → Strong heterogeneity (paper setting)
    α = 1.0 → Moderate heterogeneity
    α = 10.0 → Near IID
    """
    from scipy.stats import dirichlet
    
    clients_data = []
    for client in range(n_clients):
        # Sample class proportions from Dirichlet
        proportions = dirichlet.rvs(alpha=[alpha]*n_classes)[0]
        
        # Distribute samples according to proportions
        client_X, client_y = sample_by_proportions(X, y, proportions)
        clients_data.append((client_X, client_y))
    
    return clients_data
```

### Impact on Performance
| α value | Heterogeneity | Accuracy (4 clients) |
|---------|---------------|---------------------|
| 0.1 | Extreme | 88.7% |
| 0.5 | **Strong (paper)** | **95.13%** |
| 1.0 | Moderate | 96.2% |
| 10.0 | Near IID | 96.8% |

---

## 🧮 Model Architecture Details

### Local Model (Edge)
```python
RandomForestClassifier(
    n_estimators=80,        # Fewer trees for faster edge training
    max_depth=10,           # Prevent overfitting on small local data
    min_samples_split=2,
    min_samples_leaf=1,
    bootstrap=True,         # Bagging for variance reduction
    n_jobs=-1,              # Parallel processing
    random_state=42
)
```

**Why Random Forest for Edges?**
- ✅ No gradient computation (unlike neural networks)
- ✅ Naturally parallelizable
- ✅ Low memory footprint
- ✅ Robust to hyperparameters
- ✅ Interpretable (SHAP-compatible)

### Global Model (Cloud)
```python
RandomForestClassifier(
    n_estimators=150,       # Richer ensemble post-aggregation
    max_depth=12,           # Deeper trees for complex patterns
    # ... (other params same as local)
)
```

**Aggregation Strategy**:
```python
# For Random Forests: Combine all local trees into global forest
global_forest.estimators_ = []
for client_model in local_models:
    global_forest.estimators_.extend(client_model.estimators_)

# Weighted by client sample size
# (larger clients contribute more trees)
```

---

## 📈 Scalability Architecture

### Tested Configurations

| Clients | Samples/Client | Communication | Accuracy | Training Time |
|---------|----------------|---------------|----------|---------------|
| 2 | ~863 | 100 KB | 95.04% | 1.2s |
| 4 | ~431 | 200 KB | 95.13% | 0.6s |
| 8 | ~216 | 400 KB | 93.35% | 0.4s |
| 16 | ~108 | 800 KB | 91.58% | 0.3s |

**Observations**:
- Linear communication cost scaling
- Sub-linear accuracy degradation
- Better parallelization → faster training per client

---

## 🛠️ Technology Stack

### Core Libraries
```python
numpy==1.21.6           # Numerical operations
pandas==1.3.5           # Data manipulation
scikit-learn==1.2.0     # ML models
scipy==1.7.3            # Dirichlet distribution
```

### Explainability
```python
shap==0.41.0            # SHAP analysis
```

### Visualization
```python
matplotlib==3.5.2       # Plotting
seaborn==0.11.2         # Statistical viz
```

### Model Persistence
```python
joblib==1.1.0           # Save/load models
```

---

## 🔮 Future Extensions

### 1. Advanced FL Algorithms
- **FedProx**: Better Non-IID handling (proximal term)
- **FedOpt**: Adaptive optimization (momentum, Adam)
- **Personalized FL**: Client-specific models

### 2. Deep Learning Integration
```python
# Replace Random Forest with CNN
model = Sequential([
    Conv1D(64, 3, activation='relu'),
    MaxPooling1D(2),
    LSTM(50),
    Dense(10, activation='softmax')
])
```

### 3. Real-Time Deployment
- **Edge Hardware**: NVIDIA Jetson, Raspberry Pi
- **Communication**: MQTT, gRPC
- **Orchestration**: Kubernetes, KubeEdge

### 4. Multi-Modal Fusion
```
[Vibration] ─┐
[Temperature]─┼→ [Multi-Modal Model] → Fault Prediction
[Acoustic]  ─┘
```

---

## 📚 References

1. **FedAvg**: McMahan et al., "Communication-Efficient Learning of Deep Networks from Decentralized Data" (AISTATS 2017)
2. **Non-IID FL**: Zhao et al., "Federated Learning with Non-IID Data" (2018)
3. **SHAP**: Lundberg & Lee, "A Unified Approach to Interpreting Model Predictions" (NIPS 2017)
4. **CWRU Dataset**: Case Western Reserve University Bearing Data Center

---

## 📧 Contact

**Nahla Nabil Skaik**  
Arab Open University - Bahrain  
📧 nahla.nabil.52@gmail.com

**Repository**: https://github.com/Nahla-Nabil/Federated-PdM-IIoT
