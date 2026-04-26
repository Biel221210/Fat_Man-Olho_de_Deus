import random
import subprocess
import os
from pathlib import Path
import shutil
from InquirerPy import prompt

# SETA AS CORES AQUI
VERDE = "\033[92m"
VERDE_NEON = "\033[38;5;46m"
VERMELHO = "\033[1;31m"
MAGENTA = "\033[1;95m"
AZUL = "\033[1;94m"
CIANO = "\033[1;96m"
VERMELHO2 = "\033[1;91m"
RESET = "\033[0m"

print("\033[0;32m")

subprocess.run(['clear'])
subprocess.run(['cat', 'art_ascii'], stderr=subprocess.DEVNULL)

# ==========================================
# CONFIG UNIVERSAL
# ==========================================
BASE_DIR = Path.home() / "Fat_Man-Olho_de_Deus"
BASE_DIR.mkdir(exist_ok=True)

subprocess.run(["clear"])

ascii_path = BASE_DIR / "art_ascii"
if ascii_path.exists():
    subprocess.run(["cat", str(ascii_path)])

# ==========================================
# INSTALAÇÃO UNIVERSAL DE PACOTES
# ==========================================
def instalar_pacote(pacote):

    if shutil.which("pkg"):
        subprocess.run(["pkg", "install", "-y", pacote])
        return

    if shutil.which("apt"):
        subprocess.run(["sudo", "apt", "update", "-y"])
        subprocess.run(["sudo", "apt", "install", "-y", pacote])
        return

    if shutil.which("pacman"):
        subprocess.run(["sudo", "pacman", "-Sy", pacote, "--noconfirm"])
        return

    if shutil.which("dnf"):
        subprocess.run(["sudo", "dnf", "install", "-y", pacote])
        return

    if shutil.which("yum"):
        subprocess.run(["sudo", "yum", "install", "-y", pacote])
        return

    print(f"Instale manualmente: {pacote}")

# ==========================================
# ATUALIZAR O REPOSITÓRIO DO PAINEL
# ==========================================
def atualizar_repo():

    if (BASE_DIR / ".git").exists():

        subprocess.run(["git", "pull"], cwd=BASE_DIR)

    else:

        subprocess.run([
            "git", "clone",
            "https://github.com/Biel221210/Fat_Man-Olho_de_Deus.git",
            str(BASE_DIR)
        ])

# ==========================================
# FUNÇÃO DE REINICIAR
# ==========================================
def reiniciar():

    subprocess.run(["python3", str(Path(__file__))])
    exit()

# ==========================================
# MENU PRINCIPAL
# ==========================================
menu = prompt([
    {
        "type": "list",
        "message": "Escolha uma opção:",
        "choices": [
            {"name": "Info de Sites", "value": "1"},
            {"name": "Ferramentas", "value": "2"},
            {"name": "Scan divino", "value": "3"},
            {"name": "Gerador de Pessoas", "value": "4"},
            {"name": "Gerador de CPF", "value": "5"},
            {"name": "Atualizar Painel", "value": "6"},
            {"name": "Teste de Gayzisses", "value": "7"},
            {"name": "Sair", "value": "8"},
        ],
        "name": "opcao"
    }
])["opcao"]

# ==========================================
# INFO DE SITES
# ==========================================
if menu == "1":

    info = prompt([
        {
            "type": "list",
            "message": "Escolha o site:",
            "choices": [
                {"name": "Etapa.com", "value": "1"},
                {"name": "Hortolândia.gov", "value": "2"},
                {"name": "JusBrasil", "value": "3"},
                {"name": "Fundação CefetMinas", "value": "4"},
                {"name": "Gov.br", "value": "5"},
                {"name": "Voltar", "value": "6"},
                {"name": "Sair", "value": "7"},
            ],
            "name": "info"
        }
    ])["info"]

    if info == "1":
        subprocess.run(["cat", str(BASE_DIR / "INFO SITE ETAPA")])

    elif info == "2":
        subprocess.run(["cat", str(BASE_DIR / "INFO PREFEITURA HORTOLANDIA")])

    elif info == "3":
        subprocess.run(["cat", str(BASE_DIR / "INFO JUSBRASIL")])

    elif info == "4":
        subprocess.run(["cat", str(BASE_DIR / "FUNDAÇÃO CEFETMINAS")])

    elif info == "5":
        subprocess.run(["cat", str(BASE_DIR / "GOV.BR")])

    elif info == "6":
        reiniciar()

    elif info == "7":
        exit()

    saida = prompt([
        {
            "type": "list",
            "message": "O que deseja fazer?",
            "choices": [
                {"name": "Continuar no painel", "value": "1"},
                {"name": "Sair", "value": "2"},
            ],
            "name": "saida"
        }
    ])["saida"]

    if saida == "1":
        reiniciar()

