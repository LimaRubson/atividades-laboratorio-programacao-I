'''
Faça um programa que receba palavras digitadas pelo usuário e que:
a. Caso a palavra digitada pelo usuário tenha 2 ou menos caracteres, deverá ser
exibida a mensagem “String muito pequena” e o programa deverá ser
reiniciado;
b. Caso a palavra digitada pelo usuário seja diferente da palavra “sair”, deverá
aparecer o aviso “Tente digitar “sair” ”;
c. Por fim, caso a palavra digitada seja “sair”, deverá aparecer a mensagem “Fim!”
e o programa deverá ser encerrado
'''

print("#####   Palavras digitadas  #####")
string = input("Digite uma palavra: ")

tamanho = len(string)

while tamanho <= 2:
    print("String muito pequena")
    string = input("Digite uma palavra: ")

    if "sair" == string:
        print("Fim!")
        break
    else:
        print("Tente digitar \"sair\"")
        tamanho = len(string)
