# Methodology

## Dataset

The [House Prices — Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) dataset (Ames, Iowa housing data) provides `train.csv` (with the `SalePrice` target) and `test.csv` (unlabeled, for the Kaggle-style submission).

## Feature engineering

A single engineered feature, `TotalSqFt`, sums three raw columns:

- Above-ground living area (`GrLivArea`)
- Total basement area (`TotalBsmtSF`)
- 1st + 2nd floor square footage

## Model

A plain `LinearRegression` (scikit-learn) is fit on three features: `TotalSqFt`, `BedroomAbvGr` (bedroom count), and `FullBath` (bathroom count), against the `SalePrice` target.

## Evaluation

The model is evaluated on a held-out test split using **RMSE (Root Mean Squared Error)**:

```
Root Mean Squared Error (RMSE): 46378.46
```

Diagnostic visualizations in the notebook include the target (`SalePrice`) distribution, a feature correlation heatmap, a predicted-vs-actual scatter plot, and a residuals plot — useful for sanity-checking that a three-feature linear model captures the dominant price signal (square footage) without fully modeling location, quality, and condition effects that a richer feature set would need.

## Submission

The trained model's predictions on `data/test.csv` are written to a Kaggle-style `data/submission.csv` (`Id`, `SalePrice` columns).
