from random import randint

opcoes = ['pedra', 'papel', 'tesoura']

# Pontuar o vencedor
def regras(jogador, computador, pontos):
    if jogador == 'pedra' and computador == 'papel' or jogador == 'papel' and computador == 'tesoura' or jogador == 'tesoura' and computador == 'pedra':
        print("Você perdeu.")
        pontos['computador'] = pontos['computador'] + 1
        return pontos
    elif computador == 'pedra' and jogador == 'papel' or computador == 'papel' and jogador == 'tesoura' or computador == 'tesoura' and jogador == 'pedra':
        print("Você ganhou.")
        pontos['jogador'] = pontos['jogador'] + 1
        return pontos
    else:
        print("Empate.")

# Converte a escolha do jogador
def escolha(numero):
    if numero == '1':
        return 'pedra'
    elif numero == '2':
        return 'papel'
    elif numero == '3':
        return 'tesoura'

# Escolha do estilo de jogo
def estilo_jogo():
    while True:
        print("Você prefere: \n[1] Melhor de três \n[2] Jogar até você perder")
        jogo = input()
        if jogo in '12' and jogo != '' and len(jogo) == 1:
            if jogo == '1':
                melhor_3()
                break
            elif jogo == '2':
                ate_perder()
                break
        else:
            print("Opção inválida, digite 1 ou 2.")

# Estilos de jogos      
def melhor_3():
    pontos = {'jogador': 0, 'computador': 0}
    while True:
        escolha_pc = opcoes[randint(0,2)]
        print("Escolha qual você deseja jogar: \n[1] Pedra \n[2] Papel \n[3] Tesoura")
        escolha_jogador = input("------------------\n")

        if escolha_jogador in '123' and escolha_jogador != '' and len(escolha_jogador) == 1:
            escolha_jog = escolha(escolha_jogador)
            print(f"Você: {escolha_jog.title()} x {escolha_pc.title()} :Computador")
            regras(escolha_jog, escolha_pc, pontos)
            print(pontos)
        else:
            print("Opção inválida, digite 1, 2 ou 3.")

        if pontos['jogador'] == 2:
            print("Parabéns, você ganhou.")
            break
        elif pontos['computador'] == 2:
            print("Tente novamente. Eu ganhei desta vez.")
            break

def ate_perder():
    pontos = {'jogador': 0, 'computador': 0}
    while True:
        escolha_pc = opcoes[randint(0,2)]
        print("Escolha qual você deseja jogar: \n[1] Pedra \n[2] Papel \n[3] Tesoura")
        escolha_jogador = input("------------------\n")

        if escolha_jogador in '123' and escolha_jogador != '' and len(escolha_jogador) == 1:
            escolha_jog = escolha(escolha_jogador)
            print(f"Você: {escolha_jog.title()} x {escolha_pc.title()} :Computador")
            regras(escolha_jog, escolha_pc, pontos)
        else:
            print("Opção inválida, digite 1, 2 ou 3.")
        
        if pontos['computador'] != 0:
            print(f"Fim de jogo. Você conseguiu ganhar {pontos['jogador']} vezes, antes de perder para mim.")
            break

# Execução
print("Vamos jogar pedra, papel, tesoura?")
estilo_jogo()
