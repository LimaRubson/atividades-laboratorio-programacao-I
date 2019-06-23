'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes
foram lidas. Imprima as consoantes.
'''

arrayCaracters = []
arrayConsoantes = []
count = 0

def vogal(caracter):
    if caracter == "a":
        return True
    if caracter == "e":
        return True
    if caracter == "i":
        return True
    if caracter == "o":
        return True
    if caracter == "u":
        return True
    if caracter == "A":
        return True
    if caracter == "E":
        return True
    if caracter == "I":
        return True
    if caracter == "O":
        return True
    if caracter == "U":
        return True
    else:
        return not True


for x in range(10):
    caracter = input("Digite um caracter: ")
    arrayCaracters.append(caracter)


for x in range(len(arrayCaracters)):
    if not vogal(arrayCaracters[x]):
        count += 1
        arrayConsoantes.append(arrayCaracters[x])


print(arrayCaracters)
print(arrayConsoantes)
print(count)
