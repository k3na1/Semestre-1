import csv
import json

#Ejercicio 1

def clasificar_edad(edad):
    if edad >= 25:
        return "Mayor de edad"
    else:
        return "Menor de edad"

# Nombre del archivo CSV y JSON
archivo_csv = "datos.csv"
archivo_json = "mayores.json"

# Lista para almacenar los mayores de 25 años
mayores = []

# Lectura del archivo CSV y procesamiento de datos
with open(archivo_csv, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        nombre = row['Nombre']
        edad = int(row['Edad'])
        comuna = row['Comuna']
        
        # Clasificar la edad
        estado_edad = clasificar_edad(edad)
        
        # Mostrar en consola la información
        print(f"Nombre: {nombre}, Edad: {edad}, Estado: {estado_edad}, Comuna: {comuna}")
        
        # Guardar en la lista mayores si es mayor o igual a 25 años
        if edad >= 25:
            mayores.append({
                'Nombre': nombre,
                'Edad': edad,
                'Comuna': comuna,
                'Estado': estado_edad
            })

# Guardar la lista de mayores en un archivo JSON
with open(archivo_json, mode='w', encoding='utf-8') as json_file:
    json.dump(mayores, json_file, indent=4, ensure_ascii=False)

print(f"\nSe han guardado los datos de las personas mayores o iguales a 25 años en '{archivo_json}'.")

#Ejercicio 2

# Función para verificar si el RUN termina en los dígitos requeridos
def es_ganador(run):
    digitos_finales = run[-3:-1] + run[-1]  # Tomar los últimos tres dígitos antes del dígito verificador
    return digitos_finales in ['92', '95', '84']

# Nombre del archivo CSV y JSON
archivo_csv = "listadoRun.csv"
archivo_json = "ganadores.json"

# Lista para almacenar los ganadores
ganadores = []

# Lectura del archivo CSV y procesamiento de datos
with open(archivo_csv, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        run = row['run']
        nombre = row['nombre']
        
        # Verificar si es ganador
        if es_ganador(run):
            ganadores.append({
                'run': run,
                'nombre': nombre
            })

# Guardar la lista de ganadores en un archivo JSON
with open(archivo_json, mode='w', encoding='utf-8') as json_file:
    json.dump(ganadores, json_file, indent=4, ensure_ascii=False)

print(f"Se han guardado los datos de los ganadores en '{archivo_json}'.")

