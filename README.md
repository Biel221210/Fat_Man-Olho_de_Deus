# FAT_MAN - Olho de Deus 🔥

Um painel em Python estilo "hacking terminal aesthetic", criado para
facilitar acesso a ferramentas, executar utilidades e automatizar
tarefas como clonagem de repositórios, rodar scripts, consultar
informações e instalar ferramentas externas.

------------------------------------------------------------------------

## 💀 Instala os requesitos, bobão

    sudo apt install python3
    sudo apt install python2
    sudo apt install php
    sudo apt update

(se for no Termux cê substitui "sudo apt" por "pkg")

------------------------------------------------------------------------

## 🐧 Instalação no Linux / Kali / Termux

    git clone https://github.com/Biel221210/Fat_Man-Olho_de_Deus.git
    cd Fat_Man-Olho_de_Deus
    python3 olho_de_deus.py

------------------------------------------------------------------------

## 🔧 Funções do Painel

### **1. Informações de sites**

Mostra informações armazenadas em arquivos (`INFO SITE ETAPA`,
`INFO PREFEITURA HORTOLANDIA`, `INFO JUSBRASIL`, `FUNDAÇÃO CEFET MINAS`).

### **2. Instalar ferramentas**

Atualmente inclui:

-   **RED HAWK** (PHP)
-   **GAMKERS DDOS** (Python2)
-   **MaxPhisher** (Python, pipx)
-   **TrackIp** (Shell)
-   **Clownters.py** (Python)
-   **Seeker** (Python)

Cada ferramenta é baixada automaticamente com `git clone` e executada no
diretório correto.

### **3. Scan Divino**

Te da algumas opções do nmap para scan de site ou ip's

### **4. Gerador de Pessoas**

Gera um nome aleatório de acordo com um sexo escolhido (ele também te da uma idade)

### **5. Gerador de CPF**

usa o cálculo do governo para gerar um CPF

------------------------------------------------------------------------

## ⚙️ Requisitos Gerais

-   Python 3\
-   Git\
-   PHP (para RED HAWK)\
-   pipx (para MaxPhisher)\
-   Shell (para Track-Ip)\
-   Permissão de rede para usar git

No Termux:

    pkg install python git php
    pip install pipx
    pipx ensurepath

------------------------------------------------------------------------

## 💻 Compatibilidade

  Sistema                Suporte
  ---------------------- -----------------------------------------------
  **Kali Linux**         ✔ Total
  **Linux comum**        ✔ Total
  **Termux (Android)**   ✔ Total

------------------------------------------------------------------------

## 📝 Notas importantes

-   Cada ferramenta roda de forma isolada quando possível (via pipx).\
-   Evita instalar dependências desnecessárias.\
-   O projeto está em construção --- melhorias virão.

------------------------------------------------------------------------

## 🤝 Contribuição

Pull requests são bem-vindos!\
Só dá o fork, cria sua branch e mete o commit.

------------------------------------------------------------------------

## 🔥 Autor

Criado por **biel**, o visionário do FAT MAN -- Olho de Deus.

------------------------------------------------------------------------
