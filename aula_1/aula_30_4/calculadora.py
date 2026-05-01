print("---------------------")
print("      Calculadora    ")
print("---------------------")
print()
print("Essa e a nossa calculadora, ela pode fazer as seguintes operacoes")
print("a partir de dois numeros que voce informar")
print()

print("Digite o valor correspondente ao calculo")
print("que voce quer fazer")
print()
print("1 - As 4 operacoes")
print("2 - Media de 3 valores")
print("3 - Formula de Bhaskara")
print()
opcao = int(input("Digite a opcao: "))


match opcao:
     case 1:
  
        first_num = float(input("Digite o primeiro numero: "))
        second_num = float(input("Digite o segundo numero: "))
        print() 

        adicao = first_num + second_num
        print("A adicao resulta em: ", adicao)
          
        subtracao = first_num - second_num
        print("A subtracao resulta em: ", subtracao)

        multi = first_num * second_num
        print(f"A multiplicacao resulta em: {multi}")   
          
        # Verificando se o segundo numero e diferente de 0
        if second_num != 0:
            divisao = first_num / second_num
            print(f"A divisao resulta em: {divisao}")
        else:
            print("A divisao nao pode ser feita.")




     case 2:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        num3 = float(input("Digite o terceiro numero: "))
        media = (num1 + num2 + num3) / 3
        print(f"A media dos numeros resulta em: {media}")

     case 3:
          print("formula de bhaskara")
          

first_num = float(input("Digite o primeiro numero: "))
second_num = float(input("Digite o segundo numero: "))
print()
adicao = first_num + second_num
subtracao = first_num - second_num
mult = first_num * second_num
divisao = first_num / second_num

print()
print("A adicao resulta em: ", adicao) 
print("A subtracao resulta em: ", subtracao)
multi = first_num * second_num
print(f"A multiplicacao resulta em: {multi}")

# Verificando se o segundo numero e diferente de 0
if second_num != 0:
    divisao = first_num / second_num
    print(f"A divisao resulta em: {divisao}")
else:
     print("A divisao nao pode ser feita")

print() 