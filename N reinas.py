# Declaramos una variable global que va a ser las dimensiones del tablero a evaluar, en este caso 5 x 5
global N
N = 5


def mostrarSolucion(tablero):
    for i in range(N):
        for j in range(N):
            print(tablero[i][j], end=" ")
        print()

# Funcion para valuar si la reina puede o no colocarse en la posición "x"


def puedeColocarse(tablero, fila, col):

    # Verificamos la fila
    for i in range(col):
        if tablero[fila][i] == 1:
            return False

    # Verifique la diagonal superior en el lado izquierdo
    for i, j in zip(range(fila, -1, -1),
                    range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Verifique la diagonal inferior en el lado izquierdo
    for i, j in zip(range(fila, N, 1),
                    range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    return True


def solNQ(tablero, col):

    if col >= N:
        return True

    # Probamos colocar la reina en todos los espacios posibles
    for i in range(N):

        if puedeColocarse(tablero, i, col):

            # Colocamos la reina en la posicion [i][col]
            tablero[i][col] = 1

            # Recursiva para las demás reinas
            if solNQ(tablero, col + 1) == True:
                return True

            # Si la posición escogida no es la solución, la reemplazamos por un 0
            tablero[i][col] = 0

    # Si la reina no puede colocarse en ninguna fila de la columna, se retorna falso
    return False


# Funcion principal con el tablero y la condición cuando no existe solucion
def solucionNQ():
    tablero = [[0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]]

    if solNQ(tablero, 0) == False:
        print("No hay solución")
        return False

    mostrarSolucion(tablero)
    return True


# Empezamos con la funcion solucionNQ
solucionNQ()
