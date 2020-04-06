""" 
Escopo de variaveis

dos casos de escopo:

1 1Vaiaveis Globais:
 - Variaveis Globais Sao Reconhecida, ou Seja Seu Escopo Comprrende, Todo o Programa.

2 - Variaveis Locais:
 - Variaveis Locais Sao Reconhecidas apenas no bloco onde foram declaradas  ou seja seu 
 escopo esta limitada ao bloco aonde foi declarada.

 pada declarar variais em python fazemos

 Nome_da_variVEL = vALOR DA vARIAVEL

 Python  uma linguagem de tipagem Dinamica isso significa que ao declaramos uma variavel
  nos nao colocamos otipo de dado dela este tipo e inferidoao atribuimos o valor a mesma.

Exemplo em C:
in numero = 42:

exemplo em java:
int numero = 42:
"""
Exemplo

numero = 42 # Variavel Global
print(numero)
print(type(numero))
# class "int"

numero = "Geek" 
print(type(numero))
# class "string"


-----------------------------------------------------------------------------------------

numero = 42

if numero > 10:
    novo = numero + 10 # a variavewl novo esta Declarada dentro do if entao ela e Local
    print(novo)
print(novo)
