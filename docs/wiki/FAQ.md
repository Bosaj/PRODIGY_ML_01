# FAQ

**Why only three features (`TotalSqFt`, `BedroomAbvGr`, `FullBath`)?**
This task is intentionally scoped to a simple linear regression exercise — the Prodigy InfoTech internship brief asks specifically for square footage and bed/bath counts, not the full ~80-column Ames dataset.

**Is an RMSE of ~46,378 good?**
It's a reasonable baseline for a three-feature linear model on a dataset where sale prices range roughly from $35,000 to $750,000+. Kaggle leaderboard solutions using the full feature set and gradient-boosted models achieve substantially lower RMSE (often under $15,000), since they capture location, quality, and condition effects this notebook doesn't model.

**Where do `train.csv` and `test.csv` come from?**
They're the standard files from Kaggle's [House Prices — Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) competition and must be placed in `data/` before running the notebook.

**Can I submit `data/submission.csv` to the Kaggle competition?**
Yes, it's formatted for that competition's submission format (`Id`, `SalePrice`), though its score reflects the simplified three-feature model, not a competition-tuned pipeline.

**Does CI check the RMSE value?**
No — CI validates notebook structure and dependency installability only. It doesn't execute the training cells.
