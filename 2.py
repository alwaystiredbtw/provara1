# leia idade e tempo de trabalho e diga se o trabalhador pode se aposentar

idade = int(input("Qual sua idade? "))
tempoT = int(input("Quantos anos de trabalho voce tem?"))

aposentar = bool

if idade >= 65 or tempoT >= 30:
    aposentar = True
elif idade >= 60 and tempoT >= 25:
    aposentar = True

if aposentar == True:
    print("Parabens! Voce pode se aposentar !!")
else:
    print("Voce nao pode se aposentar !! trabalhe !!!!!!!!!!!!!!")