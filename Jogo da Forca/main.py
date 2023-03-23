from random import randint

# Lista com todos os arquivos/temas de palavras possíveis
temas = ['animais.txt', 'frutas.txt', 'paises.txt']

# Escolher arquivo com as palavras
resposta = input("Gostaria de escolher o tema do Jogo da Forca? (s/n) ")
if resposta == 's':
    print("Os temas são: ")
    print("[1] Animais \n[2] Frutas \n[3] Países")
    while True:
        tema = input("Escolha o tema digitando seu número: ")
        try:
            tema = int(tema)
        except ValueError:
            pass
        if tema == 1:
            arquivo = temas[0]
            break
        elif tema == 2:
            arquivo = temas[1]
            break
        elif tema == 3:
            arquivo = temas[2]
            break
        else:
            print("Tema não identificado.")
else:
    arquivo = temas[randint(0, len(temas)-1)]

# Abrir arquivo com as palavras
try:
    with open(arquivo, 'r', encoding='utf8') as arq:
        linhas_arquivo = arq.readlines()
        nomes = linhas_arquivo
except FileNotFoundError:
    print("Essa opção não se encontra mais disponível")
    
# Escolher a palavra que será utilizada
palavra = nomes[randint(0, len(nomes))].lower()
tamanho_palavra = len(palavra) - 1

# Criar uma lista da palavra sem acentos
palavra_sem_acento = []
for letra in palavra:
    if letra == 'á' or letra == 'à' or letra == 'â' or letra == 'ã':
        palavra_sem_acento.append('a')
    elif letra == 'é' or letra == 'è' or letra == 'ê':
        palavra_sem_acento.append('e')
    elif letra == 'í' or letra == 'ì' or letra == 'î':
        palavra_sem_acento.append('i')
    elif letra == 'ó' or letra == 'ò' or letra == 'ô' or letra == 'õ':
        palavra_sem_acento.append('o')
    elif letra == 'ú' or letra == 'ù' or letra == 'û':
        palavra_sem_acento.append('u')
    else:
        palavra_sem_acento.append(letra)

# Criar uma lista do tamanho da palavra escolhida preenchida de underscores
adivinhar_palavra = []
for vezes in range(0, tamanho_palavra):
    if palavra[vezes] == ' ':
        adivinhar_palavra.append(' ')
    elif palavra[vezes] == '-':
        adivinhar_palavra.append('-')
    else:
        adivinhar_palavra.append('_')

# Começar a jogar
vida = 6
while True:
    for item in adivinhar_palavra:
        print(item, end='')

    letra = input("\nDigite uma letra: ")

    if letra in "abcdefghijklmnopqrstuvwxyz" and letra != '' and len(letra) == 1:
        letra = letra.lower()
        if letra in palavra_sem_acento:
            for vezes in range(0, tamanho_palavra):
                if letra == palavra_sem_acento[vezes]:
                    adivinhar_palavra[vezes] = palavra[vezes]
        else:
            vida = vida -1
            print(f"Esta letra não pertence a palavra escolhida.")
            if vida == 1:
                print("Resta apenas 1 vida.")
            elif vida == 0:
                pass
            else:
                print(f"Restam apenas {vida} vidas.")
    else:
        print("Isto não é uma letra")
    
    # Fim de jogo
    if vida == 0:
        print("GAME OVER")
        print(f"A palavra escolhida era {palavra}")
        break    
    if '_' not in adivinhar_palavra:
        print(palavra, end='')
        print("Parabéns, você ganhou!!")
        break
