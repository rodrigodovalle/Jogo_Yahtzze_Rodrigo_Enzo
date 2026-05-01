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


# No jogo de dados, também é possível remover os dados já armazenados.

# Precisamos implementar a função remover_dado no arquivo funcoes.py.
# A função recebe:
# uma lista de dados rolados
# uma lista de dados já guardados
# um número inteiro com o índice do dado a ser removido

# A função deve retornar uma lista com dois valores:
# o primeiro é a lista de dados rolados atualizada
# o segundo é a lista de dados no estoque

# Exemplo:

# dados_rolados = [2, 2, 2, 2]
# dados_no_estoque = [1]
# dado_para_remover = 0

# print(remover_dado(dados_rolados, dados_no_estoque, dado_para_remover))

# Saída:
# [[2, 2, 2, 2, 1], []]

# Explicação:
# o jogador tem o dado [1] guardado
# ele decide remover esse dado do estoque

# a função deve:
# remover o valor da lista dados_no_estoque
# adicionar esse valor na lista dados_rolados

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    novo_estoque = []
    for i in range(len(dados_no_estoque)):
        if i == dado_para_remover:
            dados_rolados = dados_rolados + [dados_no_estoque[i]]
        else:
            novo_estoque = novo_estoque + [dados_no_estoque[i]]
    return [dados_rolados, novo_estoque]


#Ex 4

def calcula_pontos_regra_simples(dados):
    pontos = {}

    for numero in range(1, 7):
        soma = 0
        for dado in dados:
            if dado == numero:
                soma += dado
        pontos[numero] = soma

    return pontos

# Ex 5

def calcula_pontos_soma(dados):
    soma = 0

    for dado in dados:
        soma += dado

    return soma

# Ex 6

def calcula_pontos_sequencia_baixa(dados):
    unicos = sorted(set(dados))

    for i in range(len(unicos) - 3):
        if (unicos[i] + 1 == unicos[i+1] and
            unicos[i] + 2 == unicos[i+2] and
            unicos[i] + 3 == unicos[i+3]):
            return 15

    return 0

# Ex 7

def calcula_pontos_sequencia_alta(dados):

    if (1 in dados and 2 in dados and 3 in dados and 4 in dados and 5 in dados):
        return 30

    if (2 in dados and 3 in dados and 4 in dados and 5 in dados and 6 in dados):
        return 30

    return 0

# Ex 8 

def calcula_pontos_full_house(dados):
    contagem = {}

    for dado in dados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1

    tem_tres = False
    tem_dois = False

    for valor in contagem.values():
        if valor == 3:
            tem_tres = True
        if valor == 2:
            tem_dois = True

    if tem_tres and tem_dois:
        soma = 0
        for dado in dados:
            soma += dado
        return soma

    return 0

# Ex 9
def calcula_pontos_quadra(dados):
    contagem = {}

    for dado in dados:
        if dado in contagem:
            contagem[dado] += 1
        else:
            contagem[dado] = 1

    for valor in contagem.values():
        if valor >= 4:
            soma = 0
            for dado in dados:
                soma += dado
            return soma

    return 0

# Ex 10

def calcula_pontos_quina(dados):
    contagens = [0] * 7

    for dado in dados:
        contagens[dado] += 1

    for quantidade in contagens:
        if quantidade >= 5:
            return 50

    return 0

# Ex 11

def calcula_pontos_regra_avancada(dados):
    resultado = {}

    resultado['cinco_iguais'] = calcula_pontos_quina(dados)
    resultado['full_house'] = calcula_pontos_full_house(dados)
    resultado['quadra'] = calcula_pontos_quadra(dados)
    resultado['sem_combinacao'] = calcula_pontos_soma(dados)
    resultado['sequencia_alta'] = calcula_pontos_sequencia_alta(dados)
    resultado['sequencia_baixa'] = calcula_pontos_sequencia_baixa(dados)

    return resultado

# Ex 12

def faz_jogada(dados, categoria, cartela_de_pontos):
    if categoria in ["1", "2", "3", "4", "5", "6"]:
        categoria_num = int(categoria)
        pontos_simples = calcula_pontos_regra_simples(dados)
        cartela_de_pontos['regra_simples'][categoria_num] = pontos_simples[categoria_num]
    else:
        pontos_avancados = calcula_pontos_regra_avancada(dados)
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancados[categoria]

    return cartela_de_pontos