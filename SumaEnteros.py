def tabla(v):
    global t
    t = [0]
    for i in range (len(v)-1,0,-1):
        t.insert(0,t[0]+v[i])

def suma_enteros(x,v,suma,M):
    global t
    k = len(x)
    n = len(v)

    if k == n:
        return [x]
    ls = []

    if suma + v[k] <= M and suma + v[k] + t[k] >= M:
        ls = ls + suma_enteros(x[:]+[1],v,suma+v[k],M)
    if suma + t[k] >= M:
        ls = ls + suma_enteros(x[:]+[0],v,suma,M)
    return ls