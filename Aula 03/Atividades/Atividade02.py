'''
2) Escreva um programa que pergunte o salário do
funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
'''

salario = int(input("Digite o seu salario:"))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print(f"Aumento: R${aumento:.2f}")
print(f"Novo Salario: R$ {novo_salario:.2f}")