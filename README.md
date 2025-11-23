# Federated-PdM-IIoT
# Hybrid Edge-Cloud Federated Learning for Predictive Maintenance

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![IEEE Conference](https://img.shields.io/badge/conference-IEEE%202025-green.svg)](link-to-conference)

> **Official implementation** of "Hybrid Edge–Cloud Federated Learning Framework for Predictive Maintenance in Industrial IoT"

## 🎯 Overview

This repository contains the complete implementation of a privacy-preserving federated learning framework for bearing fault diagnosis in Industrial IoT environments. The system achieves **95.13% accuracy** while maintaining data privacy across distributed edge nodes.

## ✨ Key Features

- ✅ **Privacy-Preserving**: Raw data never leaves edge devices
- 🔄 **FedAvg Aggregation**: Cloud-based model aggregation
- 📊 **SHAP Explainability**: Transparent feature importance
- 🏭 **Non-IID Support**: Robust across heterogeneous data
- 📈 **Scalable**: Tested with 2-16 clients
- 🎓 **Reproducible**: Fixed random seeds (42)

## 📊 Main Results

| Model | Accuracy | Precision | F1-Score | AUC-ROC |
|-------|----------|-----------|----------|---------|
| **Federated** | **95.13%** | **95.39%** | **95.13%** | **99.45%** |
| Centralized | 94.96% | 95.22% | 94.96% | 99.57% |

## 🚀 Quick Start

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

## 📦 Requirements
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

## 📁 Repository Structure
