"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preso = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preso)
print(variavel)
print('O hexadecimal de %d é %08x' % (1500, 1500))