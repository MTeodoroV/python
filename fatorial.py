#def main():
    #n = int(input("Digite o valor que deseja fazer o seu fatorial: "))
    #fat = 1
    #i = 2
    #while i <= n:
        #fat = fat*i
        #i = i + 1

    #print("O valor de %d! eh =" %n, fat)
#main()

n = int(input("Digite o qual numero deseja fatoriar: "))
fat = 1

while n > 0:
    fat = fat * n
    n = n - 1
print(fat)