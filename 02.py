menor = int(input("Entre com a menor numero da faixa de busca: "))
maior = int(input("Entre com a maior numero da faixa de busca: "))

print("Os números primos entre {0} e {1} sao: ".format(menor,maior))

for num in range (menor,maior + 1):
    if num > 1:
        for i in range (2,num):
            if(num % i) == 0:
                break
        else:
            print(num)

