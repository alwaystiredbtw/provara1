# jogo da forca de 1 letra (pre definida)

print("Seja bem vindo ao jogo da forca de 1 letra !")

letra = "M" # de marina 
tentativa = ""
cont = 1

while True:
    tentativa = str(input("Tente uma letra: ")).upper().strip()
    if tentativa == letra:
        print(f"Parabens, voce acertou a letra {letra} !")
        break
    if cont == 5:
        print("Suas tentativas acabaram :( ")
        break
    cont += 1
