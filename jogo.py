import random


numero_secreto = random.randint(0, 100)
tentativas = 0

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 0 e 100.")

while True:
    tentativa = int(input("Digite sua tentativa: "))
    tentativas += 1

if tentativa < numero_secreto:
        print("O número secreto é maior. Tente novamente.")
elif tentativa > numero_secreto:
    print("O número secreto é menor. Tente novamente.")
else:
    print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")



