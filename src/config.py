from typing import List

DATASET_NAME = "Atibaia Real Estate Price Prediction"

FEATURES_TO_REMOVE = [
    'Status', 'Referência', 'Referência alternativa', 'Compl.', 'Edf. / Cond.', 
    'Endereço', 'R$ Venda M²', 'R$ Locação M²', 'Data de atualização', 'Fotos', 
    'R$ Locação', 'Captador(es)', 'Promotor(es)', 'Indicador(es)', 'Marcador(es)', 
    'Permuta por'
]

FEATURES_TO_GROUP = ["Finalidade", "Cidade", "Bairro"]

# Here you can input the Feature you want to group, and value is the limit.
FEATURES_TO_GROUP = {
    "Finalidade":30,
    "Cidade":10,
    "Bairro":5
}

# Insert Categorical features here
FEATURES_TO_ENCODE = ["Tipo", "Finalidade", "Bairro", "Cidade"]

# Threshold of area and price to remove outliers
AREA_THRESHOLD = 30000
PRICE_THRESHOLD = 4000000

# Columns for log transformation

FEATURES_TO_LOG = ["R$ Venda", "R$ Cond.", "R$ Iptu", "Área total", "Área"]



# Other configs