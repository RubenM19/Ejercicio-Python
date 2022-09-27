#Igual a la tarea basado en el ejemplo de asientos back
def back(i,n,pila,cola):
    global cont
    if sumP(pila) == 9:
        cont = cont +1
        print(f'{cont}.',end=' ')
        print(pila)
    else:
        j=i
        while j<n:
            if (( len(cola) >= 1 and sumP(pila) < 9)):
                pila.append(cola.pop(0))
                back((i+1),n,pila,cola)
                cola.append(pila.pop())
            else:
                cola.append(cola.pop(0))
            j=j+1

def sumP(pila):
    suma = sum(pila)
    return suma

cont = 0
cola = [2, 3, 6, 1, 5]
back(0, len(cola),[],cola)