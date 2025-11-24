# Dataset Information

## 📊 Overview

This directory contains the **bearing vibration dataset** used in the experiments of the paper:

**"Hybrid Edge-Cloud Federated Learning Framework for Predictive Maintenance in Industrial IoT"**

The dataset used in this project comes from **two sources**:

1. **🔹 Real CWRU Features Dataset (from Kaggle)**  
   Loaded automatically from:  
   **https://www.kaggle.com/datasets/brjapon/cwru-bearing-datasets**

2. **🔹 Synthetic CWRU-inspired dataset**  
   Automatically generated inside `federated_pdm_complete.py` when no Kaggle data is found.

The experiments in the paper used **the real Kaggle dataset**, not the synthetic one.

---

## 🎯 Dataset Specifications (Kaggle Version)

| Property | Value |
|----------|-------|
| **Total Samples** | 2,300 |
| **Number of Classes** | 10 (balanced) |
| **Samples per Class** | 230 |
| **Features** | 10 statistical/spectral features |
| **Train/Test Split** | 75% / 25% (stratified) |
| **Data Source** | Kaggle (CWRU Bearing Dataset) |

---

## 🏷️ Fault Categories

| Class ID | Label | Description |
|----------|-------|-------------|
| 0 | Normal | Healthy bearing |
| 1 | IR_007 | Inner Race fault (0.007") |
| 2 | IR_014 | Inner Race fault (0.014") |
| 3 | IR_021 | Inner Race fault (0.021") |
| 4 | OR_007_6 | Outer Race (0.007", 6 o’clock) |
| 5 | OR_014_6 | Outer Race (0.014", 6 o’clock) |
| 6 | OR_021_6 | Outer Race (0.021", 6 o’clock) |
| 7 | Ball_007 | Ball fault (0.007") |
| 8 | Ball_014 | Ball fault (0.014") |
| 9 | Ball_021 | Ball fault (0.021") |

---

## 📈 Extracted Features

### Time-Domain Features
- max  
- min  
- mean  
- rms  
- sd  

### Shape / Statistical Features
- crest  
- form  
- peak-to-peak  
- kurtosis  
- skewness  

---

## 📂 File Structure

data/
├── README.md
├── sample_features.csv # 10 example samples only
└── .gitkeep # keeps folder in Git

yaml
نسخ الكود

**Note:**  
The full Kaggle dataset **is not included** in this repository due to size and licensing.  
It is automatically loaded when running the notebook.

---

## 🔗 Data Sources

- **Primary Dataset (used in all experiments)**  
  Kaggle CWRU Bearing Features Dataset  
  https://www.kaggle.com/datasets/brjapon/cwru-bearing-datasets  

- **Original Raw Data (CWRU)**  
  https://engineering.case.edu/bearingdatacenter  

---

## 💻 Example: Loading the Kaggle Dataset

```python
import pandas as pd

df = pd.read_csv("/kaggle/input/cwru-bearing-datasets/feature_time_48k_2048_load_1.csv")
print(df.head())
🔍 Data Quality Checks
✔ Balanced classes (230 each)
✔ No missing values
✔ Standardized features (z-score)
✔ Strict train/test split (no leakage)
✔ Reproducible (random_state=42)

🎓 Citation
If you use this dataset, please cite:

@inproceedings{skaik2025hybrid,
  title={Hybrid Edge--Cloud Federated Learning Framework for Predictive Maintenance in Industrial IoT},
  author={Skaik, Nahla Nabil},
  booktitle={IEEE Conference Proceedings},
  year={2025},
  organization={IEEE}
}
📧 Contact
For dataset questions:
Nahla Nabil Skaik
📧 nahla.nabil.52@gmail.com
