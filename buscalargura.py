grafo = [[0, 1, 2], [1, 0, 3, 4], [2, 0, 5, 6], [3, 1], [4, 1], [5, 2], [6, 2]]
fila = []
visitados = []
pilha = []



def adjacentes_vertice(v, lista):
    adj = []
    for i in range(len(lista)):
        if (lista[i][0] == v):
            adj = lista[i][1:]
    return adj

def buscaLargura(grafo, verticeInicial=None):
    if verticeInicial == None:
        x = int(input("Informe o vertice: "))
    else:
        x = verticeInicial
        fila = [x]
        visitados = [x]
        while len(fila):
            n = fila.pop(0)
            for m in adjacentes_vertice(grafo, n):
                if(m not in visitados):
                    visitados.append(0)
                    fila.append(m)
        print(fila)
        return visitados
    
buscaLargura(grafo, verticeInicial=None)