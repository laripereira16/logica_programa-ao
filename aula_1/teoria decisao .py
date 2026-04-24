nome =input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
print("Ola, ",nome,"! A sua idade e ",idade)

# A estrutura de decisao analisa uma comparacao e exrcuta o codigo 
# com base na resposta . Para utilizarmos a estrutura de decisao, precisamos 
# de compradores, que sao:

# - > maior 
# - < menor 
# - == igual
# - != diferente 
# - >= maior ou igual
# - <= menor ou igual 
# - ! nao  

if idade >= 18:
    print("Voce e maior de idde!")
    if idade >= 60:
        print("Voce e idoso!") 
        print("Ja pode pegar a carteirrinha de estacionamento")
else:
    print(" Voce e menor de idade!")
    print("Nao pode comprar cigarro no Reino Unido")