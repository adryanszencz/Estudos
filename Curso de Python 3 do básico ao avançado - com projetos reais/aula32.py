"""
Exercise 1

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'
    
if par_impar:
    par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Vocé não digitou um numero inteiro')
"""

"""
Exercise2

entrada = input('Digite a hora em numeros inteiros: ')

try :
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom Dia')

    elif hora >= 12 and hora <= 17:
        print('Boa Tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa Noite')

    else:
        print('Não conheço essa hora')

except:
    print('Por favor, digite apenas numeros inteiros')
"""

"""
#Exercise 3

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1:
    if tamanho_nome <= 4:
        print('Seu nome e curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome e normal')
    else:
        print('Seu nome e longo')

else:
    print('Digite mais de uma letra.')

"""