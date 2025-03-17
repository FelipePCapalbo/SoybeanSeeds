import requests

# URL da API GraphHopper
GRAPHOPPER_URL = "http://localhost:8989/route"

# Origem e destino (exemplo: São Paulo → Rio de Janeiro)
origem = "-23.55052,-46.633308"  # São Paulo (SP)
destino = "-22.906847,-43.172897"  # Rio de Janeiro (RJ)

# Parâmetros ajustados para forçar alternativas
params = {
    "point": [origem, destino],
    "profile": "car",
    "locale": "pt",
    "ch.disable": "true",  # Desativa CH para permitir alternativas
    "alternative_route.max_paths": 5,  # Aumenta o número de alternativas
    "alternative_route.max_weight_factor": 3.0,  # Permite trajetos até 3x mais longos
    "alternative_route.max_share_factor": 0.6,  # Reduz o compartilhamento do trajeto principal
    "instructions": "false",
}

# Enviar requisição
response = requests.get(GRAPHOPPER_URL, params=params)

# Verificar resposta
if response.status_code == 200:
    data = response.json()

    if "paths" in data and len(data["paths"]) > 0:
        print("\n🚗 Rotas alternativas encontradas:\n")
        for i, rota in enumerate(data["paths"]):
            distancia_km = rota["distance"] / 1000
            tempo_min = rota["time"] / 60000
            print(f"🔹 Rota {i+1}: {distancia_km:.2f} km, Tempo: {tempo_min:.2f} min")
    else:
        print("❌ Nenhuma rota alternativa encontrada.")
else:
    print(f"❌ Erro ao buscar rotas: {response.status_code} {response.text}")
