nota = int(input('Escribe tu nota:'))

if nota>0 and nota <20:
    if nota>15:
        print("MUY BUENA NOTA BRO")
    elif nota>11:
        print("A LAS JUSTAS APROBASTE")
    else:
        print("GG WP")
else:
    print("ANORMALIDADES EN TU NOTA")