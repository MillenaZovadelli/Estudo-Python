# Escreva um programa que leia a quantidade de dias, horas e segundo do usuario. calcule o total em segundos.

dias = int(input("Digite a quantidade dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos 

print(f"O total em segundos do usuario é: ", total_segundos)