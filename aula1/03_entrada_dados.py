# ============================================================
# Aula 1 - Demonstração 3: lendo dados do usuário com input()
# ============================================================
# input() SEMPRE devolve texto (str). Para fazer contas,
# precisamos CONVERTER com int() ou float().
# ============================================================

nome = input("Qual é o seu nome? ")
print(f"Prazer, {nome}!")

# Sem conversão: "Concatena" textos em vez de somar
x = input("Digite um número: ")
y = input("Digite outro número: ")
print(f"Sem converter, x + y = {x + y}   <- juntou os textos!")

# Com conversão: agora soma de verdade
x = float(x)
y = float(y)
print(f"Convertendo para float, x + y = {x + y}")

# Forma mais comum: converter já na leitura
ano_nascimento = int(input("Em que ano você nasceu? "))
idade_aproximada = 2026 - ano_nascimento
print(f"Você tem (ou fará) {idade_aproximada} anos em 2026.")
