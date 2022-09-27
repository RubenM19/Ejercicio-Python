def MayorSubcadenaComun(cadena1, cadena2):
    listString1 = list(cadena1)
    listString2 = list(cadena2)
    max = 0
    t = [[0 for m in range(len(listString2) + 1)] for i in
         range(len(listString1) + 1)]
    for i in range(1, len(listString1) + 1):
        for j in range(1, len(listString2) + 1):
            if listString1[i-1] == listString2[j-1]:
                t[i][j] = t[i-1][j-1]+1
            else:
                t[i][j] = 0

            if t[i][j] > max:
                max = t[i][j]
    print()
    print(t)
    return max

#Cadenas de ejemplo de la PPT
cadena1 = "FISH"
cadena2 = "HISHO"
print()
print("Mayor Subcadena Común entre FISH y HISHO")
print(MayorSubcadenaComun(cadena1, cadena2))


def MayorSubsecuenciaComun(cadena1, cadena2):
    listString1 = list(cadena1)
    listString2 = list(cadena2)
    maxi = 0
    t = [[0 for m in range(len(listString2) + 1)] for i in
         range(len(listString1) + 1)]
    for i in range(1, len(listString1) + 1):
        for j in range(1, len(listString2) + 1):
            if listString1[i-1] == listString2[j-1]:
                t[i][j] = t[i-1][j-1]+1
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
            if t[i][j] > maxi:
                maxi = t[i][j]
    print()
    print(t)
    return maxi

#Cadenas de ejemplo de la PPT
cadena1 = "FISH"
cadena2 = "FOSH"
print()
print("Mayor Subsecuencia Común entre FISH y FOSH")
print(MayorSubsecuenciaComun(cadena1, cadena2))

#Cadenas de ejemplo de la PPT
cadena1 = "FORT"
cadena2 = "FOSH"
print()
print("Mayor Subcadena Común entre FORT Y FOSH")
print(MayorSubsecuenciaComun(cadena1, cadena2))
