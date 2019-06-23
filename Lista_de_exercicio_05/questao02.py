'''
Crie uma agenda telefônica com os seguintes telefones:

Maria – 99887766
Pedro – 92345678
Joaquim – 99887711

Apresente ao usuário os nomes e telefones que já estão disponíveis na agenda e
pergunte se o usuário deseja:

a) Adicionar novo contato
b) Remover contato existente

'''


agenda_telefonica_list = [('Maria', '99887766'), ('Pedro', '92345678'), ('Joaquim', '99887711')]

print(type(agenda_telefonica_list))

agenda_telefonica_dict = dict(agenda_telefonica_list)

print(type(agenda_telefonica_dict))

print("Contatos: ", agenda_telefonica_dict)

decisao = int(input("Deseja adicionar novo contato? 1 - sim e 0 - não "))

if decisao == 1:
    name = input("Digite o nome: ")
    phoneNumber = input("Digite o número do telefone: ")
    agenda_telefonica_list.append((name, phoneNumber))
    agenda_telefonica_dict = dict(agenda_telefonica_list)


print("Contatos: ", agenda_telefonica_dict)


decisao = int(input("Deseja remover contato existente? 1 - sim e 0 - não "))


if decisao == 1:
    name = input("Digite o nome: ")
    agenda_telefonica_dict.pop(name)


print("Contatos: ", agenda_telefonica_dict)
