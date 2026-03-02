# Variaveis são imultaveis

nome = "Jonatas"
sobrenome = "Gomes"
nome_completo = "Jonatas Gomes"

# Em Maisuculas
print(nome.upper())

# Em Minusculas
print(nome_completo.lower())

# Acessar letras da Variavel
print(nome[0])

# Contar ocorrencias dentro da str
print(nome_completo.count("a"))

# Posição de uma letra
print(nome_completo.find("a"))

# Codificação - Conversão de str para bits
print(nome.encode())

# Decodificar o que esta em bits
print(nome.encode().decode())

# Substitui uma str por outra str
print(nome_completo.replace("a", "e"))

# Adicionar um separador por caracter em str
print(("-").join(nome_completo))
