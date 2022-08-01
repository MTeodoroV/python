print("Grafo completo:")

matriz = []
vertice = int(input("Digite o numero de vertice: "))
aresta = int(input("Digite o numero de aresta: "))

for i in range (vertice):
	linha = []
	for j in range (aresta):
		if(i == j):
			x=input("Digite os vertices: ")
			linha.append(x)
		if (i!=j):
			x=0
			linha.append(x)
	matriz.append(aresta)
for x in matriz:
	print(x)