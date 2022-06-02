vel = float(input('Informe a velocidade do carro: '))
mult = 0
if vel > 80:
    mult = (vel-80)*7
    print('Ultrapassou o limite de velocidade. Multa de R${:.2f}'.format(mult))
print('Boa viagem!')
