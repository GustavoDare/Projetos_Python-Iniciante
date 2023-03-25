from random import randint

num_sorteado = randint(0, 100)
tentativa = 7

print("Tente adivinhar o número que eu estou pensando. Ele está entre 0 e 100, podendo ser estes dois.")
print("Dica: O número que eu estou pensando é um número inteiro.")

while True:
    numero = input("\nDigite um número: ")
    try:
        num = int(numero)
    except ValueError:
        print("Número inválido.")
    else:
        if num == num_sorteado:
            print("Parabéns, você acertou o número que eu estava pensando!")
            break
        else:
            tentativa = tentativa - 1

            if abs(num_sorteado - num) < 10:
                print("Seu palpite está bem perto.")
            elif abs(num_sorteado - num) < 20:
                print("Seu palpite está próximo.")
            else:
                print("Seu palpite está longe.")
    
            if num < num_sorteado:
                print("O número sorteado é maior que seu palpite.")
            elif num > num_sorteado:
                print("O número sorteado é menor que seu palpite.")

            if tentativa == 0:
                print(f"\nAcabaram todas as suas tentativas. O número que eu tinha pensado era {num_sorteado}.")
                break
            else:
                print(f"\nVocê tem mais {tentativa} tentativas.")
            