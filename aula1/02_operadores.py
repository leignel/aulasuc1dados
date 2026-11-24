# ============================================================
# Aula 1 - Demonstração 2: operadores matemáticos
# ============================================================

a = 17
b = 5

soma = a + b             # adição
subtracao = a - b        # subtração
multiplicacao = a * b    # multiplicação
divisao = a / b          # divisão (resultado sempre float)
divisao_inteira = a // b # divisão inteira (descarta a parte decimal)
resto = a % b            # módulo = RESTO da divisão
potencia = a ** 2        # potência (a elevado a 2)

print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {resto}")
print(f"{a} ** 2 = {potencia}")

# --- Ordem de precedência (igual à matemática) --------------
# 1º ( )   2º **   3º * / // %   4º + -
print(2 + 3 * 4)     # 14
print((2 + 3) * 4)   # 20

# --- Acumulando resultados em novas variáveis ---------------
preco = 49.90
quantidade = 3
subtotal = preco * quantidade
desconto = subtotal * 0.10
total = subtotal - desconto
print(f"Subtotal: R$ {subtotal:.2f}")   # :.2f = 2 casas decimais
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total:    R$ {total:.2f}")

# --- Para que serve o resto (%)? ----------------------------
# Saber se um número é par: o resto da divisão por 2 é 0
print(f"10 % 2 = {10 % 2}  -> 10 é par")
print(f"7 % 2 = {7 % 2}   -> 7 é ímpar")
