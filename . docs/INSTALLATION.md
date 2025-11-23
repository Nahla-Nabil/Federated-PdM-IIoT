# 🔧 Installation Guide

Complete installation instructions for **Federated-PdM-IIoT** framework.

---

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 20.04+)
- **Python**: 3.9 or 3.10 (3.11+ not tested)
- **RAM**: 8GB minimum (16GB recommended)
- **Disk Space**: 500MB for code + dependencies
- **GPU**: Optional (CPU sufficient for this project)

### Check Python Version
```bash
python --version
# Should show: Python 3.9.x or 3.10.x
```

If not installed:
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **macOS**: `brew install python@3.9`
- **Linux**: `sudo apt-get install python3.9`

---

## 🚀 Quick Installation

### Method 1: Using pip (Recommended)

```bash
# 1. Clone repository
git clone https://github.com/Nahla-Nabil/Federated-PdM-IIoT.git
cd Federated-PdM-IIoT

# 2. Create virtual environment (recommended)
python -m venv venv

# 3. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Upgrade pip
pip install --upgrade pip

# 5. Install dependencies
pip install -r requirements.txt

# 6. Verify installation
python -c "import sklearn; import shap; print('✅ Installation successful!')"
```

---

## 🔄 Alternative Installation Methods

### Method 2: Using Conda

```bash
# 1. Clone repository
git clone https://github.com/Nahla-Nabil/Federated-PdM-IIoT.git
cd Federated-PdM-IIoT

# 2. Create conda environment
conda create -n federated-pdm python=3.9 -y
conda activate federated-pdm

# 3. Install dependencies
pip install -r requirements.txt

# Alternative: Install via conda
conda install numpy pandas scikit-learn matplotlib seaborn scipy -c conda-forge
pip install shap==0.41.0  # SHAP not in conda-forge with correct version
```

### Method 3: Development Installation

For contributors who want to modify the code:

```bash
# 1. Clone and enter directory
git clone https://github.com/Nahla-Nabil/Federated-PdM-IIoT.git
cd Federated-PdM-IIoT

# 2. Install in editable mode
pip install -e .

# 3. Install development dependencies
pip install pytest black flake8 jupyter
```

---

## 📦 Dependency Details

### Core Dependencies

```txt
numpy==1.21.6          # Numerical operations
pandas==1.3.5          # Data manipulation
scikit-learn==1.2.0    # Machine learning models (CRITICAL: exact version)
matplotlib==3.5.2      # Plotting
seaborn==0.11.2        # Statistical visualizations
shap==0.41.0           # Explainability (CRITICAL: exact version)
scipy==1.7.3           # Scientific computing (Dirichlet distribution)
joblib==1.1.0          # Model serialization
```

### Version Notes
⚠️ **Critical**: `scikit-learn==1.2.0` and `shap==0.41.0` must match exactly
- SHAP 0.41.0 is compatible with scikit-learn 1.2.0
- Newer versions may cause compatibility issues

---

## 🧪 Verify Installation

### Quick Test

```bash
# Run this to check all imports work:
python -c "
import numpy as np
import pandas as pd
import sklearn
import matplotlib
import seaborn
import shap
import scipy
import joblib
print('✅ All dependencies installed successfully!')
print(f'NumPy: {np.__version__}')
print(f'Pandas: {pd.__version__}')
print(f'Scikit-learn: {sklearn.__version__}')
print(f'SHAP: {shap.__version__}')
"
```

Expected output:
```
✅ All dependencies installed successfully!
NumPy: 1.21.6
Pandas: 1.3.5
Scikit-learn: 1.2.0
SHAP: 0.41.0
```

### Full Test

```bash
# Run the main experiment script
python federated_pdm_complete.py

# Should complete in ~5 minutes and generate:
# - results/figures/*.png (7 plots)
# - results/metrics/*.csv (performance data)
# - results/models/*.pkl (trained models)
```

---

## 🐛 Troubleshooting

### Issue 1: SHAP Import Error

**Error**:
```
ImportError: cannot import name 'TreeExplainer' from 'shap'
```

**Solution**:
```bash
pip uninstall shap
pip install shap==0.41.0 --no-cache-dir
```

