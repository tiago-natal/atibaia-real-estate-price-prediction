import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def model_training(df: pd.DataFrame):
    # Separation of Features and target
    # X has the features
    # y_log is the log of target.
    X = df.drop("R$ Venda_log", axis=1)
    y_log = df["R$ Venda_log"]

    # Division of train and test
    X_train, X_test, y_train_log, y_test_log = train_test_split(X, y_log,
        test_size=0.3, random_state=101
    )

    # XGBoost Model train
    model_xgb = xgb.XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        random_state=42,
        n_jobs=-1
    )

    # Trains the model with the processed data
    model_xgb.fit(X_train, y_train_log)

    print(f"Model trained with {X_train.shape[0]} samples")
    print(f"The Model will be tested with {X_test.shape[0]} samples not seen.")


    # Predictions storage
    predictions_log = model_xgb.predict(X_test)

    # Reverting Log for avaliation
    y_test_reais = np.expm1(y_test_log)
    prediciton_reais = np.expm1(predictions_log)

    # Performance metrics creation
    r2 = r2_score(y_test_reais, prediciton_reais)
    mae = mean_absolute_error(y_test_reais, prediciton_reais)
    rmse = np.sqrt(mean_squared_error(y_test_reais, prediciton_reais))
    
    print("Final XGBoost Metrics")
    print(f"R² (Coefficient of Determination): {r2:.2%}")
    print(f"MAE (Mean Absolute Error): R$ {mae:,.2f}")
    print(f"RMSE (Root Mean Squared Error): R$ {rmse:,.2f}")