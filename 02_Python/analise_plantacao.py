import pandas as pd

# ==========================================
# AGRO INTELLIGENCE
# ==========================================

# Caminho do dataset
arquivo = "04_Datasets/dados_plantacao.csv"

# Carregando os dados
plantacao = pd.read_csv(arquivo)

print("==========================================")
print("          🌱 AGRO INTELLIGENCE")
print("==========================================")

print("\nDados da plantação:")
print(plantacao)


# ==========================================
# FUNÇÃO - ANÁLISE DA UMIDADE
# ==========================================

def analisar_umidade(umidade):

    if umidade < 40:
        return "⚠️ ALERTA: Umidade baixa."

    elif umidade > 70:
        return "⚠️ ALERTA: Umidade alta."

    else:
        return "✅ Umidade dentro da faixa analisada."


# ==========================================
# FUNÇÃO - ANÁLISE DA TEMPERATURA
# ==========================================

def analisar_temperatura(temperatura):

    if temperatura < 18:
        return "⚠️ Temperatura baixa."

    elif temperatura > 32:
        return "⚠️ Temperatura alta."

    else:
        return "✅ Temperatura dentro da faixa analisada."


# ==========================================
# FUNÇÃO - ANÁLISE DO pH
# ==========================================

def analisar_ph(ph):

    if ph < 5.5:
        return "⚠️ pH ácido."

    elif ph > 7.0:
        return "⚠️ pH elevado."

    else:
        return "✅ pH dentro da faixa analisada."


# ==========================================
# CÁLCULO DAS MÉDIAS
# ==========================================

temperatura_media = plantacao["Temperatura"].mean()

umidade_media = plantacao["Umidade_Solo"].mean()

ph_medio = plantacao["pH"].mean()


# ==========================================
# RESULTADOS
# ==========================================

print("\n==========================================")
print("          📊 RESUMO DA PLANTAÇÃO")
print("==========================================")

print(f"\n🌡️ Temperatura média: {temperatura_media:.2f} °C")

print(f"💧 Umidade média do solo: {umidade_media:.2f} %")

print(f"🧪 pH médio do solo: {ph_medio:.2f}")


# ==========================================
# ANÁLISE DAS MÉDIAS
# ==========================================

print("\n==========================================")
print("          🔎 ANÁLISE DAS CONDIÇÕES")
print("==========================================")

print("\nUmidade:")
print(analisar_umidade(umidade_media))

print("\nTemperatura:")
print(analisar_temperatura(temperatura_media))

print("\npH:")
print(analisar_ph(ph_medio))


# ==========================================
# ANÁLISE DIÁRIA
# ==========================================

print("\n==========================================")
print("          📅 ANÁLISE DIÁRIA")
print("==========================================")


for indice, linha in plantacao.iterrows():

    data = linha["Data"]
    umidade = linha["Umidade_Solo"]
    temperatura = linha["Temperatura"]
    ph = linha["pH"]

    print("\n------------------------------------------")

    print("📅 Data:", data)

    print("💧 Umidade:", umidade, "%")
    print(analisar_umidade(umidade))

    print("🌡️ Temperatura:", temperatura, "°C")
    print(analisar_temperatura(temperatura))

    print("🧪 pH:", ph)
    print(analisar_ph(ph))