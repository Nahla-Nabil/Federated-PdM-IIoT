# Contributing to Federated-PdM-IIoT

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

---

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:

1. **Clear title** describing the bug
2. **Steps to reproduce** the issue
3. **Expected behavior** vs. **actual behavior**
4. **Environment details**:
   - Python version
   - Operating system
   - Library versions (`pip list`)
5. **Error messages** (full traceback if applicable)

**Example**:
```
Title: SHAP analysis fails with scikit-learn 1.3.0

Environment:
- Python 3.9.7
- scikit-learn 1.3.0 (should be 1.2.0)
- Ubuntu 22.04

Error:
AttributeError: 'RandomForestClassifier' object has no attribute 'estimators_'

Steps to reproduce:
1. Install scikit-learn 1.3.0
2. Run python federated_pdm_complete.py
3. Error occurs during SHAP analysis
```

---

### Suggesting Enhancements

For feature requests:

1. **Check existing issues** to avoid duplicates
2. **Describe the use case** - why is this needed?
3. **Propose implementation** (if you have ideas)
4. **Tag with `[FEATURE]`**

---

### Pull Request Process

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub, then:
   git clone https://github.com/YOUR_USERNAME/Federated-PdM-IIoT.git
   cd Federated-PdM-IIoT
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   # or
   git checkout -b fix/bug-description
   ```

3. **Make your changes**
   - Follow coding standards (see below)
   - Add tests if applicable
   - Update documentation

4. **Test your changes**
   ```bash
   # Run the main script
   python federated_pdm_complete.py
   
   # Run tests (if available)
   pytest tests/
   ```

5. **Commit with clear messages**
   ```bash
   git add .
   git commit -m "Add FedProx aggregation algorithm"
   ```

6. **Push and create Pull Request**
   ```bash
   git push origin feature/amazing-feature
   ```
   Then open a PR on GitHub with:
   - Clear description of changes
   - Reference to related issues
   - Screenshots/results if applicable

---

## 📝 Coding Standards

### Python Style Guide

Follow [PEP 8](https://pep8.org/) with these specifics:

```python
# Good ✅
def create_noniid_splits(X, y, n_clients=4, alpha=0.5):
    """
    Split data into Non-IID distributions using Dirichlet.
    
    Args:
        X (np.ndarray): Feature matrix
        y (np.ndarray): Labels
        n_clients (int): Number of clients
        alpha (float): Dirichlet concentration parameter
    
    Returns:
        list: List of (X_client, y_client) tuples
    """
    pass

# Bad ❌
def split(x,y,n,a):
    pass  # No docstring
```

### Documentation

- **Docstrings** for all functions/classes
- **Inline comments** for complex logic
- **Update README** if adding new features
- **Type hints** encouraged:
  ```python
  def train_model(X: np.ndarray, y: np.ndarray) -> RandomForestClassifier:
      pass
  ```

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add FedProx aggregation algorithm
fix: correct Dirichlet sampling bug
docs: update installation instructions
test: add unit tests for data splitting
refactor: simplify SHAP analysis code
```

---

## 🧪 Testing Guidelines

### Before Submitting PR

1. **Run full experiment suite**
   ```bash
   python federated_pdm_complete.py
   ```

2. **Check outputs**
   - Verify figures are generated
   - Check metrics are reasonable
   - Ensure no errors in logs

3. **Test with different configurations**
   ```bash
   # Test with different client counts
   python federated_pdm_complete.py --clients 2
   python federated_pdm_complete.py --clients 8
   ```

### Unit Tests (if adding)

```python
# tests/test_federated.py
import unittest
import numpy as np
from federated_utils import create_noniid_splits

class TestFederatedUtils(unittest.TestCase):
    def test_noniid_split_total_samples(self):
        X = np.random.rand(100, 10)
        y = np.random.randint(0, 3, 100)
        splits = create_noniid_splits(X, y, n_clients=4)
        
        total = sum(len(X_c) for X_c, _ in splits)
        self.assertEqual(total, 100)
```

---

## 🎯 Priority Areas for Contribution

### High Priority
- [ ] Real dataset integration (CWRU, IMS)
- [ ] FedProx/FedOpt algorithms
- [ ] Deep learning models (CNN, LSTM)
- [ ] Real-time deployment examples

### Medium Priority
- [ ] Multi-modal sensor fusion
- [ ] Hyperparameter optimization
- [ ] Docker containerization
- [ ] Unit test coverage

### Low Priority
- [ ] Additional visualizations
- [ ] Performance benchmarks
- [ ] Tutorial notebooks
- [ ] Documentation translations

---

## 📋 Pull Request Checklist

Before submitting, ensure:

- [ ] Code follows PEP 8 style guide
- [ ] All functions have docstrings
- [ ] Changes are tested and work correctly
- [ ] Documentation is updated (README, docs/)
- [ ] No unnecessary files committed (.pyc, .pkl, etc.)
- [ ] Commit messages are clear and descriptive
- [ ] PR description explains what and why
- [ ] Related issues are referenced (Fixes #123)

---

## 🚫 What NOT to Contribute

Please avoid:

- **Breaking changes** without discussion
- **Large datasets** (use external links instead)
- **Generated files** (models, figures) unless examples
- **Unrelated features** outside PdM/FL scope
- **Untested code** that breaks existing functionality

---

## 💬 Getting Help

If you need assistance:

1. **Check existing issues** and documentation
2. **Ask in Discussions** (preferred for questions)
3. **Create an issue** with `[QUESTION]` tag
4. **Email maintainer**: nahla.nabil.52@gmail.com

---

## 📜 Code of Conduct

### Our Standards

✅ **Positive Behavior**:
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what's best for the community

❌ **Unacceptable Behavior**:
- Trolling, insulting, or derogatory comments
- Public or private harassment
- Publishing others' private information
- Other unprofessional conduct

### Enforcement

Violations may result in:
1. Warning
2. Temporary ban
3. Permanent ban

Report issues to: nahla.nabil.52@gmail.com

---

## 🎓 Recognition

Contributors will be:
- Listed in README acknowledgments
- Mentioned in release notes
- Credited in future publications (if significant contribution)

---

## 📚 Resources

- [Python PEP 8 Style Guide](https://pep8.org/)
- [NumPy Docstring Guide](https://numpydoc.readthedocs.io/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)

---

## 🙏 Thank You!

Every contribution, no matter how small, makes a difference!

**Questions?** Open an issue or contact nahla.nabil.52@gmail.com
