#Enunciado:

#No arquivo funcoes.py faça a função rolar_dados que recebe como 
#argumento um número inteiro representando a quantidade de 
#dados a serem rolados e devolve um lista contendo os dados rolados. Ou seja, 
#ao fazer a chamada da função rolar_dados(4) 
#a função deve simular a rolagem de 4 dados de 6 
#faces e retornar um lista com 4 valores que podem variar de 1 a 6.

#Importante: Utilize a função random.randint.

#Note que o código abaixo é apenas um exemplo, e como os valores 
#dos dados são aleatórios, os valores na lista serão diferentes.

#Exemplo:
#print(rolar_dados(5))
#Saída:
#[6, 1, 1, 6, 3]


import random 
def rolar_dados(n):
    resultados = []

    for i in range(n):
        dado = random.randint(1, 6)
        resultados.append(dado)

    return resultados