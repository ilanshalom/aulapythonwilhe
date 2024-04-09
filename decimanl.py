numero_decimal = int(input("Digite um número decimal: "))

binario = ""
while numero_decimal > 0:
    resto = numero_decimal % 2
    binario = str(resto) + binario
    numero_decimal //= 2

print("O número decimal em binário é:", binario)
