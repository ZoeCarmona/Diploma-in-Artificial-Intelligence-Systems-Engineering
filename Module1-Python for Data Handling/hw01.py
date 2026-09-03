# Construir un script que:
# 1 Lea una lista de números (predefinida o por entrada del usuario),
# 2 Calcule estadísticas básicas (promedio, min, max),
# 3 Clasifique cada elemento (por ejemplo: bajo/medio/alto),
# 4 Organice el código en funciones.

# Función que lee y valida una lista de números dada por el usuario
def leerNumeros():
    while True:
        # Variable que guarda los números ingresados por el usuario
        entrada = input('\nIngresa una lista de números separados por un espacio: ')
        
        # Validamos que no esté vacío
        if not entrada.strip():
            print("Error: La lista no puede estar vacía. Ingresa al menos un número")
            continue
            
        try:
            # Intentamos convertir cada elemento a float
            listaNumeros = [float(x) for x in entrada.split()]
            # Si la conversión es exitosa, rompemos el ciclo
            break
        except ValueError:
            # Si alguien escribió una letra o símbolo, cae aquí y avisa
            print("Error: Solo es posible ingresar números")

    return listaNumeros

# Función que permite calcular el promedio, mínimos y máximos de la lista de números dada por el usuario
def estadisticasBasicas(listaNumeros):
    promedio = sum(listaNumeros) / len(listaNumeros)
    numnumMin = min(listaNumeros)
    numnumMax = max(listaNumeros)
    return f'El promedio de la lista es {promedio}, con {numnumMin} como mínimo y {numnumMax} como máximo'

# Funcion que clasifica a los números de la lista en bajo, medio o alto
def clasificacionElementos(listaNumeros):
    numMin = min(listaNumeros)
    numMax = max(listaNumeros)

    # Si todos los números son iguales, el rango es 0
    if numMin == numMax:
        print("\nTodos los números son iguales, por lo tanto su categoría es ÚNICO")
        return

    # Calculamos los límites de los tercios basados en el rango
    rango = numMax - numMin
    limite_bajo = numMin + (rango / 3)
    limite_medio = numMin + (2 * (rango / 3))
    
    for num in listaNumeros:
        if num <= limite_bajo:
            categoria = "bajo"
        elif num <= limite_medio:
            categoria = "medio"
        else:
            categoria = "alto"
            
        print(f"El número {num} se clasifica como: {categoria}")

def main():
    print('Tarea 01')

    # Creamos variable para almacenar lista
    listaNumeros = leerNumeros()

    print("\n--- Lista guardada ---")
    print(listaNumeros)

    print("\n--- Estadistica básica ---")
    print(estadisticasBasicas(listaNumeros))

    print("\n--- Clasificación de elementos ---")
    clasificacionElementos(listaNumeros)

if __name__ == '__main__':
    main()
