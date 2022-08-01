def soma (x, y):
    return x + y

def subtracao (x, y):
    return x - y

def multiplicacao (x, y):
    return x * y

def divisao (x, y):
    return x / y

print("Selecionar uma operacao")
print("1.soma")
print("2.subtracao")
print("3.multiplicacao")
print("4.divisao")

escolha = str(input("Entre com a escolha (1/2/3/4): "))

num1 = int(input("Entre com o primeiro numero: "))
num2 = int(input("Entre com o segundo numero: "))

if escolha == '1':
    print('Soma: {0} + {1} = {2}'.format(num1,num2,soma(num1,num2)))

elif escolha == '2':
    print('Subtracao: {0} - {1} = {2}'.format(num1,num2,subtracao(num1,num2)))

elif escolha == '3':
    print('Multiplicacao: {0} * {1} = {2}'.format(num1,num2,multiplicacao(num1,num2)))

elif escolha == '4':
    print('Divisao: {0} / {1} = {2}'.format(num1,num2,divisao(num1,num2)))
else:
    print("Entrada invalida")
    