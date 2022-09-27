num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if num1 > num2:
    print(f"{num1} es mayor.")
elif num2 > num1:
    print(f"{num2} es mayor.")
else:
    print("Son iguales.")