import random
from funcoes import *

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

combinacoes_simples   = ['1', '2', '3', '4', '5', '6']
combinacoes_avancadas = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']
todas_combinacoes     = combinacoes_simples + combinacoes_avancadas

imprime_cartela(cartela)

rodada = 0
while rodada < 12:

    dados_rolados   = rolar_dados(5)
    dados_no_estoque = []
    rerrolagens     = 0

    print("Dados rolados:", dados_rolados)
    print("Dados guardados:", dados_no_estoque)
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    jogada_feita = False
    while not jogada_feita:

        opcao = input()

        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            idx = int(input())
            resultado = guardar_dado(dados_rolados, dados_no_estoque, idx)
            dados_rolados = resultado[0]
            dados_no_estoque = resultado[1]

        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            idx = int(input())
            resultado = remover_dado(dados_rolados, dados_no_estoque, idx)
            dados_rolados = resultado[0]
            dados_no_estoque = resultado[1]

        elif opcao == '3':
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(5 - len(dados_no_estoque))
                rerrolagens += 1

        elif opcao == '4':
            imprime_cartela(cartela)

        elif opcao == '0':
            print("Digite a combinação desejada:")
            categoria = input()

            combinacao_valida = False
            while not combinacao_valida:
                if categoria not in todas_combinacoes:
                    print("Combinação inválida. Tente novamente.")
                    categoria = input()
                elif categoria in combinacoes_simples and cartela['regra_simples'][int(categoria)] != -1:
                    print("Essa combinação já foi utilizada.")
                    categoria = input()
                elif categoria in combinacoes_avancadas and cartela['regra_avancada'][categoria] != -1:
                    print("Essa combinação já foi utilizada.")
                    categoria = input()
                else:
                    combinacao_valida = True

            dados = dados_rolados + dados_no_estoque
            cartela = faz_jogada(dados, categoria, cartela)

            jogada_feita = True
            rodada += 1
            continue

        else:
            print("Opção inválida. Tente novamente.")
            continue

        print("Dados rolados:", dados_rolados)
        print("Dados guardados:", dados_no_estoque)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

imprime_cartela(cartela)

pontuacao = 0
soma_simples = 0

for i in range(1, 7):
    if cartela['regra_simples'][i] != -1:
        pontuacao += cartela['regra_simples'][i]
        soma_simples += cartela['regra_simples'][i]

if soma_simples >= 63:
    pontuacao += 35

for chave in cartela['regra_avancada']:
    if cartela['regra_avancada'][chave] != -1:
        pontuacao += cartela['regra_avancada'][chave]

print("Pontuação total:", pontuacao)