import subprocess
from pathlib import Path
import shutil
import os

clear = "clear" if shutil.which("clear") else "cls"
subprocess.run([clear])

home = str(Path.home())
base_dir = f"{home}/fat_man"

os.makedirs(base_dir, exist_ok=True)

subprocess.run(["cat", "art_ascii"])
print("Olá meu filho. Diga, o que queres?")

options = input("""
[1] Informações de sites
[2] Instalar ferramentas
[3] Sair
[4] Atualizar o painel
Escolha uma opção: """)

# --------------------------
#   FUNÇÃO PARA INSTALAR
# --------------------------
def install_pkg(pkg_name):
    if shutil.which("apt"):
        subprocess.run(f"sudo apt install -y {pkg_name}", shell=True)
    elif shutil.which("pkg"):
        subprocess.run(f"pkg install {pkg_name}", shell=True)
    elif shutil.which("pacman"):
        subprocess.run(f"sudo pacman -S --noconfirm {pkg_name}", shell=True)
    else:
        print("Gerenciador de pacotes não suportado.")

# ------------------------
#  OPTION 1 — INFORMAÇÕES
# ------------------------

if options == '1':
    info = input("""
[1] Etapa.com
[2] Hortolândia.gov
[3] JusBrasil
[4] Sair
Escolha: """)
    
    if info == '1':
        subprocess.run(['cat', 'INFO SITE ETAPA'])
    elif info == '2':
        subprocess.run(['cat', 'INFO PREFEITURA HORTOLANDIA'])
    elif info == '3':
        subprocess.run(['cat', 'INFO JUSBRASIL'])
    else:
        exit()

# ------------------------
#  OPTION 2 — FERRAMENTAS
# ------------------------

if options == '2':
    tool = input("""
[1] RED HAWK
[2] GAMKERS DDOS
[3] MaxPhisher
[4] IP Tracker
[5] Sair
Escolha: """)

    # RED HAWK
    if tool == '1':
        url = 'https://github.com/Tuhinshubhra/RED_HAWK'
        subprocess.run(["git", "clone", url], cwd=base_dir)
        subprocess.run(["php", "rhawk.php"], cwd=f"{base_dir}/RED_HAWK")

    # GAMKERS DDOS
    elif tool == '2':
        install_pkg("python2")
        install_pkg("git")
        install_pkg("figlet")

        url2 = "https://github.com/gamkers/GAMKERS-DDOS.git"
        subprocess.run(["git", "clone", url2], cwd=base_dir)

        subprocess.run(
            ["python2", "GAMKERS-DDOS.py"],
            cwd=f"{base_dir}/GAMKERS-DDOS"
        )

    # MAXPHISHER
    elif tool == '3':
        install_pkg("pipx")
        subprocess.run("pipx install maxphisher", shell=True)
        subprocess.run("maxphisher", shell=True)
    elif tool =='4':
        url3 = git://github.com/htr-tech/track-ip.git
        subprocess.run('apt install git curl -y', shell=True)
        subprocess.run(['git', 'clone', url3], cwd=base_dir)
        subprocess.run(
            ['bash', 'trackip'],
            cwd=f"{base_dir}/trackip"
        )
    elif tool == '5':
        exit()
    if options == '4':
        subprocess.run(['git', 'pull'], cwd=f"{base_dir}Fat_Man-Olho_de_Deus")
