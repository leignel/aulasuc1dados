# ============================================================
# Aula 2 - Demonstração 4: operadores lógicos e tabela verdade
# ============================================================
#   and (E)   -> True só se AS DUAS condições forem True
#   or  (OU)  -> True se PELO MENOS UMA condição for True
#   not (NÃO) -> inverte: True vira False e vice-versa
# ============================================================

# --- Tabela verdade impressa pelo próprio Python ------------
print("A      B      | A and B | A or B")
print(f"True   True   | {True and True}    | {True or True}")
print(f"True   False  | {True and False}   | {True or False}")
print(f"False  True   | {False and True}   | {False or True}")
print(f"False  False  | {False and False}   | {False or False}")

print(f"\nnot True  = {not True}")
print(f"not False = {not False}")

# --- AND: as duas coisas precisam ser verdade ---------------
idade = 25
tem_cnh = True
if idade >= 18 and tem_cnh:
    print("\nPode dirigir.")

# --- OR: basta uma ser verdade ------------------------------
dia = "sábado"
if dia == "sábado" or dia == "domingo":
    print("Fim de semana!")

# --- NOT: inverte -------------------------------------------
chovendo = False
if not chovendo:
    print("Dá para ir à praia.")

# --- Faixa de valores (entre 5 e 7) -------------------------
media = 6.0
if media >= 5 and media <= 7:
    print("Média entre 5 e 7.")
# Em Python também pode ser escrito assim:
if 5 <= media <= 7:
    print("Mesma coisa, escrita mais curta.")
