"""
Tipo BOOLEANO

Algebra Booleana, criada por george Boole

2 costantes, verdadeiro ou faso

Tru -> Verdadeiro
False-> falso

OBS: Sempre com a inicial maiuscula

Errado: true , false

certo:

True, False

"""
Ativo = True

print(Ativo)

"""
Operações basicas
"""
# Negação (not)?

"""
 Fazendo a Negação se o valor booleano for verdadeiro o resultado sera falso
se for falso sera verdadeiro. ou seja sempre o contrario
"""

print(not Ativo)
logado = False

# Ou (or):

""" 
É Uma Operção Binaria, ou Seja Depende de dois valores. ou um ou outro de ser verdadeiro

True Or True -> True
True or False -> True
False or true -> True
False or False -> False
"""
print(Ativo or logado)

# E (end)

""" 
Tambem é uma operação binaria ou seja, depende de dois valores.  ambos os
 valore devem ser verdadeiros.

 True and True -> True
 True And False -> False
 False And True -> False
 False And False -> False
"""