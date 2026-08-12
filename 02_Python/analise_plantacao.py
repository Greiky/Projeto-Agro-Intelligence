import pandas as pd

# Caminho do nosso dataset
arquivo = "04_Datasets/dados_plantacao.csv"

# Carregando os dados
plantacao = pd.read_csv(arquivo)

# Exibindo os dados
print("=== AGRO INTELLIGENCE ===")
print("\nDados da plantação:")
print(plantacao)