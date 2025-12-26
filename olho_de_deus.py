import subprocess
import os
from pathlib import Path
import shutil

# SETA O VERDÃO AQUI
VERDE = "\033[92m"
VERDE_NEON = "\033[38;5;46m"
RESET = "\033[0m"

print("\033[0;32m")

# Tenta exibir ASCII inicial
subprocess.run(['clear'])
subprocess.run(['cat', 'art_ascii'], stderr=subprocess.DEVNULL)

# ==========================================
# CONFIG UNIVERSAL
# ==========================================
BASE_DIR = Path.home() / "Fat_Man-Olho_de_Deus"
BASE_DIR.mkdir(exist_ok=True)

# Limpa tela
subprocess.run(["clear"])

# Mostra ASCII salvo na pasta
ascii_path = BASE_DIR / "art_ascii"
if ascii_path.exists():
    subprocess.run(["cat", str(ascii_path)])

# ==========================================
# INSTALAÇÃO UNIVERSAL DE PACOTES
# ==========================================
def instalar_pacote(pacote):
    # Termux (pkg)
    if shutil.which("pkg"):
        print(f"Instalando {pacote} via pkg...")
        subprocess.run(["pkg", "install", "-y", pacote])
        return

    # apt (Ubuntu, Debian, Kali etc)
    if shutil.which("apt"):
        print(f"Instalando {pacote} via apt...")
        subprocess.run(["sudo", "apt", "update", "-y"])
        subprocess.run(["sudo", "apt", "install", "-y", pacote])
        return

    # pacman (Arch, Manjaro)
    if shutil.which("pacman"):
        print(f"Instalando {pacote} via pacman...")
        subprocess.run(["sudo", "pacman", "-Sy", pacote, "--noconfirm"])
        return

    # dnf (Fedora)
    if shutil.which("dnf"):
        print(f"Instalando {pacote} via dnf...")
        subprocess.run(["sudo", "dnf", "install", "-y", pacote])
        return

    # yum (CentOS)
    if shutil.which("yum"):
        print(f"Instalando {pacote} via yum...")
        subprocess.run(["sudo", "yum", "install", "-y", pacote])
        return

    print(f"Não foi possível instalar o pacote {pacote}. Instale manualmente.")

# ==========================================
# ATUALIZAR O REPOSITÓRIO DO PAINEL
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
# FUNÇÃO DE REINICIAR O PAINEL
# ==========================================
def reiniciar():
    subprocess.run(["python3", str(Path(__file__))])
    exit()

# ==========================================
# TELA PRINCIPAL
# ==========================================
print(VERDE_NEON + "Olá meu filho. Diga, o que queres?" + RESET)

options = input("""
      [1] Informações de sites
      [2] Instalar ferramentas
      [3] Scan divino
      [4] Gerador de Pessoas
      [5] Gerador de CPF
      [6] Atualizar Painel
      [7] Sair
Escolha: """)

# ==========================================
# OPÇÃO 1 — INFO DE SITES
# ==========================================
if options == '1':
    info = input("""
[1] Etapa.com
[2] Hortolândia.gov
[3] JusBrasil
[4] Fundação CefetMinas
[5] Voltar ao painel
[6] Sair
Escolha: """)

    if info == '1':
        subprocess.run(["cat", str(BASE_DIR / "INFO SITE ETAPA")])

    elif info == '2':
        subprocess.run(["cat", str(BASE_DIR / "INFO PREFEITURA HORTOLANDIA")])

    elif info == '3':
        subprocess.run(["cat", str(BASE_DIR / "INFO JUSBRASIL")])

    elif info == '4':
        subprocess.run(["cat", str(BASE_DIR / "FUNDAÇÃO CEFETMINAS")])

    elif info == '5':
        reiniciar()

    elif info == '6':
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
[6] Doxxer ToolKit
[7] Seeker (Abra outro terminal e cole o seguinte comando: 'ssh -R 80:localhost:8080 nokey@localhost.run')
[8] Voltar ao painel
[9] Sair
Escolha: """)

    # RED HAWK
    if tool == '1':
        subprocess.run(["git", "clone", "https://github.com/Tuhinshubhra/RED_HAWK"], cwd=BASE_DIR)
        subprocess.run(["php", "rhawk.php"], cwd=BASE_DIR / "RED_HAWK")

    # Gamkers DDOS
    elif tool == '2':
        instalar_pacote("python2")
        subprocess.run(["git", "clone", "https://github.com/gamkers/GAMKERS-DDOS.git"], cwd=BASE_DIR)
        subprocess.run(["python2", "GAMKERS-DDOS.py"], cwd=BASE_DIR / "GAMKERS-DDOS")

    # MaxPhisher
    elif tool == '3':
        subprocess.run("pip install pipx", shell=True)
        subprocess.run("pipx ensurepath", shell=True)
        subprocess.run("pipx install maxphisher", shell=True)
        subprocess.run("maxphisher", shell=True)

    # Track IP
    elif tool == '4':
        instalar_pacote("git")
        instalar_pacote("curl")
        subprocess.run(["git", "clone", "https://github.com/htr-tech/track-ip.git"], cwd=BASE_DIR)
        subprocess.run(["bash", "trackip"], cwd=BASE_DIR / "track-ip")

    # Clownters
    elif tool == '5':
        instalar_pacote("git")
        instalar_pacote("python2")
        subprocess.run(['git', 'clone', 'https://github.com/mike90s15/Clownters.py'], cwd=BASE_DIR)
        subprocess.run(['bash', 'install.sh'], cwd=BASE_DIR / 'Clownters.py')

    # Dooxer Tool Kit
    elif tool == '6':
        instalar_pacote("git")
        instalar_pacote("python3")
        subprocess.run(['git', 'clone', 'https://github.com/Euronymou5/Doxxer-Toolkit'], cwd=BASE_DIR)
        subprocess.run(['sudo', 'bash', 'install.sh'], cwd=BASE_DIR / 'Doxxer-Toolkit')
        subprocess.run(['python3', 'dox_en.py'], cwd=BASE_DIR / 'Doxxer-Toolkit')

    # Seeker
    elif tool == '7':
        subprocess.run(['git', 'clone', 'https://github.com/thewhiteh4t/seeker.git'], cwd=BASE_DIR)
        subprocess.run(['chmod', '+x', 'install.sh'], cwd=BASE_DIR / 'seeker')
        subprocess.run(['./install.sh'], cwd=BASE_DIR / 'seeker')
        subprocess.run(['python3', 'seeker.py'], cwd=BASE_DIR / 'seeker')

    elif tool == '8':
        reiniciar()

    elif tool == '9':
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

    instalar_pacote("nmap")

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

# =========================================
# OPÇÃO 4 - GERADOR DE PESSOAS
# =========================================
elif options == '4':
    subprocess.run(['python3', 'gerador de pessoas.py'])

saida = input("""
[1] Continuar no painel
[2] Sair
Escolha: """)

    if saida == '1':
        reiniciar()
    else:
        exit()

# =========================================
# OPÇÃO 5 - GERADOR DE PESSOAS
# =========================================
elif options == '5':
    subprocess.run(['python3', 'gerador de cpf.py'])

saida = input("""
[1] Continuar no painel
[2] Sair
Escolha: """)

    if saida == '1':
        reiniciar()
    else:
        exit()

# ==========================================
# OPÇÃO 6 — ATUALIZAR PAINEL
# ==========================================
elif options == '6':
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
# OPÇÃO 6 — SAIR
# ==========================================
elif options == '7':
    exit()

















