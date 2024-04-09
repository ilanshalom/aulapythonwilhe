def binario_para_decimal(binario):
    decimal = 0
    tamanho = len(binario)
    for i in range(tamanho):
        bit = int(binario[tamanho - 1 - i])
        decimal += bit * (2 ** i)
    return decimal

def main():
    numero_binario = input("Digite um número binário: ")
    for digito in numero_binario:
        if digito != '0' and digito != '1':
            print("Entrada inválida. Por favor, digite apenas 0s e 1s.")
            return
    decimal = binario_para_decimal(numero_binario)
    print(f"O número binário {numero_binario} em decimal é: {decimal}")

if __name__ == "__main__":
    main()
