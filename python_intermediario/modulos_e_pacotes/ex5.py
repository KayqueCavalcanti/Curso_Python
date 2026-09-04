import copy

# 1. Lista original de produtos (Corrigido o colchete que faltava)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# 2. Aumentar os preços dos produtos em 10% com deepcopy e list comprehension
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# 3. Ordenar os produtos por nome decrescente (do maior para menor)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

# 4. Ordene os produtos por preco crescente (do menor para maior)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

# --- EXIBIÇÃO FINAL DOS RESULTADOS ---

print('--- PRODUTOS ORIGINAIS ---')
print(*produtos, sep='\n')
print()

print('--- NOVOS PRODUTOS (PREÇO +10%) ---')
print(*novos_produtos, sep='\n')
print()

print('--- ORDENADOS POR NOME (DECRESCENTE) ---')
print(*produtos_ordenados_por_nome, sep='\n')
print()

print('--- ORDENADOS POR PREÇO (CRESCENTE) ---')
print(*produtos_ordenados_por_preco, sep='\n')