---

### Issue 2: Scikit-learn Version Conflict

**Error**:
```
AttributeError: 'RandomForestClassifier' object has no attribute 'estimators_'
```

**Solution**:
```bash
pip uninstall scikit-learn
pip install scikit-learn==1.2.0
```

---

### Issue 3: Matplotlib Backend Error (on macOS/Linux)

**Error**:
```
RuntimeError: Python is not installed as a framework
```

**Solution**:
```bash
# Add to ~/.matplotlib/matplotlibrc
echo "backend: Agg" >> ~/.matplotlib/matplotlibrc

# Or in code (already handled in script):
import matplotlib
matplotlib.use('Agg')
```

---

### Issue 4: NumPy Array Error

**Error**:
```
ValueError: cannot copy sequence with size X to array axis with dimension Y
```

**Solution**:
```bash
pip install numpy==1.21.6 --force-reinstall
```

---

### Issue 5: Memory Error (Low RAM)

**Error**:
```
MemoryError: Unable to allocate array
```

**Solution**:
Reduce model complexity in `config.yaml`:
```yaml
centralized:
  n_estimators: 50  # Reduced from 150
  
federated:
  local_model:
    n_estimators: 30  # Reduced from 80
```

---

### Issue 6: Windows Long Path Error

**Error**:
```
FileNotFoundError: [WinError 206] The filename or extension is too long
```

**Solution**:
```bash
# Enable long paths in Windows 10/11
# 1. Run as Administrator in Command Prompt:
reg add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f

# 2. Restart computer
```

---

## 🔍 Verify GPU Support (Optional)

This project **does not require GPU**, but if you want to check:

```python
import numpy as np
print(f"NumPy BLAS: {np.__config__.show()}")

# For future deep learning extensions:
try:
    import tensorflow as tf
    print(f"TensorFlow GPU: {tf.test.is_gpu_available()}")
except:
    print("TensorFlow not installed (not needed)")
```

---

## 📚 Jupyter Notebook Setup (Optional)

To run the included notebook:

```bash
# Install Jupyter
pip install jupyter notebook

# Start Jupyter
jupyter notebook

# Open: iiot-federated-pdm.ipynb
```

---

## 🐳 Docker Installation (Advanced)

For reproducible environments:

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "federated_pdm_complete.py"]
```

Build and run:
```bash
docker build -t federated-pdm .
docker run -v $(pwd)/results:/app/results federated-pdm
```

---

## 🔄 Updating the Package

To update to the latest version:

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Re-run tests
python federated_pdm_complete.py
```

---

## 🗑️ Uninstallation

To completely remove:

```bash
# 1. Deactivate virtual environment
deactivate

# 2. Remove directory
cd ..
rm -rf Federated-PdM-IIoT

# 3. (Optional) Remove conda env
conda env remove -n federated-pdm
```

---

## 📞 Getting Help

If installation fails:

1. **Check Python version**: `python --version` (must be 3.9 or 3.10)
2. **Check pip**: `pip --version`
3. **Try clean install**:
   ```bash
   pip cache purge
   pip install -r requirements.txt --no-cache-dir
   ```
4. **Create GitHub issue** with:
   - Full error message
   - Python version
   - Operating system
   - Output of `pip list`

**Contact**: nahla.nabil.52@gmail.com

---

## ✅ Next Steps

After successful installation:

1. **Read the paper**: `docs/paper.pdf` (after publication)
2. **Review documentation**: `README.md`, `RESULTS.md`, `docs/ARCHITECTURE.md`
3. **Run experiments**: `python federated_pdm_complete.py`
4. **Explore results**: Check `results/` directory
5. **Modify config**: Edit `config.yaml` for custom experiments

---

## 🎯 Minimum Working Example

To verify everything works:

```python
# test_installation.py
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import shap

# Generate toy data
X, y = make_classification(n_samples=100, n_features=10, n_classes=3, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

# Test SHAP
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X[:10])

print("✅ Installation verified! Ready to run full experiments.")
```

Run: `python test_installation.py`

---

**Successfully installed?** Proceed to `README.md` for usage instructions! 🚀
