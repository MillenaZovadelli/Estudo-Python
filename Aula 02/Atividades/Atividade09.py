'''
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
'''

dias_fumando = int(input("Digite quantos cigarros fuma por dia: "))
anos_fumando = int(input("Digite a quantos anos você fuma: "))

total_cigarros = dias_fumando * 365 * anos_fumando
minutos_perdidos = total_cigarros * 10

dias_perdidos = minutos_perdidos // (60 * 24)

print("Dias de vida perdidos: ", dias_perdidos)