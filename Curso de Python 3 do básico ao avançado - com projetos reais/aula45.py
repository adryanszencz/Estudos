
texto = 'Luiz'
iteratador =  iter(texto)
print(iteratador)

while True:
    try:
        print(next(iteratador))
    except StopIteration:
        break