'''
    Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))
num4 = float(input("Digite o 4º número: "))
num5 = float(input("Digite o 5º número: "))

soma = num1 + num2 + num3 + num4 + num5

media = (num1 + num2 + num3 + num4 + num5) / 5

print("Soma dos números: ", soma)
print("Média dos números: ", media)
