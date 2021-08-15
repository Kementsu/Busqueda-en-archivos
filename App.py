import tkinter
from tkinter import Button, Label, Pack, StringVar, Toplevel, font
from tkinter.constants import RIDGE
from typing import Text

def pantalla1():
    global ruta
    global texto
    global root
    root = tkinter.Tk()
    root.geometry("300x150")
    root.title("Buscador de texto")
    root.configure(bg="white")
    root.resizable(False, False)

    # Almacenar variables
    ruta = tkinter.StringVar()
    texto = tkinter.StringVar()
    # Funcion
    
    # marco
    ventana = tkinter.Frame(root)
    ventana.pack(padx=10, pady= 10, fill='x', expand=True)

    # ruta
    ruta_label = tkinter.Label(ventana, text = "Ruta : ")
    ruta_label.pack(fill='x', expand=True)

    ruta_entry = tkinter.Entry(ventana, textvariable = ruta)
    ruta_entry.pack(fill= 'x', expand=True)
    ruta_entry.focus()

    # texto
    texto_label = tkinter.Label(ventana, text = "Texto : ")
    texto_label.pack(fill='x', expand=True)

    texto_entry = tkinter.Entry(ventana, textvariable = texto)
    texto_entry.pack(fill= 'x', expand=True)

    # boton
    boton1 = tkinter.Button(ventana, text = "Buscar", command = pantalla2)
    boton1.pack()
 

root.mainloop()



def pantalla2():
    ruta_1 = ruta.get()
    texto_1 = texto.get()
    global root1
    root1 = Toplevel(root)
    root1.geometry("600x300")
    root1.title("Resultados")
    # marco1
    ventana1 = tkinter.Frame(root1)
    ventana1.pack(padx=10, pady= 10, fill='x', expand=True)

    # Funcion 2 (codigo buscador)
    # def Busca(ruta_1, texto_1):
    import os
    from sys import exec_prefix
    # def Busca(ruta_1, texto_1):
    carpeta = os.listdir(ruta_1)
    texto_2 = texto_1 + "\n" 
    # print(carpeta)
    for archivo in carpeta:
        with open(ruta_1 + '/' + archivo) as f_obj:
            lineas = f_obj.readlines()
            # print(lineas)
            index = 0
            for linea in lineas:
                index = index + 1
                if linea == texto_1 or linea == texto_2:
                    print("Texto encontrado en el archivo " + archivo + " en la linea " + str(index))
                    resultado_label = tkinter.Label(ventana1, text ="Texto encontrado en el archivo : " + archivo + " en la linea " + str(index))
                    resultado_label.pack(fill='x', expand=True)



pantalla1()