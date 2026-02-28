# Declaração
nome_completo = "Jonatas Gomes"

nome_completo_aspas = """Jonatas
Gomes"""

nome_completo_quebra = "Jonatas \
Gomes"

nome = "Jonatas"
sobrenome = "Gomes"

# Formatação
print("Nome Completo (1a fomra):", nome_completo)
print("Nome Completo (2a fomra): " + nome_completo)
print("Nome Completo (3a fomra):" + "Jonatas" + " Gomes")
print("Nome Completo (4a fomra):" + "Jonatas", "Gomes")
print("Nome Completo (5a fomra):", nome_completo_aspas)
print("Nome Completo (6a fomra):", nome_completo_quebra)
print("Nome Completo (7a fomra): %s" % nome_completo)
print("Nome Completo (8a fomra): %s %s" % (nome, sobrenome))
print(f"Nome Completo (9a forma): {nome}")
      