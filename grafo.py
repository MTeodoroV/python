import igraph

def grafo(vertices, arestas):
    grafo = {}
    for v in vertices:
        grafo[v] = []
    for a in arestas:
        grafo[a[0]].append(a[1])
        print(grafo)

    return grafo

vertices = ['a', 'b', 'c']
arestas = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'b')]

print("O numero de vertices é: ")
print(len(vertices))
print("***************")
print("O numero de arestas é: ")
print(len(arestas))
print("***************")

grafo = grafo(vertices, arestas)