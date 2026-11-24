# ============================================================
# Aula 2 - Demonstração 3: mais de dois caminhos com elif
# ============================================================
# elif = "senão, se". O Python testa as condições DE CIMA PARA
# BAIXO e executa SOMENTE o primeiro bloco verdadeiro.
# ============================================================

# --- Exemplo 1: semáforo ------------------------------------
cor = input("Cor do semáforo (verde, amarelo, vermelho): ").lower()
# .lower() deixa o texto em minúsculas: "Verde" vira "verde"

if cor == "verde":
    print("Siga.")
elif cor == "amarelo":
    print("Atenção, reduza.")
elif cor == "vermelho":
    print("Pare!")
else:
    print("Cor inválida.")

# --- Exemplo 2: faixa etária --------------------------------
idade = int(input("\nIdade: "))

if idade < 12:
    print("Criança")
elif idade < 18:          # aqui já sabemos que idade >= 12
    print("Adolescente")
elif idade < 60:          # aqui já sabemos que idade >= 18
    print("Adulto")
else:
    print("Idoso")

# A ORDEM importa! Se o teste "idade < 60" viesse primeiro,
# uma criança de 8 anos seria classificada como adulto.
