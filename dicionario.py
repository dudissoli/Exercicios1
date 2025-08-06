produto = {
    'nome':'Xbox Series S',
    'preco':2399,
    'estoque': 7
}
print(f'{produto['nome']} - Preço: {produto["preco"]}')

print(produto.keys())
print(produto.values())

produto.update({'estoque': 5})
print(produto)
produto.update({'desconto': 0.12})
print(produto)

preco_a_vista = produto.get('preco') * (1 - produto.get('desconto'))
print(preco_a_vista)
