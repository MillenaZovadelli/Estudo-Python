'''
Faça um programa que solicite o preço de uma mercadoria eo percentual de desconto. Exiba o valor do desconto e o preço a pagar.
'''

preco = float(input("Insira o preço da mercadoria: "))
desconto_porcentual = float(input("Insira o desconto: "))

desconto = preco * (desconto_porcentual / 100)

preco_final = preco - desconto

print(f"Valor do Desconto: ", desconto)
print(f"Preço a pagar: ", preco_final)

