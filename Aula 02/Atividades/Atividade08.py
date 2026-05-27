'''
Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''

km = float(input("Digite a quantidade de km percorrido: "))
dias = int(input("Digite a quantidade de dias de aluguel: "))

preco_total = (dias * 60) + (km * 0.15)

print(f"preço total a pagar é: R$", preco_total)