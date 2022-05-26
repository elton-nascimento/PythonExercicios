n = str(input('Digite o nome completo: ')).strip()
nome = n.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Ùltimo sobrenome: {}'.format(nome[len(nome)-1]))