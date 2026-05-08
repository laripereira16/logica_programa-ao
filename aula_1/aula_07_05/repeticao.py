import time
import random

print("### jogo da adivinhacao ###")
print()
print("Estou pensando em um numero...")

time.sleep(2)

numero = random.randint(0, 10)

print("Pensei!")
print("Voce podera tentar adivinhar ele")
print()
# * para i em um intervalo de 1 ate 4
#for i in range(1, 4):
    #     print("Parabens! Voce acertou!")
   # else:
    #
    #    print("Voce errou!")

acertou = False
num_tentativa = 0
# enquanto acertou for false...
while acertou == False:
    num_tentativa += 1 #mesma coisa que num_tentativa = num_tentativa + 1
    print(f"Tentativa numero {num_tentativa}")
    tentativa = int(input("Digite um valor entre 0 e 10: "))

    if tentativa == numero:
        print("Parabens! Voce acertou!")
        acertou = True
    else:
        print("Voce errou!")
        if num_tentativa == 10:
            print("voce e burro")
