'''
    Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
    inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
    A saída deve ser conforme o exemplo abaixo:
    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50

'''

print("#####   Tabuada entre 1 a 10  #####")
num = int(input("Digite o número que deseja saber a tabuada: "))

print("Tabuada de ", num, ": ")
if num <= 10 and num >= 1:
    for x in range(10):
        valor = num * (x+1)
        print(num, " X ", (x+1), " = ", valor)
else:
    print("Número inválido!")

