'''
Faça um programa que recebe o nome de dois arquivos e copia o conteúdo do
primeiro arquivo para o segundo arquivo. Considere que o conteúdo do arquivo
de origem é um texto. Sua função não deve copiar linhas comentadas (que
começam com //)

'''

nomePrimeiroAquivo = input("Digite o nome do primeiro arquivo: ")
nomeSegundoArquivo = input("Digite o nome do segundo arquivo: ")

primeiroArquivo = open('C:/Users/RubsonLima/' + nomePrimeiroAquivo, 'w')
primeiroTexto = """
Lista de Estudantes
---
//Rubson Hebrain de Lima Freire
Jaime de Souza Cavalcanti
Adriano José Pacheco Lima
"""
primeiroArquivo.write(primeiroTexto)
primeiroArquivo.close()

primeiroArquivo = open('C:/Users/RubsonLima/' + nomePrimeiroAquivo, 'r')
textTest = primeiroArquivo.read()
print("######## Primeiro texto ########")
print(textTest)
primeiroArquivo.close()


primeiroArquivo = open('C:/Users/RubsonLima/' + nomePrimeiroAquivo, 'r')
textTest = primeiroArquivo.readlines()
lines = textTest
primeiroArquivo.close()


segundoArquivo = open('C:/Users/RubsonLima/' + nomeSegundoArquivo, 'w')
relist = []
for line in lines:
    if line.find("//") != 0: # ignora as linhas que começam com //
        relist.append(line)

segundoTexto = relist
segundoArquivo.writelines(segundoTexto)
segundoArquivo.close()

segundoArquivo = open('C:/Users/RubsonLima/' + nomeSegundoArquivo, 'r')
textTest = segundoArquivo.read()
print("######## Segundo texto ########")
print(textTest)
segundoArquivo.close()
