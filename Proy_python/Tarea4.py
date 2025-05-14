def calcular_IMC():
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    IMC = peso / (altura ** 2)
    print("Su IMC es:", IMC)
    
    
def convertir_Fahrenheit_a_Celsius():
    frh = float(input("Ingrese grados Fahrenheit: "))
    cel = (frh - 32) * 5 / 9
    print("Grados Celsius:", cel)

def calcular_factorial():
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    n = int(input("Ingrese un número para calcular su factorial: "))
    print("El factorial de", n, "es:", factorial(n))

def main():
    while True:
        print("Bienvenido, por favor escriba la opción que desea realizar:")
        print("1. Calcular IMC")
        print("2. Convertir Fahrenheit a Celsius")
        print("3. Calcular factorial de un número")
        print("4. Salir")

        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == "1":
            calcular_IMC()
        elif opcion == "2":
            convertir_Fahrenheit_a_Celsius()
        elif opcion == "3":
            calcular_factorial()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
