print("Faca uma matriz diagonal/matriz identidade:")

matriz = []
linhas = int(input("Digite o numero de linhas: "))
colunas = int(input("Digite o numero de colunas: "))

if (linhas == colunas):
	for i in range (colunas):
		linha = []
		for j in range (linhas):
			if(i == j):
				x=input("Digite o numero que deseja: ")
				linha.append(x)
			if (i!=j):
				x=0
				linha.append(x)
		matriz.append(linha)
for x in matriz:
	print(x)