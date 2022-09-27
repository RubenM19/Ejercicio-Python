import random

#Ingresamos nuestro algoritmo de Backtracking para N Reinas modificado de C++

def comprobar(reinas,n,k):
  for i in range(n):
    reinas2=reinas[i][0]
    if k==reinas2 or k-n==reinas2-i or k+n==reinas2+i:
      return False
  return True

def reinasBacktracking(nReinas,j,solucion):
  if j==nReinas:
    return solucion
  for i in range(nReinas):
    if comprobar(solucion,j,i):
      solucion[j]=[i,j].copy()
      s=reinasBacktracking(nReinas,j+1,solucion)
      if s!=None:
        return s
  return None

#Ingresamos nuestro algoritmo de Probabilista para N Reinas
#Codigo de la clase
def disponibles(y,n,columna,diagonal_izquierda,diagonal_derecha):
  columnas_disponibles = []
  for x in range(n):
    if(columna[x] or diagonal_izquierda[x+y] or diagonal_derecha[x-y+n-1]): 
      #Si la reina es atacada se debe volver a empezar
      continue
    columnas_disponibles.append(x)
  return columnas_disponibles
#Algoritmo como en la ppt
def reinasProbabilista(n,reinasFijas):
  solucion = []
  columna = [False]*n
  diagonal_izquierda = [False]*(n*2)
  diagonal_derecha = [False]*(n*2)
  while(len(solucion)!=reinasFijas and n>3):
    solucion = []
    columna = [False]*n
    diagonal_izquierda = [False]*(n*2)
    diagonal_derecha = [False]*(n*2)
    for y in range(0,reinasFijas):
      #Se coloca a la serina en un lugar random
      columnas_d = disponibles(y,n,columna,diagonal_izquierda,diagonal_derecha)
      #Sólo si hay columnas no atacadas
      if(columnas_d):
        x = random.choice(columnas_d)
      else:
        break
      columna[x] = diagonal_izquierda[x+y] = diagonal_derecha[x-y+n-1] = True
      solucion.append([x,y])
  return solucion

#Funcion Reinas principal

def reinas(numeroDeReinas):
    #Comprobamos que el numero de Reinas sea mayor a 3 para que no se rompa el cod
    if(numeroDeReinas>3):
        exito=False
        while exito==False:
            solucion=reinasProbabilista(numeroDeReinas,4)
            for i in range(0,numeroDeReinas-4):
                    solucion.append([None,None])
            solucion=reinasBacktracking(numeroDeReinas,4,solucion)
            if(solucion!=None):
                return solucion
    else:
        print("#Número de reinas no válido")
 

print("Problema de las N reinas Probabilístico y Backtracking - Las Vegas")
print("Ubicación de las reinas en el tablero las vegas: ")
kReinas = 5
print(reinas(kReinas))
print(reinas(kReinas))
print(reinas(kReinas))
print(reinas(kReinas))
print(reinas(kReinas))