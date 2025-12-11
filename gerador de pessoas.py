import random
Nomes_Masculinos = [
    "Miguel", "Arthur", "Heitor", "Theo", "Davi", "Gabriel", "Bernardo", "Samuel", "Lucas", "Matheus",
    "Rafael", "Guilherme", "Enzo", "Pedro", "João", "Nicolas", "Lorenzo", "Cauã", "Felipe", "Henrique",
    "Vitor", "Murilo", "Bruno", "Daniel", "Emanuel", "Caio", "Leonardo", "Eduardo", "Thiago", "Victor",
    "Fernando", "André", "Diego", "Carlos", "Rodrigo", "Alexandre", "Fábio", "Gustavo", "Marcos",
    "Ricardo", "Samuel", "Júlio", "Otávio", "César", "Leandro", "Rômulo", "Dante", "Elias", "Isaac", "Joaquim", "Luan", "Pietro",
    "Renan", "Sérgio", "Túlio", "Wesley", "Yuri", "Zeca"
]
Nomes_Femininos = [
    "Helena", "Alice", "Laura", "Manuela", "Sophia", "Isabella", "Valentina", "Lívia", "Júlia", "Luiza",
    "Maria", "Heloísa", "Eloa", "Giovanna", "Yasmin", "Cecília", "Emanuelly", "Ana", "Beatriz", "Lara",
    "Mariana", "Rafaela", "Isadora", "Melissa", "Clara", "Vitória", "Sarah", "Nicole", "Esther",
    "Luna", "Bianca", "Catarina", "Elisa", "Agatha", "Bruna", "Camila", "Daniela", "Eduarda", "Fabiana",
    "Gabriela", "Isabel", "Juliana", "Karla", "Larissa", "Mirella", "Natália", "Olívia", "Patrícia", "Rosa", "Sabrina", "Tatiana", "Vanessa",
    "Yara", "Zara", "Carolina", "Diana", "Evelyn", "Flávia"
]
Sobrenomes = [
    "Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Almeida", "Costa", "Gomes", "Martins",
    "Araújo", "Barbosa", "Cardoso", "Rocha", "Dias", "Nunes", "Cavalcanti", "Melo", "Lima", "Pereira", "Ribeiro",
    "Carvalho", "Teixeira", "Moreira", "Moura", "Freitas", "Castro", "Campos", "Santana", "Monteiro", "Vasconcelos",
    "Azevedo", "Cunha", "Fonseca", "Mendes", "Barros", "Cordeiro", "Farias", "Pinto", "Lopes", "Vieira", "Rezende",
    "Siqueira", "Tavares", "Guimarães", "Batista", "Duarte", "Sampaio", "Amaral", "César", "Borges", "Macedo", "Ramos"
]

Sexo = input("Escolha o sexo da pessoa a ser gerada (M/F): ").strip().upper()
if Sexo == 'M':
    nome = random.choice(Nomes_Masculinos) 
elif Sexo == 'F':
    nome = random.choice(Nomes_Femininos)

sobrenome = random.choice(Sobrenomes)
idade = random.randint(1, 100)
print(f"Nome: {nome} {sobrenome}")
print(f"Idade: {idade} anos")
