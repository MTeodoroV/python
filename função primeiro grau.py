import matplotlib.pyplot as plt

def main():
    while(1):
        #Cria as variaveis da equação
        a = int(input('Insira o valor de "a" da função junto ao sinal: '))
        b = int(input('Insira o valor de "b" da função junto ao sinal: '))

        
    
        if (a == 0):
            print('A função não é de primeiro grau\n')
            main()
        else:
            #Printa a equação como se escreveria no papel + seu tipo + resposta
            if(a > 0):
                print('f(x)=' + str(a) + 'x' + str(b) + '\nA função é crescente')
            if(a < 0):
                print('f(x)=' + str(a) + 'x' + str(b) + '\nA função é decrescente')

            #contas
            z =int(-b/a)
            w =int(0)
            x.append(z)
            y.append(w)

            print('O intercepto de "x" é:' + str(z))
         


            z =int(0)
            w =int(b)
            x.append(z)
            y.append(w)

      
            print('O intercepto de "y" é:' + str(w))


        #continua loop
        while(1):
            shazam = input('Deseja continuar? (S/n):')
            if(shazam == 'S' or shazam == 's' or shazam == ''):
                break
            if(shazam =='N' or shazam == 'n'):
                print('Este é o gráfico que foi formado:')
                plt.plot(x, y)
                plt.ylabel('y')
                plt.xlabel('x')
                plt.show()
                exit()
            else:
                print('número não válido')
x=[]
y=[]
main()