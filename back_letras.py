def back(i,n,pila,cola):
    global cont
    if len(pila) == n:
        cont = cont +1
        print(f'{cont}.',end=' ')
        print(pila)
    else:
        global totalDeLetras
        for j in range(len(pila), totalDeLetras):
            if not (len(pila) > n):
                pila.append(cola.pop(0))
                back((len(pila)),n,pila,cola)
                cola.append(pila.pop())

cont = 0      
cola = ['a', 'n', 'r','v', 'm']
totalDeLetras = len(cola)
numeroDeLetras = 5
back(0,numeroDeLetras,[],cola)