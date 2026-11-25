# contador = 1
# while contador <= 5:
#     print(f"Volta número {contador}")
#     contador = contador + 1

#-----------------------------------

nota = float(input("\nDigite uma nota de 0 a 10: "))
while nota < 0 or nota > 10:
    print("Nota inválida!")
    nota = float(input("\nDigite uma nota de 0 a 10: "))
print(f"Nota aceita: {nota}")