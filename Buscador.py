# Este buscador solo servira para archivos del mismo tipo ubicados en el mismo directorio
import os
from sys import exec_prefix
def Busca(ruta_1, texto_1):
    carpeta = os.listdir(ruta_1)
    texto_2 = texto_1 + "\n" 
    # print(carpeta)
    for archivo in carpeta:
        with open(ruta_1 + '/' + archivo) as f_obj:
            lineas = f_obj.readlines()
            print(lineas)
            index = 0
            for linea in lineas:
                index = index + 1
                if linea == texto_1 or linea == texto_2:
                    print("Texto encontrado en el archivo " + archivo + " en la linea " + str(index))
Busca("C:/Users/kemen/Desktop/Buscador/Prueba de buscador","Hola") 