def grafo(vertices, arestas):
    grafo = {}
    for v in vertices:
        grafo[v] = []
    for a in arestas:
        grafo[a[0]].append(a[1])
        print(grafo)
    return grafo
nVertices = int(input("Digite o numero de vertices:"))
for i in range (nVertices):
    vertices = str(input("Digite os vertices:"))
# vertices = ['a', 'b', 'c']
arestas = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'b')]
grafo = grafo(vertices, arestas)