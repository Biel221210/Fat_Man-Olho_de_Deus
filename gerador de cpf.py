import math
import random
def gerar_cpf():
    # Gera os primeiros 9 dígitos do CPF
    cpf = [random.randint(0, 9) for _ in range(9)]

    # Calcula o primeiro dígito verificador
    soma1 = sum((cpf[i] * (10 - i) for i in range(9)))
    digito1 = 11 - (soma1 % 11)
    if digito1 >= 10:
        digito1 = 0
    cpf.append(digito1)

    # Calcula o segundo dígito verificador
    soma2 = sum((cpf[i] * (11 - i) for i in range(10)))
    digito2 = 11 - (soma2 % 11)
    if digito2 >= 10:
        digito2 = 0
    cpf.append(digito2)

    # Formata o CPF no padrão XXX.XXX.XXX-XX
    cpf_formatado = f"{cpf[0]}{cpf[1]}{cpf[2]}.{cpf[3]}{cpf[4]}{cpf[5]}.{cpf[6]}{cpf[7]}{cpf[8]}-{cpf[9]}{cpf[10]}"
    return cpf_formatado
cpf = cpf_formatado = gerar_cpf()
print(f"CPF gerado: {cpf}")
