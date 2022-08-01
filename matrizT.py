print("Matriz transposta:")
print('--------------------------------------------')
print("Digite a matriz:")
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range (0 ,3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]  '))
print('-=-' * 40)
for linha in range(0, 3):
    for coluna in range(0, 3):
            print(f'[{matriz[linha][coluna]:^5}]', end= '')
    print()

print('-' * 90)
for linha in range (0,3):
	for coluna in range(0,3):
			print(f'[{matriz[coluna][linha]:^5}]', end= '')
	print()
print("=====Linha virou coluna=====")