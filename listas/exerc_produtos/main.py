from dados_produtos import produtos 
import copy

print("PRODUTOS ORIGINAIS")
print(*produtos, sep = "\n")

print()

novos_produtos = copy.deepcopy(produtos)
novos_produtos = [
    {**produto, 'preco' : round(produto['preco'] * 1.1, 2)}
    for produto in novos_produtos
]
print("PREÇOS AUMENTADOS EM 10%")
print(*novos_produtos, sep = '\n')

print()

produtos_por_nome = copy.deepcopy(produtos)
produtos_por_nome = sorted(produtos_por_nome, key=lambda produtos_por_nome: produtos_por_nome['nome'], reverse=True)
print("ORGANIZADOS POR NOME")
print(*produtos_por_nome, sep = '\n')

print()

produtos_por_preco = copy.deepcopy(produtos)
produtos_por_preco = sorted(produtos, key=lambda produtos_por_preco: produtos_por_preco['preco'])
print("ORNIZADOS POR PREÇO")
print(*produtos_por_preco, sep = '\n')

