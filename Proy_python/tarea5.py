def calcular_promedio():
    while True:  # Bucle para asegurar que el usuario ingrese un número válido
        try:
            n = int(input("¿Cuántos números desea ingresar para calcular el promedio? "))
        
            if n == 0:
                raise ValueError("La cantidad de números no puede ser cero.")
        
            suma = 0
            for i in range(n):
                try:
                    numero = float(input(f"Ingrese el número {i+1}: "))
                    suma += numero
                except ValueError:
                    print("Error: Se debe ingresar un valor numérico.")
                    return
            
            promedio = suma / n
            print(f"El promedio de los números es: {promedio}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Se ha producido un error inesperado: {e}")

def main():
    while True:
        calcular_promedio()
        respuesta = input("¿Deseas calcular el promedio de otro conjunto de números? (sí/no): ").strip().lower()
        if respuesta != "si":
            print("¡Gracias por usar el programa!")
            break
main()