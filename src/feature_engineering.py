import pandas as pd
import numpy as np
import config

from config import FEATURES_TO_GROUP, FEATURES_TO_ENCODE, AREA_THRESHOLD, PRICE_THRESHOLD, FEATURES_TO_LOG

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    

    print("Dataframe received")
    print(FEATURES_TO_GROUP)
    for feature, threshold in FEATURES_TO_GROUP.items():
        print(f"Agrupando {feature}(s) com menos de {threshold} imóveis em 'Outra'")
        contagem_cidades = df[feature].value_counts()
        cidades_raras = contagem_cidades[contagem_cidades < threshold].index
        df[feature] = df[feature].replace(cidades_raras, 'Outra')
        # print(df[feature].value_counts()) this is for testing

    # Encoding Categorical features for better model u
    df = pd.get_dummies(df, columns=FEATURES_TO_ENCODE)
    print("Dataset after get_dummies:", df.shape)

    # Filtering DF to use only sell values
    df = df[df["R$ Venda"] > 0]

    # Removing extreme outliers of area and price
    df = df[df["Área total"] < AREA_THRESHOLD]
    df = df[df["R$ Venda"] <= PRICE_THRESHOLD]

    # Creating the feature 'Ano de cadastro' and removing the original
    # This is so the model uses only the year, ignoring month and days
    df["Ano de cadastro"] = df["Data de cadastro"].dt.year
    df = df.drop(columns=["Data de cadastro"])

    # Applying log transformation for selected columns
    for feature in FEATURES_TO_LOG:
        df[feature + "_log"] = np.log1p(df[feature])

    # Creating interaction features
    df["Proporcao_Suites"] = df["Suítes"] / (df["Dormitórios"] + 1)
    df['Area_por_Dormitorio'] = np.expm1(df['Área_log']) / (df['Dormitórios'] + 1)
    df['Proporcao_Area_Construida'] = np.expm1(df['Área_log']) / (np.expm1(df['Área total_log']) + 1e-6)

    # Removing original log transformation columns
    df = df.drop(columns=FEATURES_TO_LOG)

    print(f"Final format for training: {df.shape}")
    print("End of feature engineering")
    return df
    