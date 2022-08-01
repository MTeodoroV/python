def multiplicacao(l):
    return l*l

print("Faca uma matriz diagonal/matriz identidade:")

matriz = []
linhas = int(input("Digite o numero de linhas: "))
colunas = int(input("Digite o numero de colunas: "))

if (linhas == colunas):
	for i in range (colunas):
		linha = []
		for j in range (linhas):
			if(i == j):
				l=int(input("Digite o numero que deseja: "))
l= multiplicacao(l)
linha.append(l)
if (i!=j):
	y=0
	linha.append(y)
	matriz.append(linha)
for l in matriz:
	print(l)