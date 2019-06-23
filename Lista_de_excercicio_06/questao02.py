'''
Portas lógicas são os componentes fundamentais de sistemas eletrônicos e são
derivadas da lógica de Boole. Existem vários tipos de portas (and, or, not, xor,
nand...). Crie funções em Python que representem as portas que compõem o
circuito abaixo:

'''


S1 = "Desligado"
S2 = "Desligado"


'''
Funções em Python que representam as portas que compõem o
circuito e Código que resolve o circuito para as entradas:
 I. A=0, B=1, C=0
 II. A=1, B=1, C=0
 III. A=1, B=0, C=1
'''


def s1(A, B, C):
    global S1
    if A == 1 or B == 1 or C == 1:
        S1 = "Ligado"
        return S1
    else:
        return S1


def s2(A, B, C):
    global S2
    if A == 1 or B == 1 or C == 1:
        if A == 0 and B == 1:
            S2 = "Ligado"
            return S2
        elif A == 0 and C == 1:
            S2 = "Ligado"
            return S2
        elif B == 1 and C == 1:
            S2 = "Ligado"
            return S2
        else:
            return S2
    else:
        return S2

portaA = int(input("Informe o valor da porta A: "))
portaB = int(input("Informe o valor da porta B: "))
portaC = int(input("Informe o valor da porta C: "))

print("Resultado S1: ", s1(portaA, portaB, portaC))
print("Resultado S2: ", s2(portaA, portaB, portaC))


'''
Resposta:

 I. S1 = Ligado e S2 = Ligado
 II. S1 = Ligado e S2 = Desligado
 III. S1 = Ligado e S2 = Desligado
'''
