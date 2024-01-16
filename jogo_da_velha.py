import random

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True

    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2 - i] == jogador for i in range(3)]):
        return True

    return False

def verificar_empate(tabuleiro):
    return all(all(celula != ' ' for celula in linha) for linha in tabuleiro)

def obter_movimento_jogador():
    linha = int(input("Informe a linha (0, 1, 2): "))
    coluna = int(input("Informe a coluna (0, 1, 2): "))
    return linha, coluna

def obter_movimento_computador(tabuleiro):
    movimentos_disponiveis = [(i, j) for i in range(3) for j in range(3) if tabuleiro[i][j] == ' ']

    melhor_movimento = None
    melhor_pontuacao = float('-inf')

    for movimento in movimentos_disponiveis:
        i, j = movimento
        tabuleiro[i][j] = 'O'
        pontuacao = minimax(tabuleiro, 0, False)
        tabuleiro[i][j] = ' '

        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao
            melhor_movimento = movimento

    return melhor_movimento

def minimax(tabuleiro, profundidade, maximizando):
    if verificar_vitoria(tabuleiro, 'O'):
        return 1

    if verificar_vitoria(tabuleiro, 'X'):
        return -1

    if verificar_empate(tabuleiro):
        return 0

    if maximizando:
        melhor_pontuacao = float('-inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = 'O'
                    pontuacao = minimax(tabuleiro, profundidade + 1, False)
                    tabuleiro[i][j] = ' '
                    melhor_pontuacao = max(melhor_pontuacao, pontuacao)
        return melhor_pontuacao
    else:
        melhor_pontuacao = float('inf')
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] == ' ':
                    tabuleiro[i][j] = 'X'
                    pontuacao = minimax(tabuleiro, profundidade + 1, True)
                    tabuleiro[i][j] = ' '
                    melhor_pontuacao = min(melhor_pontuacao, pontuacao)
        return melhor_pontuacao

def jogar_jogo():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador = 'X'

    while True:
        exibir_tabuleiro(tabuleiro)

        if jogador == 'X':
            linha, coluna = obter_movimento_jogador()
            if tabuleiro[linha][coluna] == ' ':
                tabuleiro[linha][coluna] = 'X'
            else:
                print("Essa posição já está ocupada.")
                continue
        else:
            print("Vez do computador:")
            linha, coluna = obter_movimento_computador(tabuleiro)
            tabuleiro[linha][coluna] = 'O'

        if verificar_vitoria(tabuleiro, jogador):
            exibir_tabuleiro(tabuleiro)
            print(f" Jogador {jogador} venceu!")
            break
        elif verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo empatou!")
            break

        jogador = 'O' if jogador == 'X' else 'X'

if __name__ == "__main__":
    jogar_jogo()
