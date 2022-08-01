print("Multiplicacao de matrizes:")

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range (0 ,3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]  '))
print('-=-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
            print(f'[{matriz[linha][coluna]:^5}]', end= '')
    print()

print("Agora digite a segunda matriz:")
matriz2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0 ,3):
    for c in range(0 ,3):
        matriz2[l][c]= int(input(f'Digite um valor para [{l},{c}]  '))
print('-=-' * 30)
for l in range(0 ,3):
    for c in range(0, 3):
            print(f'[{matriz2[l][c]:^5}]', end= '')
    print()

matriz3 = matriz * matriz2

for x in matriz3:
    print(x)