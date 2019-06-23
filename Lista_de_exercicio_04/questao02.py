'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
multiplicação e os números.

'''

arrayNumbers = []
soma = 0
multiplicacao = 1

for x in range(5):
    num = int(input("Digite o primeiro número: "))
    arrayNumbers.append(num)
    soma += num
    multiplicacao *= num 


print("Soma: ", soma)
print("Multiplicação: ", multiplicacao)
print("Números digitados: ", arrayNumbers)
