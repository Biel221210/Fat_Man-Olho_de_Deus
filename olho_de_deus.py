import subprocess
import os
from pathlib import Path

# SETA O VERDÃO AQUI
VERDE = "\033[92m"
VERDE_NEON = "\033[38;5;46m"
RESET = "\033[0m"

print("\033[0;32m")

# Limpa a tela e mostra ASCII inicial (se existir)
subprocess.run(['clear'])
subprocess.run(['cat', 'art_ascii'], stderr=subprocess.DEVNULL)

# ==========================================
# CONFIG UNIVERSAL
# ==========================================
BASE_DIR = Path.home() / "Fat_Man-Olho_de_Deus"
BASE_DIR.mkdir(exist_ok=True)

# Limpa tela
subprocess.run(["clear"])

# Mostra ASCII se existir na pasta principal
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
# FUNÇÃO PARA REINICIAR O PAINEL
# ==========================================
def reiniciar():
    subprocess.run(["python3", str(Path(__file__))])
    exit()

print(VERDE_NEON + "Olá meu filho. Diga, o que queres?" + RESET)

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
elif options == '2':
    tool = input("""
[1] RED HAWK
[2] GAMKERS DDOS
[3] MaxPhisher
[4] TrackIP
[5] Clownters.py
[6] Voltar ao painel
[7] Sair
Escolha: """)

    if tool == '1':
        subprocess.run(["git", "clone", "https://github.com/Tuhinshubhra/RED_HAWK"], cwd=BASE_DIR)
        subprocess.run(["php", "rhawk.php"], cwd=BASE_DIR / "RED_HAWK")

    elif tool == '2':
        subprocess.run(["git", "clone", "https://github.com/gamkers/GAMKERS-DDOS.git"], cwd=BASE_DIR)
        subprocess.run(["python2", "GAMKERS-DDOS.py"], cwd=BASE_DIR / "GAMKERS-DDOS")

    elif tool == '3':
        subprocess.run("pip install pipx", shell=True)
        subprocess.run("pipx ensurepath", shell=True)
        subprocess.run("pipx install maxphisher", shell=True)
        subprocess.run("maxphisher", shell=True)

    elif tool == '4':
        subprocess.run("apt install git curl -y", shell=True)
        subprocess.run(["git", "clone", 'https://github.com/htr-tech/track-ip.git'], cwd=BASE_DIR)
        subprocess.run(["bash", "trackip"], cwd=BASE_DIR / 'track-ip')

    elif tool == '5':
        subprocess.run("apt-get update -y && apt-get upgrade -y", shell=True)
        subprocess.run("apt-get install -y git python2", shell=True)
        subprocess.run(['git', 'clone', 'https://github.com/mike90s15/Clownters.py'], cwd=BASE_DIR)
        subprocess.run(['bash', 'install.sh'], cwd=BASE_DIR / 'Clownters.py')

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

# ==========================================
# OPÇÃO 3 — SCAN DIVINO (NMAP)
# ==========================================
elif options == '3':
    subprocess.run('sudo apt install nmap -y', shell=True)

    escolha = input("""
O que desejas scanear, filho meu?

[1] Ip (Agressivo)
[2] Ip (Stealth)
[3] Scan de Vulnerabilidades (site)
[4] Site (normal)
[5] Sair
Escolha: """)

    if escolha == '1':
        Ip = input('Qual IP deseja scanear? ')
        subprocess.run(['nmap', '-A', Ip])

    elif escolha == '2':
        Ip = input('Qual IP deseja scanear? ')
        subprocess.run(['nmap', '-sS', Ip])

    elif escolha == '3':
        site = input('Qual site você deseja scanear? ')
        subprocess.run(['nmap', '--script', 'vuln', site])

    elif escolha == '4':
        site = input('Qual site deseja scanear? ')
        subprocess.run(['nmap', site])

    elif escolha == '5':
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
# OPÇÃO 4 — ATUALIZAR PAINEL
# ==========================================
elif options == '4':
    atualizar = input("""
[1] Atualizar o painel
[2] Sair
Escolha: """)

    if atualizar == '1':
        atualizar_repo()
        reiniciar()
    else:
        exit()

# ==========================================
# OPÇÃO 5 — SAIR
# ==========================================
elif options == '5':
    exit()
