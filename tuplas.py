# Tupla: Coleção ordenada e imultaveis de elementos!
# Ordenada:  Ordem de elemntos
# Imultaveis: Não altera após criada

# tupla exemplo:

minha_tupla = (1, 2, 2, 3, 4)

print("minha_tupla:", minha_tupla)

print(minha_tupla[0])
print(minha_tupla[2])
print(minha_tupla[-1])

# metodo count
contagem = minha_tupla.count(2)
print(f"O elemento (2) aparece {contagem} vezes!")

# index
indice = minha_tupla.index(3)
print("O indice é:", indice)