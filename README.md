## Atibaia Real Estate Price Prediction

For my first portfolio project, I tackled the challenge of real estate valuation in Atibaia, Brazil. My goal was to move beyond subjective, manual appraisals and build a machine learning model that could offer a more consistent and data informed pricing baseline for real estate professionals.

### Core Problem

The local real estate market has long relied on manual valuation methods that are often inconsistent and prone to error. This can lead to properties being over or under-priced, negatively impacting both buyers and sellers.

### The Solution

To solve this, I built a data pipeline that involves three key steps:
1.  **Data Cleaning & Preprocessing:** Cleaning and preparing raw data from the local real estate agency.
2.  **Advanced Feature Engineering:** Creating new predictors such as suite-to-bedroom ratios and area proportions to capture nuanced market drivers.
3.  **Model Training:** Implementing an `XGBoost Regressor`, a gradient boosting algorithm known for its high performance on tabular data.

### Key Results
My final model demonstrates strong predictive power on unseen test data, achieving:
*   **R² Score:** **73.02%** (explaining over 73% of the price variance)
*   **Mean Absolute Error (MAE):** **R$ 344,797** (representing the average prediction error in monetary terms)

The results validate this model as a powerful tool to accelerate and improve the accuracy of the real estate valuation workflow.
