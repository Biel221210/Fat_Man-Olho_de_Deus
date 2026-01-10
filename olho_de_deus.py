
from pathlib import Path
import subprocess
import shutil
import os
import sys

VERDE = "\033[92m"
VERDE_NEON = "\033[38;5;46m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
RESET = "\033[0m"

BASE_DIR = Path.home() / "Fat_Man-Olho_de_Deus"
BASE_DIR.mkdir(exist_ok=True)

ASCII_PATH = BASE_DIR / "art_ascii"

def clear():
    subprocess.run(["clear"])

def pause():
    input(AMARELO + "\nPressione ENTER para continuar..." + RESET)

def reiniciar():
    os.execv(sys.executable, [sys.executable, str(Path(__file__))])

def aviso_legal():
    print(VERMELHO + """
⚠️ AVISO ⚠️
Use este painel APENAS para fins educacionais,
laboratório, CTF ou com permissão explícita.
Você é responsável por tudo que executar aqui.
""" + RESET)
    pause()

def mostrar_ascii():
    clear()
    if ASCII_PATH.exists():
        subprocess.run(["cat", str(ASCII_PATH)])
    else:
        print(VERDE_NEON + "Olho de Deus ativo." + RESET)

def instalar_pacote(pacote):
    if shutil.which("pkg"):
        subprocess.run(["pkg", "install", "-y", pacote])
    elif shutil.which("apt"):
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "install", "-y", pacote])
    elif shutil.which("pacman"):
        subprocess.run(["sudo", "pacman", "-Sy", pacote, "--noconfirm"])
    elif shutil.which("dnf"):
        subprocess.run(["sudo", "dnf", "install", "-y", pacote])
    else:
        print(VERMELHO + f"Instale manualmente: {pacote}" + RESET)

def clone_repo(url, pasta):
    destino = BASE_DIR / pasta
    if not destino.exists():
        subprocess.run(["git", "clone", url, str(destino)])
    return destino

def atualizar_repo():
    if (BASE_DIR / ".git").exists():
        subprocess.run(["git", "pull"], cwd=BASE_DIR)
    else:
        subprocess.run([
            "git", "clone",
            "https://github.com/Biel221210/Fat_Man-Olho_de_Deus.git",
            str(BASE_DIR)
        ])

def menu_principal():
    mostrar_ascii()
    print(VERDE_NEON + "Olá meu filho. Diga, o que queres?\n" + RESET)
    print("""
[1] Informações de sites
[2] Ferramentas
[3] Scan divino (Nmap)
[4] Gerador de Pessoas
[5] Gerador de CPF
[6] Atualizar Painel
[7] Sair
""")
    return input("Escolha: ")

def menu_info():
    print("""
[1] Etapa.com
[2] Hortolândia.gov
[3] JusBrasil
[4] Fundação CefetMinas
[5] Voltar
[6] Sair
""")
    return input("Escolha: ")

def menu_tools():
    print("""
[1] RED HAWK
[2] MaxPhisher
[3] TrackIP
[4] Seeker
[5] Voltar
[6] Sair
""")
    return input("Escolha: ")

def menu_nmap():
    print("""
[1] IP (Agressivo)
[2] IP (Stealth)
[3] Vulnerabilidades (site)
[4] Site normal
[5] Voltar
""")
    return input("Escolha: ")

def main():
    aviso_legal()

    while True:
        opcao = menu_principal()

        if opcao == "1":
            info = menu_info()
            arquivos = {
                "1": "INFO_SITE_ETAPA",
                "2": "INFO_PREFEITURA_HORTOLANDIA",
                "3": "INFO_JUSBRASIL",
                "4": "FUNDACAO_CEFETMINAS"
            }

            if info in arquivos:
                arq = BASE_DIR / arquivos[info]
                if arq.exists():
                    subprocess.run(["cat", str(arq)])
                else:
                    print(VERMELHO + "Arquivo não encontrado." + RESET)
                pause()
            elif info == "5":
                continue
            elif info == "6":
                sys.exit()

        elif opcao == "2":
            tool = menu_tools()

            if tool == "1":
                aviso_legal()
                repo = clone_repo("https://github.com/Tuhinshubhra/RED_HAWK", "RED_HAWK")
                subprocess.run(["php", "rhawk.php"], cwd=repo)

            elif tool == "2":
                aviso_legal()
                subprocess.run("pipx install maxphisher", shell=True)
                subprocess.run("maxphisher", shell=True)

            elif tool == "3":
                aviso_legal()
                instalar_pacote("git")
                instalar_pacote("curl")
                repo = clone_repo("https://github.com/htr-tech/track-ip.git", "track-ip")
                subprocess.run(["bash", "trackip"], cwd=repo)

            elif tool == "4":
                aviso_legal()
                repo = clone_repo("https://github.com/thewhiteh4t/seeker.git", "seeker")
                subprocess.run(["chmod", "+x", "install.sh"], cwd=repo)
                subprocess.run(["./install.sh"], cwd=repo)
                subprocess.run(["python3", "seeker.py"], cwd=repo)

            elif tool == "5":
                continue
            elif tool == "6":
                sys.exit()

        elif opcao == "3":
            instalar_pacote("nmap")
            scan = menu_nmap()

            if scan in ["1", "2", "3", "4"]:
                alvo = input("IP ou site: ")
                if scan == "1":
                    subprocess.run(["nmap", "-A", "-Pn", "-T4", alvo])
                elif scan == "2":
                    subprocess.run(["nmap", "-sS", "-Pn", "-T4", alvo])
                elif scan == "3":
                    subprocess.run(["nmap", "--script", "vuln", alvo])
                elif scan == "4":
                    subprocess.run(["nmap", alvo])
                pause()

        elif opcao == "4":
            script = BASE_DIR / "gerador_pessoas.py"
            if script.exists():
                subprocess.run(["python3", str(script)])
            else:
                print(VERMELHO + "Script não encontrado." + RESET)
                pause()

        elif opcao == "5":
            script = BASE_DIR / "gerador_cpf.py"
            if script.exists():
                subprocess.run(["python3", str(script)])
            else:
                print(VERMELHO + "Script não encontrado." + RESET)
                pause()

        elif opcao == "6":
            atualizar_repo()
            reiniciar()

        elif opcao == "7":
            sys.exit()

        else:
            print(VERMELHO + "Opção inválida." + RESET)
            pause()

if __name__ == "__main__":
    main()
