# Federated Learning Configuration
federated:
  n_clients: 4
  dirichlet_alpha: 0.5
  local_estimators: 80
  local_max_depth: 10

# Centralized Baseline
centralized:
  n_estimators: 150
  max_depth: 12
  
# Dataset
dataset:
  n_samples: 2300
  n_classes: 10
  test_size: 0.25
  random_state: 42

# Scalability Test
scalability:
  client_counts: [2, 4, 8, 16]
  n_runs: 30
