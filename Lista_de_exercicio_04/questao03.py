'''
Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando for informado
um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados,
faça:

    a. Mostre a quantidade de valores que foram lidos;
    b. Exiba todos os valores na ordem em que foram informados, um ao lado
    do outro;
    c. Exiba todos os valores na ordem inversa à que foram informados, um
    abaixo do outro;
    d. Calcule e mostre a soma dos valores;
    e. Calcule e mostre a média dos valores;
    f. Calcule e mostre a quantidade de valores acima da média calculada;
    g. Calcule e mostre a quantidade de valores abaixo de sete;
    h. Encerre o programa com uma mensagem; 

'''

arrayIndeterminateNumber = []
arryOrdemInversa = []
arrayAcimaDaMedia = []
arrayAbaixoDeSete = []
x = 0
soma = 0
media = 0
count = 0

while(x != -1):
    num = float(input("Digite um valor ou -1 para encerrar: "))

    if num != -1:
        count += 1
        arrayIndeterminateNumber.append(num)
        soma += num
    else:
        x = num

media = soma / count

for x in range(len(arrayIndeterminateNumber)):
    if arrayIndeterminateNumber[x] > media:
        arrayAcimaDaMedia.append(arrayIndeterminateNumber[x])
    elif arrayIndeterminateNumber[x] < 7:
        arrayAbaixoDeSete.append(arrayIndeterminateNumber[x])

y = count - 1
while y >= 0:
    arryOrdemInversa.append(arrayIndeterminateNumber[y])
    y -= 1


print("Quantidade de valores lidos: ", count)
print("Valores na ordem informada: ", arrayIndeterminateNumber)
print("Valores informados na ordem inversa: ")
for i in range(len(arryOrdemInversa)):
    print(arryOrdemInversa[i])

print("Soma dos valores: ", soma)
print("Média dos valores: ", media)
print("Quantidade de valores acima da média calculada: ", len(arrayAcimaDaMedia))
print("Quantidade de valores abaixo de sete: ", len(arrayAbaixoDeSete))
print("######### Obrigado/Obrigada e volte sempre! #########")
