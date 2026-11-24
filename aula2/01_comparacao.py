# ============================================================
# Aula 2 - Estruturas de decisão (IF)
# Demonstração 1: operadores de comparação
# ============================================================
# Toda comparação é uma PERGUNTA que o Python responde com
# True (verdadeiro) ou False (falso) -> o tipo bool da Aula 1.
# ============================================================

idade = 20

print(idade > 18)    # maior que           -> True
print(idade < 18)    # menor que           -> False
print(idade >= 20)   # maior ou igual a    -> True
print(idade <= 17)   # menor ou igual a    -> False
print(idade == 20)   # igual a             -> True
print(idade != 20)   # diferente de        -> False

# --- ATENÇÃO: = é diferente de == ---------------------------
# =   guarda um valor (atribuição)
# ==  pergunta se dois valores são iguais (comparação)
nota = 7          # guardei 7 na variável nota
print(nota == 7)  # perguntei: nota é igual a 7? -> True

# --- O resultado de uma comparação pode ser guardado --------
maior_de_idade = idade >= 18
print(f"É maior de idade? {maior_de_idade}")
print(type(maior_de_idade))   # <class 'bool'>

# --- Comparando textos --------------------------------------
senha = "senac123"
print(senha == "senac123")    # True
print(senha == "SENAC123")    # False: maiúsculas contam!

# --- Cuidado: input() devolve texto -------------------------
# "10" > "9" compara como TEXTO (letra por letra) e dá False!
print("10" > "9")             # False  (texto)
print(10 > 9)                 # True   (número)
# Por isso: converta com int() ou float() antes de comparar.
