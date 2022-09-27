def asignar(c):
    n = len(c)
    ms, cms = init_ms(c)
    cma = compute_cma([],c)

    if cma<cms:
        nodo_raiz = [[], cma]
        lista = [nodo_raiz]
    while len(lista)>0:
        x, cma = lista.pop()
        tareas = [t for t in range(n) if t not in x]
        for t in tareas:
            x_new = x[:] + [t]
            cma_new = compute_cma(x_new, c)
            if cma_new < cms:
                if len(x_new) == n :
                    ms, cms = x_new, cma_new
                    while len(lista) > 0 and lista[0][1]>= cms:
                        lista.pop(0)
                else:
                    i = len(lista)-1
                    while i>= 0 and lista [i][1] < cma_new:
                        i=i-1
                    lista.insert(i+1,[x_new,cma_new])
    return ms, cms

def init_ms(c):
    n = len(c)
    cdiag1 = 0
    cdiag2 = 0
    for i in range(n):
        cdiag1 += c[i][i]
        cdiag2 += c[i][n-i-1]
    if cdiag1 <= cdiag2:
        return [i for i in range(n)], cdiag1
    else:
        return [n-i-1 for i in range(n)], cdiag2

def compute_cma(x,c):
    n = len(c)
    k = len(x)
    coste_x = 0
    for i in range(k):
        coste_x += c[i][x[i]]
    sum_minf = sum(min(c[i][j] for j in range(n) if j not in x) for i in range (k,n))
    sum_minc = sum(min(c[i][j] for i in range(k,n)) for j in range(n) if j not in x)
    return coste_x + max(sum_minf, sum_minc)