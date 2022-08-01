caracteres =[]

r = 1
y = 1

while (1):
    caracteres.append(int(input("Possibilidades numero %d: " % r)))

    r = r + 1

    while(1):
        shazam = input('Deseja continuar? (S/n):')
        if(shazam == 'S' or shazam == 's' or shazam == ''):
            break
        if(shazam =='N' or shazam == 'n'):
            for x in caracteres:
                y = y * x
            print(y)
            exit()
        else:
            print('número não válido')
