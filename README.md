# House Price Prediction — Linear Regression

![CI](https://github.com/Bosaj/PRODIGY_ML_01/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)

Task 01 of the Prodigy InfoTech Machine Learning internship: predict house sale prices from structural features using linear regression.

An interactive Streamlit demo (`app.py`) trains the model live and lets you predict a price from square footage, bedrooms, and bathrooms — deployable in one click via [share.streamlit.io](https://share.streamlit.io) (point it at `app.py`).

## Overview

Using the [House Prices — Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) dataset (Ames, Iowa housing data), this project engineers a total-living-area feature and fits a linear regression model to predict `SalePrice` from square footage, bedroom count, and bathroom count.

## Features

- Feature engineering: `TotalSqFt` combines above-ground living area, basement area, and 1st/2nd floor square footage.
- Linear regression on `TotalSqFt`, `BedroomAbvGr`, and `FullBath`.
- Model evaluation via RMSE on a held-out test split.
- Visual diagnostics: target distribution, feature correlation heatmap, predicted-vs-actual scatter plot, and residuals plot.
- Generates a Kaggle-style `submission.csv` from the test set.

## Tech Stack

Python, pandas, NumPy, scikit-learn, Matplotlib, Seaborn.

## Getting Started

### Installation
```bash
pip install -r requirements.txt
```

### Usage

Interactive app:
```bash
streamlit run app.py
```

Original analysis notebook:
```bash
jupyter notebook House_Price_Prediction.ipynb
```
The notebook loads `data/train.csv` and `data/test.csv`, trains the model, and writes predictions to `data/submission.csv`. A [static rendering](https://bosaj.github.io/PRODIGY_ML_01/) of the notebook's outputs is also published via GitHub Pages.

## Testing / CI

[`.github/workflows/ci.yml`](.github/workflows/ci.yml) validates the notebook's structural integrity and installs the full dependency set on every push.

## Project Structure

```
PRODIGY_ML_01/
├── data/
│   ├── train.csv
│   └── test.csv
├── app.py                       # Interactive Streamlit demo
├── House_Price_Prediction.ipynb
└── requirements.txt
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE).

## Author

Oussama EL HADJI — [github.com/Bosaj](https://github.com/Bosaj)


## 📊 Monitoring, Controlling, Evaluation & QA

This project includes a standardized 4-Pillar Observability and QA framework:
- **Logs & Prometheus/Grafana Monitoring**: Configured in `monitoring/` with Prometheus scraper configs and Grafana dashboards.
- **Health Controlling & Evaluation**: Liveness/readiness controllers in `monitoring/health.py` and evaluation harness in `scripts/eval_harness.py`.
- **QA & Testing**: Automated Pytest/Vitest integration and CI workflows via `.github/workflows/ci_qa_monitoring.yml`.

For complete instructions, architecture details, and commands, see [docs/MONITORING_AND_QA.md](file:///C:\Users\ROG FLOW\Desktop\Projects\Github_Projects\PRODIGY_ML_01\docs\MONITORING_AND_QA.md).
