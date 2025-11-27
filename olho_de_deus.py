import subprocess
import os
from pathlib import Path
import platform

# SETA O VERDÃO AQUI

VERDE = "\033[92m"
VERDE_NEON = "\033[38;5;46m"
RESET = "\033[0m"

print("\033[0;32m")

subprocess.run(['clear'])
subprocess.run(['cat', 'art_ascii'])

# ==========================================
# CONFIG UNIVERSAL
# ==========================================
BASE_DIR = Path.home() / "Fat_Man-Olho_de_Deus"
BASE_DIR.mkdir(exist_ok=True)

# Limpa tela
subprocess.run(["clear"])

# Mostra ASCII se existir
ascii_path = BASE_DIR / "art_ascii"
if ascii_path.exists():
    subprocess.run(["cat", str(ascii_path)])

# ==========================================
# FUNÇÃO DE ATUALIZAÇÃO DO PAINEL
# ==========================================
def atualizar_repo():
    if (BASE_DIR / ".git").exists():
        print("Atualizando painel...")
        subprocess.run(["git", "pull"], cwd=BASE_DIR)
    else:
        print("Repositório não encontrado. Clonando...")
        subprocess.run([
            "git", "clone",
            "https://github.com/Biel221210/Fat_Man-Olho_de_Deus.git",
            str(BASE_DIR)
        ])

# ==========================================
# LOOP PRINCIPAL DO PAINEL
# ==========================================

def reiniciar():
    subprocess.run(["python3", str(Path(__file__))])
    exit()

print(VERDE_NEON + "Olá meu filho. Diga, o que queres?" + VERDE_NEON)

options = input("""
      [1] Informações de sites
      [2] Instalar ferramentas
      [3] Scan divino
      [4] Atualizar Painel
      [5] Sair
Escolha: """)

# ==========================================
# OPÇÃO 1 — INFO DE SITES
# ==========================================
if options == '1':
    info = input("""
[1] Etapa.com
[2] Hortolândia.gov
[3] JusBrasil
[4] Voltar ao painel
[5] Sair
Escolha: """)

    if info == '1':
        subprocess.run(["cat", str(BASE_DIR / "INFO SITE ETAPA")])

    elif info == '2':
        subprocess.run(["cat", str(BASE_DIR / "INFO PREFEITURA HORTOLANDIA")])

    elif info == '3':
        subprocess.run(["cat", str(BASE_DIR / "INFO JUSBRASIL")])

    elif info == '4':
        reiniciar()

    elif info == '5':
        exit()

    saida = input("""
[1] Continuar no painel
[2] Sair
Escolha: """)

    if saida == '1':
        reiniciar()
    else:
        exit()

# ==========================================
# OPÇÃO 2 — FERRAMENTAS
# ==========================================
if options == '2':
    tool = input("""
[1] RED HAWK
[2] GAMKERS DDOS
[3] MaxPhisher
[4] TrackIP
[5] Clownters.py
[6] Voltar ao painel
[7] Sair
Escolha: """)

    # -------- RED HAWK --------
    if tool == '1':
        subprocess.run(["git", "clone", "https://github.com/Tuhinshubhra/RED_HAWK"], cwd=BASE_DIR)
        subprocess.run(["php", "rhawk.php"], cwd=BASE_DIR / "RED_HAWK")

    # -------- GAMKERS DDOS --------
    elif tool == '2':
        subprocess.run(["git", "clone", "https://github.com/gamkers/GAMKERS-DDOS.git"], cwd=BASE_DIR)
        subprocess.run(["python2", "GAMKERS-DDOS.py"], cwd=BASE_DIR / "GAMKERS-DDOS")

    # -------- MaxPhisher --------
    elif tool == '3': 
        subprocess.run("pip install pipx", shell=True)
        subprocess.run("pipx ensurepath", shell=True)
        subprocess.run("pipx install maxphisher", shell=True)
        subprocess.run("maxphisher", shell=True)
    
    # -------- Track Ip ----------
    elif tool == '4':
        subprocess.run("apt install git curl -y", shell=True)
        subprocess.run(["git", "clone", 'https://github.com/htr-tech/track-ip.git'], cwd=BASE_DIR)
        subprocess.run(["bash", "trackip"], cwd=BASE_DIR / 'track-ip')

    # -------- Clownters --------
    elif tool == '5':
        subprocess.run("apt-get update -y && apt-get upgrade -y", shell=True)
        subprocess.run("apt-get install -y git python2", shell=True)
        subprocess.run(['git', 'clone', 'https://github.com/mike90s15/Clownters.py'], cwd=BASE_DIR)
        subprocess.run(['sudo', 'bash', 'install.sh'], cwd=BASE_DIR / 'Clownters.py')
    
    elif tool == '6':
        reiniciar()

    elif tool == '7':
        exit()

    saida = input("""
[1] Continuar no painel
[2] Sair
Escolha: """)

    if saida == '1':
        reiniciar()
    else:
        exit()
    
    if options == '3':
        subprocess.run('sudo apt install nmap', shell=True)
        Ip_ou_site = input("""
O que desejas scanear, filho meu?
[1] Ip (Agressivo)
[2] Ip (Stealth)
[3] Scan de Vulnerabilidades (site, no caso)
[4] Site (no seco, só)
[5] sair
Escolha: """)
    if Ip_ou_site == '1':
        Ip = input('Qual Ip deseja scanear?')
        subprocess.run(['nmap', '-A', Ip])
    elif Ip_ou_site == '2':
        Ip = input('Qual Ip deseja scanear?')
        subprocess.run(['nmap', '-sS', Ip])
    elif Ip_ou_site == '3':
        site = input('Qual site você deseja scanear?')
        subprocess.run(['nmap', '--script', 'vuln', site])
    elif Ip_ou_site == '3':
        site = input('Qual site você deseja scanear?')
        subprocess.run(['nmap', site])
    elif options == '5':
        exit()
        
    if options == '4':
        Atualizar = input("""
[1] Atualizar o painel
[2] Sair
Escolha: """)
    if Atualizar == '1':
        subprocess.run(['git', 'pull'])
    else:
        exit()

# ==========================================
# OPÇÃO 5 — SAIR
# ==========================================
if options == '5':
    exit()
































