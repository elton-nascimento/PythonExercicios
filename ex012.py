preco = float(input('Digite o preço do produto R$ '))
desconto = preco*(5/100)
print('Valor do desconto de 5% R$ {:.2f}'.format(desconto))
novoPreco = preco-desconto
print('O produto com desconto de 5% é igual a R$ {:.2f}'.format(novoPreco))