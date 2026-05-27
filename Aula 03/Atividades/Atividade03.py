'''
3) Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar: soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.
'''

num1 = float(input("Digite o n1: "))
num2 = float(input("Digite o n2: "))
operacao = input("Escolha uma operação(+, -, *, /): ")
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if operacao != 0:
       resultado = num1 / num2
    else:
        print("Erro: Divisão por zero!")
else: 
    print("Erro: Operação invalida!")

print("Resultado: ", resultado)
