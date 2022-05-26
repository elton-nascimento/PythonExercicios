frase = str(input('Digite uma frase: ')).upper()
print('Quantidade de vezes que aparece a letra A = {}'.format(frase.count('A')))
print('A primeira posição da letra A: {}'.format(frase.find('A')+1))
print('A última posição da letra A: {}'.format(frase.rfind('A')+1))