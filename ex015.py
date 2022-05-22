kmPercorrido = float(input('Informe os km percorridos: '))
diasAlugados = int(input('Informe a quantidade de dias alugados: '))
valorPagar = (diasAlugados * 60) + (kmPercorrido * 0.15)
print('O valor a pagar pelo aluguel do carro é igual a R$ {:.2f}'.format(valorPagar))