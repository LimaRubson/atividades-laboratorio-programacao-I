'''
Um dos modelos mais importantes e básicos para redes neurais é o neurônio
Perceptron. Ele possui duas funções especiais: a função de campo local induzido
e a função de ativação. A função de campo local induzido recebe três parâmetros:
w (vetor de peso), x (vetor de entrada) e b (bias – inteiro) e calcula a função: Σ
(w*x + b). Já a função de ativação, recebe a saída da função de campo local induzido 
e o coloca na função sigmoide: 1/(1-ex), onde x corresponde a saída da função de campo 
local induzido.

Agora que você conhece as funções que formam o perceptron, crie um código em
Python, que realize a função de campo local induzido, a função de ativação e que
calcule o resultado do perceptron para um vetor de peso W, entrada X e bias B
fornecido pelo usuário.
'''

def campoLocalInduzido(w, x, b):
    e = (w*x + b)
    return e


def ativacao(w, x, b):
    return 1/(1-2.7**campoLocalInduzido(w, x, b))


w = float(input("Informe o vetor de peso: "))
x = float(input("Informe o vetor de entrada: "))
b = int(input("Informe o bias: "))


print("Resultado: ", ativacao(w, x, b))

