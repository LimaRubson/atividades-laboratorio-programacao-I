'''
    O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a
menor e a maior temperaturas informadas, bem como a média das temperaturas.
'''

print("#####   Temperaturas  #####")
temp = int(input("Digite a temperatura ou \"000\" para sair: "))
listaTemp = []
soma_das_temperaturas = 0
quantidade_temperaturas = 0
media_temperaturas = 0

while temp != 000:
    listaTemp.append(temp)
    temp = int(input("Digite a temperatura ou \"000\" para sair: "))


for temperatura in listaTemp:
    soma_das_temperaturas += temperatura

quantidade_temperaturas = len(listaTemp)
media_temperaturas = soma_das_temperaturas / quantidade_temperaturas

print("Menor temperatura: ", min(listaTemp), "graus")
print("Maior temperatura: ", max(listaTemp), "graus")
print("Média das temperaturas: ", media_temperaturas, "graus")

