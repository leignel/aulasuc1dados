# ============================================================
# Aula 2 - Demonstração 2: if e else
# ============================================================
# if  = "se"     -> executa o bloco quando a condição é True
# else = "senão" -> executa quando a condição é False
#
# Regras do Python:
#   1. A linha do if/else termina com DOIS-PONTOS  :
#   2. O bloco de dentro fica RECUADO (4 espaços ou Tab)
#   3. O recuo (indentação) é que diz o que está "dentro" do if
# ============================================================

idade = int(input("Qual a sua idade? "))

if idade >= 18:
    print("Você é maior de idade.")
    print("Pode tirar a carteira de motorista.")
else:
    print("Você é menor de idade.")
    faltam = 18 - idade
    print(f"Faltam {faltam} ano(s) para completar 18.")

# Esta linha está FORA do if/else (sem recuo): roda sempre.
print("Fim do programa.")

# Experimente: tire o recuo de uma das linhas de dentro do if
# e rode de novo. O que acontece?  (IndentationError)
