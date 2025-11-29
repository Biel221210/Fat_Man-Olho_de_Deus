import requests
import urllib.parse
import webbrowser
import time
import os
import subprocess
import sys

USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
}

def clear():
    os.system("clear")

def banner():
    print(r"""
_________                    .___                   .__               
\_   ___ \_______   ____   __| _/____   ____   ____ |__|____    ______
/    \  \/\_  __ \_/ __ \ / __ |/ __ \ /    \_/ ___\|  \__  \  /  ___/
\     \____|  | \/\  ___// /_/ \  ___/|   |  \  \___|  |/ __ \_\___ \ 
 \______  /|__|    \___  >____ |\___  >___|  /\___  >__(____  /____  >
        \/             \/     \/    \/     \/     \/        \/     \/ 
    .___                                                              
  __| _/____                                                          
 / __ |/  _ \                                                         
/ /_/ (  <_> )                                                        
\____ |\____/                                                         
     \/                                                               
_________                                                             
\_   ___ \  ____  __ __                                               
/    \  \/_/ __ \|  |  \                                              
\     \___\  ___/|  |  /                                              
 \______  /\___  >____/                                               
        \/     \/      
              🔎 BUSCADOR JUSBRASIL — MODO AVANÇADO 🔎
    """)

def montar_url(query, tribunal=None, cidade=None, area=None):
    base = "https://www.jusbrasil.com.br/busca?"
    params = {"q": query}

    if tribunal:
        params["tribunal"] = tribunal
    if cidade:
        params["cidade"] = cidade
    if area:
        params["area"] = area

    return base + urllib.parse.urlencode(params)

def checar_resultados(url):
    try:
        r = requests.get(url, headers=USER_AGENT, timeout=10)

        if r.status_code != 200:
            return False, f"Código HTTP inesperado: {r.status_code}"

        if "Nenhum resultado encontrado" in r.text:
            return False, "Nenhum resultado encontrado."

        return True, "Resultados encontrados."
    except Exception as e:
        return False, f"Erro: {e}"

def salvar_log(texto):
    desktop = os.path.expanduser("~/Desktop")
    log_path = os.path.join(desktop, "log_busca_jusbrasil.txt")

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(texto + "\n")

def abrir_busca():
    clear()
    banner()
    print("== Busca Avançada no JusBrasil ==")

    termo = input("Nome para pesquisar: ").strip()
    tribunal = input("Tribunal (opcional, ex: TJSP): ").strip() or None
    cidade = input("Cidade (opcional): ").strip() or None
    area = input("Área jurídica (ex: penal): ").strip() or None

    query = urllib.parse.quote(termo)
    url = montar_url(query, tribunal, cidade, area)

    print("\nChecando resultados...")
    ok, msg = checar_resultados(url)

    print(f"\nStatus: {msg}")

    salvar_log(f"Busca por '{termo}' → {msg} → {url}")

    if ok:
        print("Abrindo no navegador...")
        webbrowser.open(url)

def reabrir_olho_de_deus():
    caminho = os.path.join(os.getcwd(), "olho_de_deus.py")

    if not os.path.exists(caminho):
        print("\n[ERRO] O arquivo 'olho_de_Deus.py' não foi encontrado nesta pasta.")
        print("Coloque ele na mesma pasta do painel e tente de novo.")
        return

    print("\nReabrindo o olho_de_deus.py...")
    try:
        subprocess.Popen(["python3", caminho])
        sys.exit(0)  # Fecha o painel atual depois de abrir o script
    except Exception as e:
        print(f"[ERRO] Falha ao abrir olho_de_deus.py: {e}")
