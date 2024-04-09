contador = 0
soma = 0
resp = "s"

while resp == "s" or resp =="s":
    num = float(input("digite um numero"))
    soma = soma + num 
    contador = contador +1 
    resp = input("deseja continuar s/n?")
    
    media = soma / contador 
    print("a media dos numeros digitados é %.2f" %media)