'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
Ex.: 5!=5.4.3.2.1=120. 
'''

print("#####   Fatorial de um número  #####")
num = int(input("Digite o número que deseja saber o fatorial: "))

def fatorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * fatorial(n - 1) 


print(num, "!: ", fatorial(num))
