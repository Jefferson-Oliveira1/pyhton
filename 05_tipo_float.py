"""
Tipo Float

xasas Decimais

OBS: o Separadpr de casas decimais na programação e o ponto nao a Virgula
"""

# errado do ponto de vista float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))


# Certo do poto de vista Float
valor = 1.44
print(valor)
print(type(valor))

# e possivel fazer duplas atribuições
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))

print(valor2)
print(type(valor2))

# Podeos converter float para um int
"""
Obs: Ao Converter Valores float para inteiros, nos perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# podeos trabalhar tbm numeros complexos

variavel = 5j