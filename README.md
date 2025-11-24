# Hybrid Edge-Cloud Federated Learning for Predictive Maintenance

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![IEEE Conference](https://img.shields.io/badge/conference-IEEE%202025-green.svg)](link-to-conference)

> **Official implementation** of "Hybrid Edge-Cloud Federated Learning Framework for Predictive Maintenance in Industrial IoT"

## Overview

This repository contains the complete implementation of a **privacy-preserving federated learning framework** for bearing fault diagnosis in Industrial IoT environments. The system achieves **95.13% accuracy** while maintaining data privacy across distributed edge nodes.

## Key Features

- **Privacy-Preserving**: Raw data never leaves edge devices
- **FedAvg Aggregation**: Cloud-based model aggregation
- **SHAP Explainability**: Transparent feature importance
- **Non-IID Support**: Robust across heterogeneous data
- **Scalable**: Tested with 2-16 clients
- **Reproducible**: Fixed random seeds (42)

## Main Results

| Model | Accuracy | Precision | F1-Score | AUC-ROC |
|-------|----------|-----------|----------|---------|
| **Federated** | **95.13%** | **95.39%** | **95.13%** | **99.45%** |
| Centralized | 94.96% | 95.22% | 94.96% | 99.57% |

## Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/NahlaSkaik/Federated-PdM-IIoT.git
cd Federated-PdM-IIoT
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Experiments

```bash
python federated_pdm_complete.py
```

## Requirements

```txt
numpy>=1.21.0
pandas>=1.3.0
scikit-learn==1.2.0
matplotlib>=3.5.0
seaborn>=0.11.0
shap==0.41.0
scipy>=1.7.0
joblib>=1.1.0
```

## Repository Structure

```
Federated-PdM-IIoT/
├── federated_pdm_complete.py     # Main implementation
├── requirements.txt              # Dependencies
├── LICENSE                       # MIT License
├── README.md                     # Project documentation
│
├── data/                         # Dataset directory
│   └── README.md                 # Dataset description
│
├── results/                      # Experiment outputs
│   ├── figures/                  # Plots
│   ├── metrics/                  # Metrics CSV files
│   └── models/                   # Saved models
│
└── docs/                         # Additional documentation
    └── README.md

```

## Experiments Included

### 1. Centralized Baseline

```python
# Random Forest with 150 estimators
rf_baseline = RandomForestClassifier(n_estimators=150, max_depth=12)
```

### 2. Federated Learning

```python
# 4 edge clients with Non-IID Dirichlet distribution (α=0.5)
clients_data = create_noniid_splits(X_train, y_train, n_clients=4)
```

### 3. Algorithm Comparison

- Random Forest
- Gradient Boosting
- Decision Tree
- SVM (RBF)

### 4. Scalability Analysis

- Tested: 2, 4, 8, 16 clients
- Mean accuracy tracked across configurations

### 5. SHAP Explainability

```python
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
```

## Generated Outputs

The script automatically generates:

- `1_confusion_matrices.png` - Confusion matrices comparison
- `2_roc_curves.png` - ROC curves
- `3_feature_importance.png` - Top 10 features
- `4_performance_comparison.png` - Metrics comparison
- `5_scalability_analysis.png` - Scalability plot
- `6_shap_summary.png` - SHAP summary
- `7_shap_importance.png` - SHAP importance ranking
- `performance_comparison.csv` - Detailed metrics
- `federated_pdm_complete.pkl` - Saved models

## Citation

If you use this code in your research, please cite:

```bibtex
@inproceedings{skaik2025hybrid,
  title={Hybrid Edge--Cloud Federated Learning Framework for Predictive Maintenance in Industrial IoT},
  author={Skaik, Nahla Nabil},
  booktitle={IEEE Conference Proceedings},
  year={2025},
  organization={IEEE}
}
```

## Paper

**Link:** [IEEE Xplore](link-after-acceptance)  | [GitHub](https://github.com/Nahla-Nabil/Federated-PdM-IIoT.git)

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📖 Documentation
   
   - **[Installation Guide](docs/INSTALLATION.md)** - Detailed setup instructions
   - **[Architecture](docs/ARCHITECTURE.md)** - System design and workflow
   - **[Results](RESULTS.md)** - Complete experimental results

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Nahla Nabil Skaik**  
Arab Open University - Bahrain  
Email: nahla.nabil.52@gmail.com  
GitHub: [@Nahla-Nabil](https://github.com/NahLA-Nabil)
Linkedin: (https://www.linkedin.com/in/nahla-nabil-876597211/)

## Acknowledgments

- Arab Open University - Bahrain for research support
- CWRU Bearing Data Center for dataset inspiration
- IEEE Conference Organizers
- Open-source community for excellent tools

---

**Star this repository if you find it helpful!**
