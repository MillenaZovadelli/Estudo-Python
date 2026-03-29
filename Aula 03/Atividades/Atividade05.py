'''
5) Escreva um programa que calcule o preço a pagar pelo
fornecimento de energia elétrica. Pergunte a quantidade
de kWh consumida e o tipo de instalação: R para
residências, I para indústrias e C para comércios. Calcule o
preço a pagar, de acordo com a tabela a seguir.

  Preço por tipo e faixa de consumo
Tipo Faixa      (kWh)          Preço
Residencial   Até 500         R$ 0,40
Residencial   Acima de 500    R$ 0,65

Comercial     Até 1000        R$ 0,55
Comercial     Acima de 1000   R$ 0,60

Industrial    Até 5000        R$ 0,55
Industrial    Acima de 5000   R$ 0,60
'''

kwn = float(input("Digite a quantidade de kWh consumida: "))
tipo = input("Digite o tipo de instalação(R = Residencial, C = Comercial, I = Industrial): ")

if tipo == "R":
    if kwn <= 500:
        preco = kwn * 0.40
    else:
        preco = kwn * 0.65
elif tipo == "C":
    if kwn <= 1000:
        preco = kwn * 0.55
    else:
        preco = kwn * 0.60
elif tipo == "I":
    if kwn <= 5000:
        preco = kwn * 0.55
    else:
        preco = kwn * 0.60

else: 
    ("Tipo de instalação errada!")
    preco = None

if preco is not None:
  print(f"O valor a pagar é: {preco:.2f}")