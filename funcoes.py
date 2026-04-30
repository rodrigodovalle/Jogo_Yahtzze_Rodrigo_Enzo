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

# Antes de iniciar este exercício, leia atentamente o enunciado
# do projeto no site da disciplina para evitar perda de nota.

# No jogo de dados, é possível guardar alguns dos dados rolados
# para tentar formar uma combinação específica.

# Precisamos implementar a função guardar_dado no arquivo funcoes.py.
# A função deve receber:
# uma lista de dados rolados
# uma lista de dados já guardados
# um número inteiro representando o índice do dado a ser guardado

# A função deve retornar uma lista com dois valores:
# o primeiro: lista de dados rolados atualizada
# o segundo: lista de dados armazenados no estoque

# Exemplo:

# dados_rolados = [1, 3, 2]
# dados_no_estoque = [1, 2]
# dado_para_guardar = 1

# print(guardar_dado(dados_rolados,
#                    dados_no_estoque,
#                    dado_para_guardar))

# Saída esperada:
# [[1, 2], [1, 2, 3]]

# Explicação:
# O jogador já tem [1, 2] guardados.
# Ele quer guardar o dado de índice 1 da lista [1, 3, 2],
# ou seja, o valor 3.

# A função deve:
# remover esse valor da lista dados_rolados
# adicionar esse valor na lista dados_no_estoque

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    valor = dados_rolados[dado_para_guardar]

    novos_dados_rolados = []
    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            novos_dados_rolados.append(dados_rolados[i])

    novos_dados_no_estoque = []
    for item in dados_no_estoque:
        novos_dados_no_estoque.append(item)

    novos_dados_no_estoque.append(valor)

    return [novos_dados_rolados, novos_dados_no_estoque]
