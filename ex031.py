viagem = float(input('Digite a distância da viagem em KM: '))
if viagem > 200:
    passagem = viagem * 0.45
else:
    passagem = viagem * 0.50
print('Valor da passagem: R$ {:.2f}'.format(passagem))