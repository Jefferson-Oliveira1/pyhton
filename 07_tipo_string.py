"""
Tipo String 

Ja Vimos que em python um dado e considerado do tipo string sempre que:

 estiver entre aspas Simples

exemplo
- Estiver entre aspas Simples -> 'uma string ', '1234', 'a', 'True', '42.3'
- Estiver entre aspas Duplas -> "uma string ", "1234", "a", "True", "42.3"
- Estiver entre aspas simples tripas -> '''uma string ''', '''1234''', '''a''', '''True''', '''42.3'''
"""

# Estiver entre aspas duplas triplas ->  """uma string """, """1234""", """a""", """True""", """42.3"""

# nome = 'Geek University'
# nome = ''''Geek University'''
# nome = "Geek University"

==========================================================================================================
print(nome)
print(type(nome))

==========================================================================================================
==========================================================================================================
nome = "Ginas'bars"
print(nome)
print(type(nome))

==========================================================================================================
==========================================================================================================
nome = "angelina \nJolie"
print(nome)
print(type(nome))

==========================================================================================================
==========================================================================================================
nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

==========================================================================================================
==========================================================================================================
nome = 'geek Unversity'
print(nome.upper()) #tudo maiusculo

==========================================================================================================
==========================================================================================================
nome = 'geek Unversity'
print(nome.lowe()) #tudo minusculo

==========================================================================================================
==========================================================================================================
nome = 'geek Unversity'
print(nome.split()) #traforma Lista de string
[  0 ,  1 ,  3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14]
[ 'G', 'e', 'e' ,'k', ' ', 'U', 'n', 'v', 'e', 'r', 's', 'i', 't', 'y']
print(nome[0:4])  # Slice de String
Geek

print(nome[5:15])  # Slice de String
 Unversity

 print(nome.split())
 [  0,         1]
 ['geek', 'Unversity']

  print(nome.split(0))
 ['geek']

   print(nome.split(1))
 ['Unversity']

# [::-1] -. Comece do primeiro elemento, vá até  útimo elemento e inverta

print(mome[::-1]) # Serve para inverter as letras de traz para frente Pythonico
ytisrevinu keeg

==========================================================================================================
==========================================================================================================
print(nome.replace("G", "P"))# Substitui a Letra G pela Letra P
Peek Unversity

print(nome.replace("i", "P"))# Substitui a Letra G pela Letra P
Piik Unvirsity

==========================================================================================================
texto = "Socorram me Subindo onibus em  marocos" #texto em palindromo
print(texto)

print(texto [::-1])
"Socorram me Subindo onibus em  marocos"




