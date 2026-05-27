'''
4) Escreva um programa para aprovar o empréstimo
bancário para a compra de uma casa. O programa deve
perguntar o valor da casa a comprar, o salário e a
quantidade de anos a pagar. O valor da prestação mensal
não pode ser superior a 30% do salário. Calcule o valor da
prestação como sendo o valor da casa a comprar dividido
pelo número de meses a pagar.
'''
valor_casa = float(input("Qual é o valor da casa que quer comprar: R$"))
salario = float(input("Digite o seu salario: R$"))
anos = int(input("Digite em quantos anos deseja pagar: "))

meses = anos * 12
prestacao = valor_casa / meses

limite = salario * 0.30

if prestacao <= limite:
    print("Emprestimo aprovado!")
else:
    print("EMprestimo negado!")

