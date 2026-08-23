# Getting Started

## Installation

```bash
pip install -r requirements.txt
```

Key dependencies: pandas, NumPy, scikit-learn, Matplotlib, Seaborn.

## Running the project

```bash
jupyter notebook House_Price_Prediction.ipynb
```

The notebook loads `data/train.csv` and `data/test.csv`, engineers the `TotalSqFt` feature, trains the linear regression model, evaluates it on a held-out split, and writes predictions to `data/submission.csv`.

## How CI validates the project

[`.github/workflows/ci.yml`](../.github/workflows/ci.yml) runs on every push: it validates that `House_Price_Prediction.ipynb` is structurally well-formed (via `nbformat`) and installs the full dependency set from `requirements.txt`. It does not re-run the training cells or check the RMSE value.
