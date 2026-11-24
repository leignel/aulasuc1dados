# ============================================================
# Aula 2 - PRÁTICA ASSISTIDA (fazer junto com a turma)
# ============================================================
# Programas do dia a dia usando decisões, comparação e
# operadores lógicos. Construa linha a linha com os estudantes.
# ============================================================

# --- 1. Ingresso de cinema: meia-entrada --------------------
# Paga meia quem tem menos de 18 anos OU é estudante
# OU tem 60 anos ou mais.
print("=== CINEMA ===")
preco_inteira = 40.00
idade = int(input("Idade: "))
estudante = input("É estudante? (s/n): ").lower() == "s"

if idade < 18 or idade >= 60 or estudante:
    print(f"Meia-entrada: R$ {preco_inteira / 2:.2f}")
else:
    print(f"Inteira: R$ {preco_inteira:.2f}")

# --- 2. Frete grátis ----------------------------------------
# Frete grátis se a compra for de R$ 200 ou mais E o CEP
# for do estado do RJ (começa com 2).
print("\n=== LOJA ONLINE ===")
valor_compra = float(input("Valor da compra (R$): "))
cep = input("CEP (só números): ")

if valor_compra >= 200 and cep[0] == "2":     # cep[0] = 1º caractere
    print("Parabéns! Frete grátis.")
else:
    print("Frete: R$ 25,00")

# --- 3. Calculadora da Aula 1, agora sem erro na divisão ----
print("\n=== DIVISÃO SEGURA ===")
dividendo = float(input("Dividendo: "))
divisor = float(input("Divisor: "))

if divisor != 0:
    print(f"Resultado: {dividendo / divisor:.2f}")
else:
    print("Não é possível dividir por zero!")
