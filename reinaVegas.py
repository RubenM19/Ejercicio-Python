import random

def colocar(k):
    global x
    for j in range (k):
        if abs(k-j) == abs(x[j]-x[k] or x[j] == x[k]):
            return False
    return True
def backtracking (t):
    global n
    global y
    global x
    if(t>=n):
        for i in range(n):
            y[i] = x[i]
        return True
    else:
        for i in range(n):
            x[t] = i
            if(colocar(t) and backtracking(t+1)):
                return True
    return False

def ReinasLasVegas(stopVegas):
    k = 0
    count = 1
    global x
    global y
    global n
    while(k < stopVegas and count > 0):
        count = 0
        for i in range(n):
            x[k] = i
            if(colocar(k)):
                y[count] = i
                count += 1
        if(count > 0):
            x[k] = y[random.randint(0, count - 1)]
    return  count>0

def nReinas(stopVegas):
    global n
    global x
    global y
    found = False

    while(not ReinasLasVegas(stopVegas)):
        for i in range(n):
            print(x[i])

    if(backtracking(stopVegas)):
        for i in range(n):
            print(x[i])
        found = True

    return found

n = 8
x = [0 for m in range(n)]
y = [0 for m in range(n)]
nReinas(3)
print(x)