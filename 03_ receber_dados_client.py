"""
Receber Dados Do Client

input() -> Todo Dado Recebido Via Input e do tipo String

Em Python Stinng e Tudo que Estiver entre:
- Aspas Simples
- Aspas Duplas:
- Aspas Simples Triplas:
- Aspas Duplas Triplas:

Exemplos:
- aspas Simples -> 'Anjolina Jolie'
- aspas duplas -> "Anjolina Jolie"
- aspas Simples tiplas -> '''Anjolina Jolie'''
"""
#- aspas duplas triplas -> """Anjolina Jolie"""

# entrada de dados
# print("Qual O Seu Nome?  ")
# nome = input() # Input -> Entrada 

nome = input("Qual O Seu Nome? ")

# Exempo de Print Antigo 2.x
# print("Seja Bem Vindo(a) %s" % nome)

# Exemplo De Printe Moderno 3.x
# print("Seja Bem-vindo(a) {0}" .format(nome))

# Exemplo De Print Atual3.7
print(f"Seja Bem Vindo(a) {nome}")

# print("Qual Sua Idade? ")
# idade = input()
idade = int(input("Quanos Anos vc tem? "))j
# Processamento

# saida de dados "antigo" 2.x
# print(" %s Tem %s Anos" % (nome, idade))

# Exmplo De Print Moderno 3.x
# print("A {0} Tem {1}" .format(nome, idade))

# Exemplo De Print Atual3.7

# print(f"A {nome} Tem {idade} anos")

"""
# int(idade) -> cast
cast e a "conversao"de um tipo de dado para outro

"""
print(f"{nome} Nasceu em {2020 - idade}")