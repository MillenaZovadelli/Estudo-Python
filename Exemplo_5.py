nome = input("Digite o nome do aluno: ")
nota1 = float(input("informe a primeira nota: "))
nota2 = float(input("informe a segunda nota: "))
nota3 = float(input("informe a terceira nota: "))
nota4 = float(input("informe a quarta nota: "))

mediafinal = (nota1 + nota2 + nota3 + nota4) / 4

if mediafinal >=7.0:
    print("A media: %.2f - aprovado "% mediafinal)
else:
    print("A media: %.2f - reprovado "% mediafinal)