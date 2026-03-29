'''
1) Escreva um programa que pergunte a velocidade do
carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse
caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
'''

velocidade =  int(input("Digite a velocidade:"))
if velocidade > 80:
    multa = (velocidade - 80) * 5 
    print("Você foi multado!")
    print(f"Sua multa é R${multa}")
else:
    print("Você está dentro do limite da velocidade.")