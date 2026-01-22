VERMELHO = "\033[1;91m"
RESET = "\033[0m"
gay = input(VERMELHO + """
            [1] O dev do code é gay?
            [2] Eu sou gay?
            Escolha: """ + RESET)
if gay == '1':
    print("Não. Ele é muito sigma, mais que você inclusive.")
elif gay == '2':
    respostas = ["Sim.", "Não.", "Talvez.", "Com certeza!", "De jeito nenhum."]
    print(random.choice(respostas))
else:
    print("Opção inválida.")