# ==========================================
# FERRAMENTAS
# ==========================================
elif menu == "2":

    tool = prompt([
        {
            "type": "list",
            "message": "Escolha a ferramenta:",
            "choices": [
                {"name": "RED HAWK", "value": "1"},
                {"name": "GAMKERS DDOS", "value": "2"},
                {"name": "MaxPhisher", "value": "3"},
                {"name": "TrackIP", "value": "4"},
                {"name": "Clownters.py", "value": "5"},
                {"name": "Seeker", "value": "6"},
                {"name": "Voltar", "value": "7"},
                {"name": "Sair", "value": "8"},
            ],
            "name": "tool"
        }
    ])["tool"]

    if tool == "1":
        subprocess.run(["git", "clone", "https://github.com/Tuhinshubhra/RED_HAWK"], cwd=BASE_DIR)
        subprocess.run(["php", "rhawk.php"], cwd=BASE_DIR / "RED_HAWK")

    elif tool == "2":
        instalar_pacote("python2")
        subprocess.run(["git", "clone", "https://github.com/gamkers/GAMKERS-DDOS.git"], cwd=BASE_DIR)
        subprocess.run(["python2", "GAMKERS-DDOS.py"], cwd=BASE_DIR / "GAMKERS-DDOS")

    elif tool == "3":
        subprocess.run("pip install pipx", shell=True)
        subprocess.run("pipx ensurepath", shell=True)
        subprocess.run("pipx install maxphisher", shell=True)
        subprocess.run("maxphisher", shell=True)

    elif tool == "4":
        instalar_pacote("git")
        instalar_pacote("curl")
        subprocess.run(["git", "clone", "https://github.com/htr-tech/track-ip.git"], cwd=BASE_DIR)
        subprocess.run(["bash", "trackip"], cwd=BASE_DIR / "track-ip")

    elif tool == "5":
        instalar_pacote("git")
        instalar_pacote("python2")
        subprocess.run(['git', 'clone', 'https://github.com/mike90s15/Clownters.py'], cwd=BASE_DIR)
        subprocess.run(['bash', 'install.sh'], cwd=BASE_DIR / 'Clownters.py')

    elif tool == "6":
        subprocess.run(['git', 'clone', 'https://github.com/thewhiteh4t/seeker.git'], cwd=BASE_DIR)
        subprocess.run(['chmod', '+x', 'install.sh'], cwd=BASE_DIR / 'seeker')
        subprocess.run(['./install.sh'], cwd=BASE_DIR / 'seeker')
        subprocess.run(['python3', 'seeker.py'], cwd=BASE_DIR / 'seeker')

    elif tool == "7":
        reiniciar()

    elif tool == "8":
        exit()

    saida = prompt([
        {
            "type": "list",
            "message": "Continuar?",
            "choices": [
                {"name": "Sim", "value": "1"},
                {"name": "Sair", "value": "2"},
            ],
            "name": "saida"
        }
    ])["saida"]

    if saida == "1":
        reiniciar()

# ==========================================
# SCAN DIVINO
# ==========================================
elif menu == "3":

    instalar_pacote("nmap")

    escolha = prompt([
        {
            "type": "list",
            "message": "O que deseja scanear?",
            "choices": [
                {"name": "IP agressivo", "value": "1"},
                {"name": "IP stealth", "value": "2"},
                {"name": "Scan vulnerabilidades", "value": "3"},
                {"name": "Site normal", "value": "4"},
                {"name": "Sair", "value": "5"},
            ],
            "name": "scan"
        }
    ])["scan"]

    if escolha == "1":
        Ip = input("IP: ")
        subprocess.run(['nmap', '-A', Ip])

    elif escolha == "2":
        Ip = input("IP: ")
        subprocess.run(['nmap', '-sS', Ip])

    elif escolha == "3":
        site = input("Site: ")
        subprocess.run(['nmap', '--script', 'vuln', site])

    elif escolha == "4":
        site = input("Site: ")
        subprocess.run(['nmap', site])

    elif escolha == "5":
        exit()

    saida = prompt([
        {
            "type": "list",
            "message": "Continuar?",
            "choices": [
                {"name": "Sim", "value": "1"},
                {"name": "Sair", "value": "2"},
            ],
            "name": "saida"
        }
    ])["saida"]

    if saida == "1":
        reiniciar()

# ==========================================
# GERADOR DE PESSOAS
# ==========================================
elif menu == "4":

    subprocess.run(['python3', 'gerador de pessoas.py'])

    saida = prompt([
        {
            "type": "list",
            "message": "Continuar?",
            "choices": [
                {"name": "Sim", "value": "1"},
                {"name": "Sair", "value": "2"},
            ],
            "name": "saida"
        }
    ])["saida"]

    if saida == "1":
        reiniciar()

# ==========================================
# GERADOR DE CPF
# ==========================================
elif menu == "5":

    subprocess.run(['python3', 'gerador de cpf.py'])

    saida = prompt([
        {
            "type": "list",
            "message": "Continuar?",
            "choices": [
                {"name": "Sim", "value": "1"},
                {"name": "Sair", "value": "2"},
            ],
            "name": "saida"
        }
    ])["saida"]

    if saida == "1":
        reiniciar()

# ==========================================
# ATUALIZAR
# ==========================================
elif menu == "6":

    atualizar = prompt([
        {
            "type": "list",
            "message": "Atualizar painel?",
            "choices": [
                {"name": "Sim", "value": "1"},
                {"name": "Sair", "value": "2"},
            ],
            "name": "update"
        }
    ])["update"]

    if atualizar == "1":

        atualizar_repo()

        reiniciar()

# ==========================================
# TESTE
# ==========================================
elif menu == "7":

    subprocess.run(['python3', 'gay_percent.py'])

    saida = prompt([
        {
            "type": "list",
            "message": "Continuar?",
            "choices": [
                {"name": "Sim", "value": "1"},
                {"name": "Sair", "value": "2"},
            ],
            "name": "saida"
        }
    ])["saida"]

    if saida == "1":
        reiniciar()

# ==========================================
# SAIR
# ==========================================
elif menu == "8":

    exit()
