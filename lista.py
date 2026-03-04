#  Lista é uma conleção de elementos ordenaveis e multaveis.
# Declaração
minha_lista = [1, 2, 3, 4, 5, "rocketseta", True, False]
minha_lista2 = [1, 7, 3, 6, 5, 4, 2]


# Exibir a lista
print("Minha lista de exemplo:", minha_lista)

# Exibirdo a lista
minha_lista[0] = "python"
print("Minha lista de exemplo:", minha_lista)
print("minha_lista[0] =", minha_lista[0])
print("minha_lista[5] =", minha_lista[5])
print("minha_lista[2:7] =", minha_lista[2:7])
print("minha_lista[:6] =", minha_lista[:6])
print("minha_lista[2:] =", minha_lista[2:])

# Métodos de lista

# append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append(6):",minha_lista)

# index(): Retorna o indice do elemento
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# insert(): Insere um elemento em um indice especifico
minha_lista.insert(2, 10)
print("Apos o insert(2, 10):", minha_lista)

# pop(): remove e retorna um elemento
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após pop(3)", minha_lista)

# remove(): remove o primeiro elemento com valor especificado
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

#sort(): Organizar a lista
minha_lista2.sort()
print("Após sort():", minha_lista2)
