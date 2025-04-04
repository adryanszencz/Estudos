"""
# Como eu fiz

nome = 'Luiz Otavio'
tamanho  = len(nome)
nova_string = '*'

i = 0
while i <= tamanho:
    if i == 11:
        nova_string += nome[i]
        break
    nova_string += nome[i] + '*'
    i += 1
    print (i)
    print(nova_string)

"""
# Oq ele fez

nome = 'Luiz Otavio'

indice = 0
novo_nome = '*'

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'{letra}*'
    indice += 1
print (novo_nome)