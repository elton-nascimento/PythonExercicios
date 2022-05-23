import math
ang = float(input('Digite o ângulo: '))
senAng = math.sin(math.radians(ang))
cosAng = math.cos(math.radians(ang))
tanAng = math.tan(math.radians(ang))
print('O valor de seno do ângulo {}º é igual a {:.2f}'.format(ang, senAng))
print('O valor do cesseno do ângulo {}º é igual a {:.2f}'.format(ang, cosAng))
print('O valor da tangente do ângulo {}º é igual a {:.2f}'.format(ang, tanAng))