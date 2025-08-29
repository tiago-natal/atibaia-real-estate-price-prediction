from typing import List


FEATURES_TO_REMOVE = [
    'Status', 'Referência', 'Referência alternativa', 'Compl.', 'Edf. / Cond.', 
    'Endereço', 'R$ Venda M²', 'R$ Locação M²', 'Data de atualização', 'Fotos', 
    'R$ Locação', 'Captador(es)', 'Promotor(es)', 'Indicador(es)', 'Marcador(es)', 
    'Permuta por'
]

FEATURES_TO_GROUP = ["Finalidade", "Cidade", "Bairro"]

# Here you can input the Feature you want to group, and value is the limit.
FEATURES_TO_GROUP = {"Finalidade":30, "Cidade":10, "Bairro":5}

# Other configs