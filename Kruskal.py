class Grafo:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
 
    def nuevo_borde(self, u, v, w):
        self.graph.append([u, v, w])
 
 
    def buscar(self, parent, i):
        if parent[i] == i:
            return i
        return self.buscar(parent, parent[i])
 
    def union(self, parent, rank, x, y):
        xroot = self.buscar(parent, x)
        yroot = self.buscar(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
  
    def kruskal(self):
        print("\nKRUSKAL:")
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.buscar(parent, u)
            y = self.buscar(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        for u, v, weight in result:
            print("Borde:",u," - ", v,end =" ")
            print(": ",weight)
 
 
g = Grafo(5)
g.nuevo_borde(0, 1, 8)
g.nuevo_borde(0, 2, 5)
g.nuevo_borde(1, 2, 9)
g.nuevo_borde(1, 3, 11)
g.nuevo_borde(2, 3, 15)
g.nuevo_borde(2, 4, 10)
g.nuevo_borde(3, 4, 7)
g.kruskal()