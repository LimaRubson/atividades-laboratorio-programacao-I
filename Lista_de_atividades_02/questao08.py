'''
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.
'''

intervalo025 = 0
intervalo2650 = 0
intervalo5175 = 0
intervalo76100 = 0

print("#####   Intervalos de números positivos  #####")
num = int(input("Digite um número: "))
lista = []

while num >= 0:
    lista.append(num)
    num = int(input("Digite um número: "))

for x in range(len(lista)):
    if 0 <= lista[x] <= 25:
        intervalo025 += 1
    elif 26 <= lista[x] <= 50:
        intervalo2650 += 1
    elif 51 <= lista[x] <= 75:
        intervalo5175 += 1
    elif 76 <= lista[x] <= 100:
        intervalo76100 += 1
        
print("\nNúmeros digitados: ", lista)
print("\nIntervalo [0-25]: ", intervalo025)
print("Intervalo [26-50]: ", intervalo2650)
print("Intervalo [51-75]: ", intervalo5175)
print("Intervalo [76-100]: ", intervalo76100)
