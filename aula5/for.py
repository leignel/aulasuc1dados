#------- variações do range() ------------
# print("\nrange(5): ", end="")
# for i in range(5):
#     print(i, end=" ")

# print("\nrange(1, 6): ", end="")
# for i in range(1, 6):
#     print(i, end=" ")

# print("\nrange(0, 11, 2): ", end="")
# for i in range(0, 11, 2):
#     print(i, end=" ")

# print("\nrange(10, 0 -1): ", end="")
# for i in range(10, 0, -1):
#     print(i, end=" ")
# print()



#------------------ CONTADOR E ACUMULADOR --------------

#contador: conta QUANTAS vezes algo aconteceu -> contador = contador + 1
# acumulador: SOMA valores ao longo das repetições -> soma = soma + valor

soma = 0     #acumulador começa em zero FORA do for
pares = 0    # contador começa em zero, FORA do for

for numero in range(1, 11):
    soma = soma + numero
    if numero % 2 == 0:
        pares = pares + 1
print(f"\nSoma de 1 a 10: {soma}")
print(f"Quantidade de pares: {pares}")
