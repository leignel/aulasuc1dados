# ============================================================
# Aula 1 - Demonstração 1: variáveis e tipos de dados
# ============================================================
# Variável = uma "caixa" com nome onde guardamos um valor.
# Em Python, o sinal = significa ATRIBUIÇÃO (guardar), não igualdade.
# ============================================================

# --- Os 4 tipos básicos -------------------------------------
nome = "Ana"            # str   -> texto (sempre entre aspas)
idade = 25              # int   -> número inteiro
altura = 1.68           # float -> número com casas decimais (use PONTO)
estudante = True        # bool  -> verdadeiro (True) ou falso (False)

print(nome)
print(idade)
print(altura)
print(estudante)

# --- Descobrindo o tipo com type() --------------------------
print(type(nome))       # <class 'str'>
print(type(idade))      # <class 'int'>
print(type(altura))     # <class 'float'>
print(type(estudante))  # <class 'bool'>

# --- Mostrando texto e variáveis juntos (f-string) ----------
print(f"{nome} tem {idade} anos e {altura} m de altura.")

# --- Variáveis podem mudar de valor -------------------------
idade = 26
print(f"Fez aniversário! Agora {nome} tem {idade} anos.")

# --- Boas práticas de nomes ---------------------------------
# ✔ use letras minúsculas e _ entre palavras (snake_case)
nota_final = 8.5
salario_mensal = 3200.00

# ✘ não pode: começar com número, ter espaço, usar acento é evitado
# 1nota = 7        -> erro
# nota final = 7   -> erro
# ✘ evite nomes sem significado: x, a1, coisa

# --- Python diferencia maiúsculas de minúsculas -------------
Nome = "Bruno"
print(nome)   # Ana
print(Nome)   # Bruno  (são variáveis DIFERENTES)
