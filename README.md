# FAT_MAN - Olho de Deus 🔥

Um painel em Python estilo "hacking terminal aesthetic", criado para
facilitar acesso a ferramentas, executar utilidades e automatizar
tarefas como clonagem de repositórios, rodar scripts, consultar
informações e instalar ferramentas externas.

Este painel foi criado originalmente para Linux/Kali/Termux, mas
**funciona no Windows** com algumas adaptações.

------------------------------------------------------------------------

## 🚀 Instalação no Windows

1.  Instale o **Python 3**\
    https://www.python.org/downloads/

2.  Instale o **Git**\
    https://git-scm.com/download/win

3.  Instale o **PHP** (necessário para rodar o RED HAWK)\
    https://windows.php.net/download/

4.  Instale o `pipx` (opcional, mas recomendado)
  
    Abra o terminal (CMD/PowerShell):

        python -m pip install pipx
        pipx ensurepath

5.  Instale o **wsl** 
    
        wsl --install

6.  Baixe o repositório do FAT_MAN:

        git clone https://github.com/Biel221210/Fat_Man-Olho_de_Deus.git

7.  Entre na pasta:

        cd Fat_Man-Olho_de_Deus

8.  Execute o painel:

        python olho_de_deus.py

------------------------------------------------------------------------

## 🐧 Instalação no Linux / Kali / Termux

    git clone https://github.com/Biel221210/Fat_Man-Olho_de_Deus.git
    cd Fat_Man-Olho_de_Deus
    python3 olho_de_deus.py

------------------------------------------------------------------------

## 🔧 Funções do Painel

### **1. Informações de sites**

Mostra informações armazenadas em arquivos (`INFO SITE ETAPA`,
`INFO PREFEITURA HORTOLANDIA`, `INFO JUSBRASIL`).

### **2. Instalar ferramentas**

Atualmente inclui:

-   **RED HAWK** (PHP)
-   **GAMKERS DDOS** (Python2)
-   **MaxPhisher** (Python, pipx)
-   **TrackIp** (Shell)

Cada ferramenta é baixada automaticamente com `git clone` e executada no
diretório correto.

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
  **Windows**            ✔ Funciona (depende das ferramentas externas)
  MacOS                  ⚠ Não testado

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
