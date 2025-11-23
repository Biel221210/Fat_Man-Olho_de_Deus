import subprocess
import requests
import urllib.parse
import webbrowser
import time
import os
from datetime import datetime

subprocess.run(['clear'])

VERDE = "\033[92m"
VERDE_NEON = "\033[38;5;46m"
RESET = "\033[0m"

USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
}

# === LOGGING ==========================================================
def salvar_log(texto):
    desktop = os.path.expanduser("~/Desktop")
    pasta_logs = os.path.join(desktop, "jusbrasil_logs")

    # cria a pasta se não existir
    os.makedirs(pasta_logs, exist_ok=True)

    # nome do arquivo com timestamp
    nome_arquivo = datetime.now().strftime("log_%Y-%m-%d_%H-%M-%S.txt")
    caminho_arquivo = os.path.join(pasta_logs, nome_arquivo)

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(texto)

    return caminho_arquivo


# === SISTEMA ==========================================================
def clear():
    os.system("clear")


def banner():
    print(VERDE_NEON + r"""
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
        🔎 PAINEL AVANÇADO — OSINT LITE 🔎
    """+ VERDE)


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
            return False, f"HTTP {r.status_code}"

        if "Nenhum resultado encontrado" in r.text:
            return False, "Nenhum resultado encontrado."

        return True, "Resultados encontrados."

    except Exception as e:
        return False, f"Erro: {e}"


def abrir_busca(tipo):
    clear()
    banner()
    print(f"== Buscar por: {tipo} ==")

    termo = input(f"{tipo.capitalize()}: ").strip()
    tribunal = input("Tribunal (opcional): ").strip() or None
    cidade = input("Cidade (opcional): ").strip() or None
    area = input("Área (opcional): ").strip() or None

    query = urllib.parse.quote(termo)
    url = montar_url(query, tribunal, cidade, area)

    print("\nChecando resultado...")
    ok, msg = checar_resultados(url)

    # montar log
    texto_log = f"""
==== JUSBRASIL OSINT LITE ====
Tipo de busca: {tipo}
Termo: {termo}
Tribunal: {tribunal}
Cidade: {cidade}
Área: {area}
URL: {url}

Status: {msg}
Timestamp: {datetime.now()}
"""

    caminho_log = salvar_log(texto_log)

    print(f"\nStatus: {msg}")
    print(f"Log salvo em:\n{caminho_log}")

    if ok:
        print("\nAbrindo no navegador...")
        webbrowser.open(url)

    input("\nENTER para voltar ao menu...")


# === MENU ==============================================================
def main():
    while True:
        clear()
        banner()
        print("""
[1] Buscar por nome
[2] Buscar por advogado
[3] Buscar por número de processo
[4] Pesquisa manual
[0] Sair
        """)

        op = input("> ").strip()

        if op == "1":
            abrir_busca("nome")
        elif op == "2":
            abrir_busca("advogado")
        elif op == "3":
            abrir_busca("processo")
        elif op == "4":
            termo = input("Digite o termo: ")
            url = f"https://www.jusbrasil.com.br/busca?q={urllib.parse.quote(termo)}"
            print("Abrindo no navegador...")
            webbrowser.open(url)
            time.sleep(2)
        elif op == "0":
            clear()
            print("Fechando painel... ✨")
            time.sleep(1)
            break
        else:
            print("Opção inválida.")
            time.sleep(1)


if __name__ == "__main__":
    main()
