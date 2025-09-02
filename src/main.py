from feature_engineering import engineer_features
from data_processing import load_and_clean_data
from model_training import model_training
from config import DATASET_NAME


def main():
    """
    Main Prediction Model Function
    """
    print("Executing main code")
    print(f"Starting data processing, feature engineering and model training of {DATASET_NAME}")
    print("\nStarting Data processing function")
    df_clean = load_and_clean_data("data/imoveis-30-07-2025.xls")
    print("\nStarting feature engineering function")
    df_features = engineer_features(df_clean)
    print("\nStarting Model training")
    model_training(df_features)


    print("\nDone")

if __name__ == "__main__":
    main()