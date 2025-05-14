def verificar_par_impar():
    while True:  # Bucle 
        try:
            numero = int(input("Introduce un número: "))  # Pedir número al usuario
            if numero % 2 == 0:
                print(f"El número {numero} es par.")
            else:
                print(f"El número {numero} es impar.")
            break  # Si el número es válido, salir del bucle
        except ValueError:
            print("Error: No ingresaste un número válido. Por favor, intenta de nuevo.")  

# Función principal que controla el flujo del programa
def main():
    while True:
        verificar_par_impar()  
        respuesta = input("¿Deseas calcular otro número? (sí/no): ").strip().lower()  
        if respuesta != "si":
            print("¡Gracias por usar el programa!")
            break  # si la respuesta es diferente de "sí", salir del bucle

# Llamada a la función principal
main()
