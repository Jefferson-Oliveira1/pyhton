"""
pep8 - python Ennhaproposal

Sao Proposta de Melhoria para a Linguagem python

The  Zem Of python

Import This

A Ideia da Pep8 é que Possamos Escrever Codigo Python de forma Pythonica

[1] - utilizar camel case para nomes de classe:

[2] - utilize Nomes em Minusculo. Separados por underline para funções ou variaveis:
--------------------------------------------------
[3] - utilize quatro espaço para indentação! 
--------------------------------------------------

[4] - Linhas Em Branco
- Separar Funções e Definir Claae Com Duas Linhas em Branco:
- Metodos Dentro de Uma Classe Ser Separados Com Uma Linha Em Branco

[5] - Imports
- Importes deve ser sempre Feitos em linhas Separados

[6] - Espaçoes em espressões e istruçoes

[7] - termine sempre uma Istrução em uma nova linha



==========================================================================================================================

[1]

class Calculadora: # nome correto para classe python com inicial Maiuscula.
    # a Letra C em maiusclo se Chama camel case
    pass

class Calculadora_cientifica: # nome incorreto para Classe nao existe _ existe.
    # Na Verdade Na Junção Das Palavras Ambas tem que estar com Letras Maiuscula
    pass

class CalculadoraCientifica: # Junção Correta
    pass

===========================================================================================================================

[2]

def soma(): # nome Ok Ou Nome Bom para Funções. Nome De Funções Deve Ser Minuscula
    pass

def soma_dois():# nome Ok Ou Nome Bom para Funções
    pass

def Soma():# Nome Ruim para Funções com Letra Maiuscula
    pass

numero = 4  # Nome Bom para Variavel, Tudo minusculo

numero_impar = 5 # Nome Bom para Variavel, Tudo minusculo e com underline separando os Nomes

==========================================================================================================================

[3]

if "a" in "banana":# identação correta com quatro de espaço (nao e recomendado ussar o tap aperte quatro vez o espaço)
    print("tem")
 
if "a" in "banana": #aqui ele vai aguardar um bloco de identação os quatro espaços de indentação 
print ("tem")

==========================================================================================================================

[4]

class Classe:
    pass
linha 1 # Pular Duas Linhas De Uma Classe Para A Outra
linha 2
class OutraClasse:
    pass

==========================================================================================================================

[5]

#Imports Devem Ser Colocados  No Topo Do Arquivo, Logo Depois de quaisquer Cometarios ou docstrings
#  e antes de constantes ou variaveis clobais.

import sys #imports Corretos Cada Um Em Uma Linha (ussado para importar o pacot completo)
import os

from types import StringType, Listype #Um Tipo diferente de import do pacote Type estou importando duas partes
# (usado para importar items separados)

from type import ( # Caso Tenha Muitos Imports De Um Mesmo Pacote, Recomenda-se Fazer Este Tipo:
____StringType,
____ListType,
____SetType
____SetType,
____OutroType
)


import sys. os #import errado pois estao na Mesma Linha

==========================================================================================================================

[6]

# faça

funcaoalgo(algo[1], {outro: 2})

algo(1) # passando parametro

dict ["chave"] = lista[indice]

x  = 1 # Variaveis
y = 3
variavel_longo = 5


# Nao Faça

Funcao( algo [] 1 ], { outro: 2 })

algo_(1) #passando parametro

dict [ "chave" ] = list_[indice]

x              = 1
y              = 3
variavel_longo = 5

==========================================================================================================================

[7]

import this # pule uma linha finalize com enter uma linha em branco
#linha em branco

==========================================================================================================================
"""
import this

