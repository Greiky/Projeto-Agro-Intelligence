import pandas as pd

# Caminho do nosso dataset
arquivo = "04_Datasets/dados_plantacao.csv"

# Carregando os dados
plantacao = pd.read_csv(arquivo)

# Exibindo os dados
print("=== AGRO INTELLIGENCE ===")
print("\nDados da plantação:")
print(plantacao)

# Calculando a temperatura média
Temperatura_media = plantacao["Temperatura"].mean()

print("\nTemperatura média da plantação:")
print(Temperatura_media)

# Calculando a umidade média do solo
Umidade_media = plantacao["Umidade_Solo"].mean()

print("\nUmidade média do solo:")
print(Umidade_media)

# Calculando o pH médio do solo
ph_medio = plantacao["pH"].mean()

print("\npH médio do solo:")
print(ph_medio)

if Umidade_media < 40:
    print("Umidade baixa")

elif Umidade_media > 70:
    print("Umidade alta")

# Analisando a umidade de cada dia
for indice, linha in plantacao.iterrows():

    umidade = linha["Umidade_Solo"]

    print("\nData:", linha["Data"])
    print("Umidade:", umidade)

    if umidade < 40:
        print("⚠️ ALERTA: Umidade baixa.")

    elif umidade > 70:
        print("⚠️ ALERTA: Umidade alta.")

    else:
        print("✅ Umidade dentro da faixa analisada.")


