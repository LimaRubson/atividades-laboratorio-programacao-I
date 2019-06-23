'''
    Faça um Programa que realiza as operações básicas de uma calculadora (adição,
subtração, multiplicação e divisão) de dois números. Estas operações deverão ser
desenvolvidas através de funções. Peça ao usuário 2 números e apresente os
resultados das operações.

a) Adição
b) Subtração
c) Multiplicação
d) Divisão

'''


def adicao(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    return num1 / num2


num01 = float(input("Digite o 1º valor: "))
num02 = float(input("Digite o 2º valor: "))


print("Valor da adição dos valores informados: ", adicao(num01, num02))
print("Valor da subtração dos valores informados: ", subtracao(num01, num02))
print("Valor da multiplicação dos valores informados: ", multiplicacao(num01, num02))
print("Valor da divisão dos valores informados: ", divisao(num01, num02))

