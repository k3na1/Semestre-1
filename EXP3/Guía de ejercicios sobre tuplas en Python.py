#Ejercicio 1

# 1. Crear la tupla `informacion`
informacion = ("Juan", 30, "Ciudad de México")

# 2. Acceder e imprimir cada elemento de la tupla utilizando índices
print("Nombre:", informacion[0])
print("Edad:", informacion[1])
print("Ciudad de residencia:", informacion[2])

# 3. Utilizar el desempaquetado de tuplas para asignar los valores a variables individuales
nombre, edad, ciudad = informacion

# Imprimir las variables individuales
print("\nDesempaquetado de tupla:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad de residencia:", ciudad)

#Ejercicio 2

# 1. Crear la tupla `numeros` del 1 al 10
numeros = tuple(range(1, 11))

# 2. Calcular la suma de los elementos de la tupla
suma_numeros = sum(numeros)
print("\nSuma de los números:", suma_numeros)

# 3. Encontrar el valor máximo y mínimo en la tupla
maximo = max(numeros)
minimo = min(numeros)
print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)

# 4. Contar cuántas veces aparece el número 5 en la tupla
veces_numero_5 = numeros.count(5)
print("Número de veces que aparece el 5:", veces_numero_5)

#Ejercicio 3

# 1. Crear la tupla `letras` del alfabeto de la 'a' a la 'j'
letras = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')

# 2. Obtener una sub-tupla con las primeras 5 letras e imprimirla
primeras_cinco = letras[:5]
print("\nPrimeras 5 letras:", primeras_cinco)

# 3. Obtener una sub-tupla con las últimas 3 letras e imprimirla
ultimas_tres = letras[-3:]
print("Últimas 3 letras:", ultimas_tres)

# 4. Obtener una sub-tupla con cada segunda letra e imprimirla
cada_segunda_letra = letras[::2]
print("Cada segunda letra:", cada_segunda_letra)
