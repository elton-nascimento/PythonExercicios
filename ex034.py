salario = float(input('Digite o valor do salario R$ '))
if salario > 1250:
    novoSalario = salario + (salario*10/100)
else:
    novoSalario = salario + (salario*15/100)
print('O salario de R$ {:.2f} agora é no valor de R$ {:.2f}'.format(salario, novoSalario))