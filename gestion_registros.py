"""Juntos: w = write/escribir o escribir, r = read/leer, A = appenda/anadir.
1. Reemplazar 'Megan,38,desayuno' con su nombre, edad, y su preferencia entre desayuno almuerzo, o cena.
2. Correr este codigo en su maquina local (que no tenga errores)
3. Verificar que se crea el archivo salida.txt, en el directorio actual, con sus datos.
"""

# w Funcion para escribir en el archivo
#def escribirDocumento(data):
#    with open("salida.txt", "w", encoding="utf-8") as fileToWriteTo:
#        fileToWriteTo.write(data + "\n")


# TODO 1:
# Reemplazar 'Megan,38,desayuno' con su nombre, edad, y su preferencia entre desayuno almuerzo, o cena.
#miEntrada = 'Megan,38,desayuno'
#escribirDocumento(miEntrada)
def escribirDocumento(data):
    with open("salida.txt", "w", encoding="utf-8") as fileToWriteTo:
        fileToWriteTo.write(data + "\n")
miEntrada = 'Ana,34,almuerzo'
escribirDocumento(miEntrada)

# TODO 2:
# a Despues de verificar el documento salida.txt, agregar 3 lineas con datos de companeros. 
def agregarAlDocumento(data):
    with open("salida.txt", "a") as fileToWriteTo:
        fileToWriteTo.write(data + "\n") 
agregarAlDocumento("Carlos,29,desayuno")
agregarAlDocumento("María,27,cena")
agregarAlDocumento("Luis,31,almuerzo")
        
# TODO 3: 
# r 

def leerDocumento():
    with open("salida.txt", "r") as fileToReadFrom:
        contenido = fileToReadFrom.read()
        print(contenido)

leerDocumento()

# TODO 4:
# Cambiar capitulo13.py a un archivo de csv. Usarlo para que imprima solo los cantantes. 

import csv

with open("capitulo13.csv", "r", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila["cantante"])
#TODO 5:
# Crear codigo para hace otra cosa con el archiva .csv"""

import csv

conteo_paises = {}

with open("capitulo13.csv", "r", encoding="utf-8") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        pais = fila["pais"]
        conteo_paises[pais] = conteo_paises.get(pais, 0) + 1

print("Conteo por país:")
print(conteo_paises)