x=0
quantidade=0
valor=0
j=1
total=0

while(j==1):
    x=float(input("Digite o codigo:"))
    if x==100:
        print("O seu pedido foi Cachorro Quente")
        quantidade=float(input("Digite a quantidade de pedidos:"))
        valor = valor + quantidade * 1.20
        print (valor)

    if x==101:
        print("O seu pedido foi Bauru Simples")
        quantidade=float(input("Digite a quantidade de pedidos:"))
        valor = valor + quantidade * 1.30 
        print (valor)

    if x==102:
        print("O seu pedido foi Bauru com Ovo")
        quantidade=float(input("Digite a quantidade de pedidos:"))
        valor = valor + quantidade * 1.50
        print (valor)

    if x==103:
        print("O seu pedido foi Hamburguer")
        quantidade=float(input("Digite a quantidade de pedidos:"))
        valor = valor + quantidade * 1.20 
        print (valor)

    if x==104:
        print("O seu pedido foi Chesseburguer")
        quantidade=float(input("Digite a quantidade de pedidos:"))
        valor = valor + quantidade * 1.70 
        print (valor)

    if x==105:
        print("O seu pedido foi Suco")
        quantidade=float(input("Digite a quantidade de pedidos:"))
        valor = valor + quantidade * 2.20 
        print (valor)

    if x==106:
        print("O seu pedido foi Refrigerante")
        quantidade=float(input("Digite a quantidade de pedidos:"))
        valor = valor + quantidade * 1.00 
        print (valor)
    j=int(input("deseja continuar? Digite 1 se nao digite 0:  "))

print('Total a pagar e: R$:', valor)