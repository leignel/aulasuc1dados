# Enunciado:
#   Calcule e mostre o número de lâmpadas necessárias para
#   iluminar um cômodo.
#
#   Entrada: potência da lâmpada (watts), largura e comprimento
#            do cômodo (metros).
#   Considere: 3 watts por metro quadrado e um bocal (soquete)
#              para cada 3 m².
#
# Dicas:
#   - Não existe "meia lâmpada": arredonde PARA CIMA.
#     import math  ->  math.ceil(2.1) dá 3
#   - Use um if para avisar quando forem necessárias MAIS
#     lâmpadas do que o número de bocais do cômodo.
#
# Teste: lâmpada 60 W, cômodo 4 x 5 m
#   -> área 20 m², potência 60 W, 1 lâmpada, 7 bocais
#-----------------------------------------------------------------------
import math

potencia_lampada = float(input("Potência da lâmpada (W): "))
largura = float(input("Largura do cômodo (m): "))
comprimento = float(input("Comprimento do cômodo (m): "))

area = largura * comprimento
potencia_necessaria = area * 3 #3 W por m²
lampadas = math.ceil(potencia_necessaria / potencia_lampada)
bocais = math.ceil(area / 3) #1 bocal a cada 3m²

print(f"Área do cômodo: {area:.2f} m²")
print(f"Potência necessária: {potencia_necessaria:.0f} W")
print(f"Lâmpadas de {potencia_lampada:.0f} W necessárias: {lampadas}")
print(f"Bocais disponíveis no cômodo: {bocais}")

if lampadas > bocais:
    print("Atenção: faltam bocais! Use lâmpadas mais potentes.")
else:
    print("Os bocais são suficientes")
