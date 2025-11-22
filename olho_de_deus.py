import os
import signal
import subprocess
subprocess.run (['clear'])
subprocess.run (['cat', 'art_ascii'])
print('Olá meu filho. Diga, oque queres')
options = input("""
      [1] Informações de sites
      [2] Instalar ferramentas
      [3] Sair
Escolha uma opção: """)

if options == '1':
   info = input("""
                [1] Etapa.com
                [2] Hortolândia.gov
                [3] Sair
Escolha uma opção: """)
   if info == '1':
      subprocess.run (['cat', 'INFO SITE ETAPA'])
   elif info == '2':
      subprocess.run (['cat', 'INFO PREFEITURA HORTOLANDIA'])
   elif info == '3':
      print('Fechando painel')
      exit()

if options == '2':
   tool = input("""
                 [1] RED HAWK
                 [2] GAMKERS DDOS
                 [3] MaxPhisher
                 [4] Sair
Escolha uma opção: """)
   if tool == '1':
      url = 'https://github.com/Tuhinshubhra/RED_HAWK'
      destino = '/home/kali/fat_man'
      subprocess.run (['git', 'clone', url, destino])
      subprocess.run (
         ['php', 'rhawk.php'],
         cwd='home/kali/fat_man/RED_HAWK'
      )
   elif tool == '2':
      url2 = 'https://github.com/gamkers/GAMKERS-DDOS.git'
      destino2 = '/home/kali/fat_man'
      subprocess.run ('apt update && apt upgrade -y', shell=True)
      subprocess.run ('apt install -y python2', shell=True)
      subprocess.run ('apt install -y git', shell=True)
      subprocess.run ('apt install -y figlet', shell=True)
      subprocess.run (['git', 'clone', url2, destino2])
      subprocess.run(
         ['python2', 'GAMKERS-DDOS.py'], cwd='/home/kali/fat_man/GAMKERS-DDOS'
      )
   elif tool == '3':
       subprocess.run("apt install pipx", shell=True)
       subprocess.run("pipx install maxphisher", shell=True)
       subprocess.run("maxphisher", shell=True)
   elif tool == '4':
      exit()
