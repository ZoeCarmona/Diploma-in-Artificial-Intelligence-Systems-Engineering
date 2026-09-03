'''
    Reto:
    - Leer un archivo CSV con registros.
    - Representar cada registro como un objeto.
    - Aplicar filtros usando colecciones. (quitar duplicados)
    - Guardar resultados en JSON.
'''

import csv
import json

# Clase que usamos para representar una persona
class Persona:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

# Leer un archivo CSV con registros
def procesarCSV(rutaArchivo):
    with open(rutaArchivo, encoding="utf-8") as f:
        lector = csv.reader(f)
        listaLector = list(lector)
        listaLectorFiltrada = listaLector.pop(0)
        return listaLector

# Representar cada registro como un objeto
def guardarDatosAObjeto(listaDatos):
    listaPersonas = []
    i = 0
    for persona in listaDatos:
        listaPersonas.append(Persona(listaDatos[i][0], listaDatos[i][1], listaDatos[i][2]))
        i+=1
    return listaPersonas

# Aplicar filtros usando colecciones (quitar duplicados)
def limpiar_duplicados(lista_personas):
    vistos = set()
    for persona in lista_personas:
        vistos.add((persona.nombre, persona.edad, persona.carrera))

    listaPersonasFiltrada = []
    for nombre, edad, carrera in vistos:
        listaPersonasFiltrada.append(Persona(nombre, edad, carrera))
    return listaPersonasFiltrada
    # vistos = { (p.nombre, p.edad, p.carrera) for p in lista_personas }
    # return [Persona(nombre, edad, carrera) for nombre, edad, carrera in vistos]

# Guardar resultados en JSON
def guardar_json(lista_personas, ruta_salida):
    datos = []
    for p in lista_personas:
        datos.append(vars(p))

    #datos = [p.__dict__ for p in lista_personas]

    with open(ruta_salida, mode="w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

def main():
    listaDatos = procesarCSV("datos.csv")
    listaPersonas = guardarDatosAObjeto(listaDatos)
    listaLimpia = limpiar_duplicados(listaPersonas)
    guardar_json(listaLimpia, "./salidaDatos.json")
    with open("salidaDatos.json", encoding="utf-8") as f:
      data = json.load(f)
      print(data)


if __name__ == "__main__":
    main()
