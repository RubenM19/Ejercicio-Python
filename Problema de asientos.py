def back(i,n,pila,cola):
    global cont
    if i == n:
        cont = cont +1
        print(f'{cont}.',end=' ')
        print(pila)
    else:
        j=i
        while j<n:
            if not ((i == 1 and cola[0] == 'a') or (i==0 and cola[0] == 'r')):
                pila.append(cola.pop(0))
                back((i+1),n,pila,cola)
                cola.append(pila.pop())
            else:
                cola.append(cola.pop(0))
            j=j+1

cont = 0
cola = ['a', 'n', 'r']
back(0, len(cola),[],cola)