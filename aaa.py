produtos = {}

for i in range(5):
    nome = input('digite o nome do produto:')
    valor = float(input('digite o valor do produto:'))

    produtos[nome] = valor


def calcular_total(produtos):
    return sum(produtos.values())

def produto_mais_caro(produtos):
    nome = max(produtos, key=produtos.get)
    preco = produtos[nome]
    return nome, preco

def produto_mais_barato(produtos):
    nome = min(produtos, key=produtos.get)
    preco = produtos[nome]
    return nome, preco

def media_precos(produtos):
    return sum(produtos.values()) / len(produtos)


print('Relatório final')

print(produtos)


# BUSCA
nome_busca = input('Digite o nome do produto para buscar: ')
print(produtos.get(nome_busca, 'Produto não encontrado'))


# REMOVER
nome_remover = input('Digite um produto para remover (ou ENTER para pular): ')

if nome_remover != '':
    if nome_remover in produtos:
        del produtos[nome_remover]
        print('Produto removido com sucesso!')
    else:
        print('Produto não encontrado')


total = calcular_total(produtos)
mais_caro = produto_mais_caro(produtos)
mais_barato = produto_mais_barato(produtos)
media = media_precos(produtos)

print('Total:', total)
print('Mais caro:', mais_caro)
print('Mais barato:', mais_barato)
print('Média:', media)
