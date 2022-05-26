nome = str(input('Nome completo: ')).strip()
nome = nome.upper()
print('O nome tem SILVA? ')
print('SILVA' in nome)

print('O nome tem Silva? {}'.format('silva' in nome.lower()))