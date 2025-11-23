import requests
import urllib.parse
import webbrowser
import time
import os

USER_AGENT = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
}

def clear():
    os.system("clear")

def banner():
    print(r"""
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
            🔎 PAINEL AVANÇADO DE CONSULTAS — JUSBRASIL 🔎
    """)

def get_desktop_log_path():
    home = os.path.expanduser("~")
    desktop = os.path.join(home, "Desktop")
    if not os.path.exists(desktop):
        desktop = home  # fallback
    return os.path.join(desktop, "jusbrasil_logs.txt")

LOG_PATH = get_desktop_log_path()

def salvar_log(texto):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(texto + "\n")

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

    print(f"== Buscar por {tipo} ==")
    termo = input(f"{tipo}: ").strip()

    tribunal = input("Tribunal (Opcional, ex: TJSP): ").strip() or None
    cidade = input("Cidade (Opcional): ").strip() or None
    area = input("Área (Opcional): ").strip() or None

    query = urllib.parse.quote(termo)
    url = montar_url(query, tribunal, cidade, area)

    print("\nChecando resultados…")
    ok, msg = checar_resultados(url)

    # SALVAR LOG
    salvar_log(f"[{tipo}] Termo: {termo} | Status: {msg} | URL: {url}")

    print(f"\nStatus: {msg}")

    if ok:
        print("Abrindo no navegador…")
        webbrowser.open(url)

    print("\n(Log salvo no Desktop)")
    input("\nENTER p/ voltar ao menu...")

def main():
    while True:
        clear()
        banner()
        print("""
[1] Buscar por nome
[2] Buscar por advogado
[3] Buscar por processo
[4] Apenas abrir pesquisa manual
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
            termo = input("Termo: ")
            url = f"https://www.jusbrasil.com.br/busca?q={urllib.parse.quote(termo)}"
            webbrowser.open(url)
            salvar_log(f"[Manual] {termo} -> {url}")
            input("\nENTER p/ voltar...")
        elif op == "0":
            clear()
            print("Fechando painel…")
            time.sleep(1)
            break
        else:
            print("Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    main()
