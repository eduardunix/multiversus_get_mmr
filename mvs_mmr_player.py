import requests
from bs4 import BeautifulSoup
import sys


# Verificando se foram fornecidos argumentos
if len(sys.argv) < 2:
    print("Por favor, forneça um argumento.")
    sys.exit(1)

# Acessando o primeiro argumento
player_id = sys.argv[1]

def obter_informacoes_jogador(player_id):
    url = f"https://tracker.gg/multiversus/profile/wb/{player_id}/overview"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        mmr_element = soup.find("span", class_="mmr")  
        username = soup.find("span", class_="trn-ign__username")
        numero_de_partidas = soup.find("div", class_="stat")  
        if mmr_element and numero_de_partidas:
            partidas = numero_de_partidas.text.strip()
            mmr = mmr_element.text.strip()            
            user = username.text.strip()
            return mmr,partidas, user
        else:
            return None, None
    else:
        print("Erro ao obter página:", response.status_code)
        return None, None
user, mmr, partidas = obter_informacoes_jogador(player_id)
if  partidas:
    print(f"{partidas.replace('Wins','')}")
    print(f"{mmr}")
    print(f"{user}")
else:
    print("Informações do jogador não encontradas.")
