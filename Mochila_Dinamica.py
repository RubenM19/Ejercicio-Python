def MochilaDinamica(Max, pesos, beneficios, ):
    n = len(pesos)
    t =[[0 for m in range(Max + 1)] for i in range(n + 1)]
    for i in range (1, n+1):
        for m in range (1, Max+1):
            if pesos[i-1] <= m and beneficios[i-1] + t[i-1][m-pesos[i-1]] > t[i-1][m]:
                t[i][m] = beneficios[i-1] + t[i-1][m-pesos[i-1]]
            else:
                t[i][m] = t[i-1][m]
    print()
    print(t)
    return t[n][Max]

pesos = [1,3,4]
beneficio = [1500,2000,3000]
Max = 4
print()
print("Solución problema de la Mochila")
print(MochilaDinamica(Max,pesos,beneficio))