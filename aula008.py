import random
num = random.randint(1, 10)
n = int(input('Acerte o número entre 1 e 10: '))
if n == num:
    print('ACERTOU! {} = {}'.format(n, num))
while n != num:
    num = random.randint(1, 10)
    n = int(input('Acerte o núemro entre 1 e 10: '))
    if n == num:
        print('ACERTEOU! {} = {}'.format(n, num))
        break


