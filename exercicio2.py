#n = int(input("Informe a quantidade de vertices: "))
lista = [[0, 1, 2], [1, 0, 3, 4], [2, 0, 5, 6], [3, 1], [4, 1], [5, 2], [6, 2]]
fila = []
visitados = []
pilha = []

def cria_lista():
    for i in range(n):
        lista.append([i])
    return cria_lista

def inserir_aresta():
    for x in range(n):
        v1 = int(input("Inserir vertice: "))
        v2 = int(input("Inserir vertice a ser ligado: "))
        lista[x].append(v1)
        lista[x - 1].append(v2)
    print(lista)
  
def busca_largura():
    fila.append(0)
    while len(fila) != 0:
        v = fila[0]
        visitados.append(v)
        for j in lista[v]:
            if (j not in fila) and (j not in visitados):
                fila.append(j)
        fila.pop(0)
        print("Fila: " + str(fila))
        print("Visitados: " + str(visitados))

def busca_profundidade():
    visitados = []
    pilha.append(0)
    while len(pilha) != 0:
        v = pilha[-1]
        visitados.append(v)
        pilha.pop()
        for j in lista[v]:
            if (j not in pilha) and (j not in visitados):
                pilha.append(j)
        print("Pilha: " + str(pilha))
        print("Visitados: " + str(visitados))
        
#cria_lista()
#inserir_aresta()
print("***Busca por largura***")
busca_largura()
print("***Busca por profundidade***")
busca_profundidade()
