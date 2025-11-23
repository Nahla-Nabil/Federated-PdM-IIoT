# Dataset Information

## CWRU Bearing Dataset

This project uses the **Case Western Reserve University Bearing Data Center** dataset.

### Download Instructions

1. Visit: [CWRU Bearing Data Center](https://engineering.case.edu/bearingdatacenter/download-data-file)
2. Download these files:
   - Normal Baseline Data (12k Drive End Bearing Fault Data)
   - Inner Race Fault: 0.007", 0.014", 0.021"
   - Outer Race Fault: 0.007", 0.014", 0.021"
   - Ball Fault: 0.007", 0.014", 0.021"

### Data Preprocessing

The code automatically:
- Extracts time-domain features (mean, std, RMS, kurtosis, etc.)
- Extracts frequency-domain features (FFT peaks, spectral centroid)
- Normalizes features using StandardScaler

### Expected Format

Place `.mat` files in this directory:
```
data/
├── Normal_0.mat
├── IR007_0.mat
├── OR007_6_0.mat
└── ...
```

**Note:** Raw data files are not included due to size constraints. Download from the official source above.
```

---

### 3️⃣ **إضافة ملف .gitignore**
```
Add file → Create new file
اسم الملف: .gitignore
```
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# Jupyter Notebook
.ipynb_checkpoints

# Models and Results
*.pkl
*.joblib
results/figures/*.png
results/metrics/*.csv
results/models/*.pkl

# Data files (too large)
data/*.mat
data/*.csv
data/*.npy

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

---

### 4️⃣ **إضافة ملف config.yaml (اختياري ولكن احترافي)**
```
Add file → Create new file
اسم الملف: config.yaml
