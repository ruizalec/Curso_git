#Escribir una función que pida un número entero entre 1 y 10 y
# guarde en un fichero con el nombre tabla-n.txt
# la tabla de multiplicar de ese número, donde n es el número introducido.
def tabla_multiplicar():
    try:
        n = int(input("Ingresa un numero entre 1 y 10: "))
        if 1 <= n <= 10:
            archivo = f"tabla-{n}.txt"
            with open(archivo, "w") as archivo:
                for i in range(1,11):
                    resultado = n * i
                    archivo.write(f"{n} x {i} = {resultado}\n")
            print (f"Tabla de multiplicar del {n} x {i} guardada en {archivo}")
        else:
            print ("El numero ingresado no es valido")
    except ValueError:
        print ("El numero ingresado no es valido ingresa uno nuevo")

tabla_multiplicar()

