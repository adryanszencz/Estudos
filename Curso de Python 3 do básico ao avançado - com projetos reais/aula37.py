contador = 0

while contador < 100 :
    contador += 1

    if contador == 6 :
        print ('Não vou mostra o 6.')
        continue

    if contador >= 10 and contador <= 27 :
        print (f'Não vou mostra o {contador}.')
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')