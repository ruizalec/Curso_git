def es_primo(numero): 
    if numero < 2: # Los números menores que 2 no son primos
        return False
    for i in range(2, int(numero ** 0.5) + 1): # Verificar divisibilidad hasta la raíz cuadrada del número
        if numero % i == 0: # Si el número es divisible por i, no es primo
            return False
    return True

def obtener_numeros_pares_y_primos(minimo, maximo): 
    pares = []
    primos = []
    for num in range(minimo, maximo + 1): # Iterar desde el mínimo hasta el máximo
        if num % 2 == 0: # Verificar si el número es par
            pares.append(num)
        if es_primo(num): # Verificar si el número es primo
            primos.append(num)
    return primos, pares

def main():
    minimo = int(input("Ingresa el rango mínimo: ")) 
    maximo = int(input("Ingresa el rango máximo: "))
    primos, pares = obtener_numeros_pares_y_primos(minimo, maximo) 
    
    print(f"Números primos entre {minimo} y {maximo}: {primos}") 
    print(f"Números pares entre {minimo} y {maximo}: {pares}") 

if __name__ == "__main__":
    main()
