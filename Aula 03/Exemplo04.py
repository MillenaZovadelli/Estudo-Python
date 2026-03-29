'''
Exemplo 04: Calcular a conta de um telefone celular
de uma empresa chamada "Tchau", considerando os seguintes planos:
• Abaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto.
• Entre 200 e 400 minutos, o preço é de R$ 0,18.
• Acima de 400 minutos, o preço é de R$ 0,15
'''

minutos = int(input("Quantos minutos você utilizou neste mês: "))
if minutos < 200:
    preco = 0.20
else:
    if minutos < 400:
        preco = 0.18
    else:
        preco = 0.15

print(f"Você vai pagar este mês: R$ {minutos * preco:.2f}")