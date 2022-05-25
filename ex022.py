nome = str(input('Digite seu nome completo: ')).strip()
print('Nome em maiúsculo: {}'.format(nome.upper()))
print('Nome em minúsculo: {}'.format(nome.lower()))
print('Quantidade de letras no nome: {}'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split();
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0],len(separa[0])))