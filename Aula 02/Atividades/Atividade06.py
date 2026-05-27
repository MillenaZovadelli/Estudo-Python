'''
Escreva um programa que calcule o tempo de viagem de carro. pergunte a distância a percorrer e a velocidade média para a viagem.
'''

distancia = float(input("Digite a distancia que irá percorrer (em km): "))
velocidade = float(input("Digite a velocidade media (em km): "))

tempo = distancia / velocidade

print(f"O tempo estimado de viagem é:", tempo,"horas.")