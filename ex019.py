import random

a1 = str(input('Digite o prmeiro aluno: '))
a2 = str(input('Digite o segudnod aluno: '))
a3 = str(input('Digite o terceiro aluno: '))
a4 = str(input('Digite o quarto aluno: '))
lista = [a1, a2, a3, a4]
esc = random.choice(lista)
print('O aluno escolhido foi {}.'.format(esc))