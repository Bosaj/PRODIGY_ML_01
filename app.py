from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

DATA_DIR = Path(__file__).parent / "data"


@st.cache_resource
def train_model():
    """Train the same linear regression model as the notebook, on load."""
    train_df = pd.read_csv(DATA_DIR / "train.csv")

    features = ["GrLivArea", "TotalBsmtSF", "1stFlrSF", "2ndFlrSF", "BedroomAbvGr", "FullBath", "SalePrice"]
    train_selected = train_df[features].dropna()
    train_selected["TotalSqFt"] = (
        train_selected["GrLivArea"]
        + train_selected["TotalBsmtSF"]
        + train_selected["1stFlrSF"]
        + train_selected["2ndFlrSF"]
    )

    X = train_selected[["TotalSqFt", "BedroomAbvGr", "FullBath"]]
    y = train_selected["SalePrice"]

    model = LinearRegression()
    model.fit(X, y)
    return model, train_selected


st.title("House Price Prediction")
st.caption(
    "Linear regression trained live (on app start) on the Ames housing "
    "training set, exactly as in the original notebook. Prodigy InfoTech "
    "ML internship, Task 01."
)

model, train_selected = train_model()

st.subheader("Predict a sale price")
total_sqft = st.number_input(
    "Total square footage (above-ground + basement + 1st/2nd floor)",
    min_value=200, max_value=10000, value=1800, step=50,
)
bedrooms = st.number_input("Bedrooms above grade", min_value=0, max_value=10, value=3)
bathrooms = st.number_input("Full bathrooms", min_value=0, max_value=6, value=2)

if st.button("Predict price"):
    input_df = pd.DataFrame(
        [[total_sqft, bedrooms, bathrooms]],
        columns=["TotalSqFt", "BedroomAbvGr", "FullBath"],
    )
    predicted_price = model.predict(input_df)[0]
    st.success(f"Predicted sale price: ${predicted_price:,.2f}")

with st.expander("Model coefficients"):
    st.write(f"TotalSqFt coefficient: {model.coef_[0]:.2f}")
    st.write(f"BedroomAbvGr coefficient: {model.coef_[1]:.2f}")
    st.write(f"FullBath coefficient: {model.coef_[2]:.2f}")
    st.write(f"Intercept: {model.intercept_:.2f}")

with st.expander("Training data preview"):
    st.dataframe(train_selected.head(10))
