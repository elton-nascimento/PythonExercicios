# **-potencia
# //-divisão inteira
# %-modulo ou resto da divisão

# ORDEM DE PRECEDÊNCIA
# 1 - ()
# 2 - **
# 3 - * / // %
# 4 - + -

n1 = int(input('Digite um número:'))
n2 = int(input('Digte um número: '))
som = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
divInt = n1 // n2
exp = n1 ** n2
print('A soma é {}. A subtração é {}. A multiplicação é {}'.format(som,sub,mul))
print('A divisão e {}. A divisão inteira é {:.2f}. A exponenciação é {}'. format(div, divInt, exp))