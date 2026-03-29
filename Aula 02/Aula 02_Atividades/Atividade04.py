# Faça um programa que calcule o aumento de um salário. ele deve solicitar o valor do salario e a porcentagem do aumento. exiba o valor do aumento e do novo salario.

salario = float(input("Digite o seu salario: "))
porcentagem = float(input("Digite a porcentagem do aumento: "))

aumento = salario * (porcentagem / 100)

novo_salario = salario + aumento

print(f"Valor do aumento: {aumento}")
print(f"Novo Salario: {novo_salario}")