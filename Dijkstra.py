from re import X
import sys
 
class Grafo():
 
    def __init__(self, vertx):
        self.V = vertx
        self.graph = [[0 for column in range(vertx)]
                      for row in range(vertx)]
 
    def pSol(self, dist):
        print("\nDistancia del vértice a la fuente DIJKSTRA")
        for node in range(self.V):
            print(node, " - ", dist[node])
 

    def minDistancia(self, dist, sptSet):
        min = sys.maxsize

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 

    def dijk(self, source):
 
        dist = [sys.maxsize] * self.V
        dist[source] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            u = self.minDistancia(dist, sptSet)
 
            sptSet[u] = True
 

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: dist[v] = dist[u] + self.graph[u][v]
 
        self.pSol(dist)
 
f = Grafo(9)
f.graph = [[0, 2, 0, 0, 0, 0, 0, 8, 0],
           [2, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 17, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 17, 10, 0, 3, 0, 0],
           [0, 0, 0, 0, 0, 3, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
 
f.dijk(0)