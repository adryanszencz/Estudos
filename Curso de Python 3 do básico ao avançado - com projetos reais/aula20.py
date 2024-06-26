primeiro_valor = input('Digit um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor} e maior que {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'{segundo_valor} e maior que {primeiro_valor}')
else:
    print(f'{primeiro_valor} sao iguais {segundo_valor}')
