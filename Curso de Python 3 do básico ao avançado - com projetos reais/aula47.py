palavraChve = "test"

valor = False

while True:
    letraDigitada = input('Digite um letra :')
    print (len(letraDigitada))
    if len(letraDigitada) == 1:
        for letra in palavraChve:
            if letraDigitada == letra:
                valor = True

    if valor == True:
        break