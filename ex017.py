import math
adjacente = float(input('Digite o cateto adjacente: '))
oposto= float(input('Digte o cateto oposto: '))
hipotenusa = math.hypot(adjacente,oposto)
print('O valor da hipotenusa é igual a {}'.format(hipotenusa))