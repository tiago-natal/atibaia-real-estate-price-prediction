import pandas as pd
import numpy as np
import config

from config import FEATURES_TO_GROUP

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:


    for feature in FEATURES_TO_GROUP:
        print(f"Agrupando {feature.key}")


    print("Agrupando cidades com menos de 10 imóveis em 'Outra'")
    contagem_cidades = imoveis['Cidade'].value_counts()
    cidades_raras = contagem_cidades[contagem_cidades < 10].index
    imoveis['Cidade'] = imoveis['Cidade'].replace(cidades_raras, 'Outra')

    print("Agrupando finalidades com menos de 30 imóveis em 'Outra'")
    contagem_finalidade = imoveis['Finalidade'].value_counts()
    finalidades_raras = contagem_finalidade[contagem_finalidade < 30].index
    imoveis['Finalidade'] = imoveis['Finalidade'].replace(finalidades_raras, 'Outra')
    
    print("")