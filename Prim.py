INF = 9999999
# Numero de vértices
N = 5
#Creando grafo por matriz
Grafo = [[0, 16, 7, 0, 0],
         [16, 0, 7, 9, 2],
         [7, 7, 0, 2, 6],
         [0, 9, 2, 0, 1],
         [0, 2, 6, 1, 0]]

nodo_Seleccionado = [0, 0, 0, 0, 0]

sin_borde = 0

nodo_Seleccionado[0] = True

# Imprimimos resultados
print("\nPRIM")
print("Borde : Peso")
while (sin_borde < N - 1):
    
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if nodo_Seleccionado[m]:
            for n in range(N):
                if ((not nodo_Seleccionado[n]) and Grafo[m][n]):  
                    if minimum > Grafo[m][n]:
                        minimum = Grafo[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(Grafo[a][b]))
    nodo_Seleccionado[b] = True
    sin_borde += 1
