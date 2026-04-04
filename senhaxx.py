import subprocess
import getpass
import sys
VERDE = '\033[32m'
VERMELHO = '\033[31m'
RESET = '\033[0m'
senha = "220614"
senha_confirmacao = getpass.getpass(f'senha: ')
if senha == senha_confirmacao:
    print(VERDE + 'Acesso concedido' + RESET)
    subprocess.run(['python3', 'olho_de_deus.py'])
else:
    print(VERMELHO + 'Acesso negado' + RESET)
    sys.exit()
