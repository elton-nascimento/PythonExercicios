import random
import time

x = random.randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
num = int(input('Em que número pensei? '))
print('PROCESSANDO...')
time.sleep(3)
if num == x:
    print('ACERTOU! PARABÉNS')
else:
    print('ERROU! TENTE OUTRA VEZ.')
print(x)
