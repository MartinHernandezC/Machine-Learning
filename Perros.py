import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

def leer_csv(link):
    df = pd.read_csv(link)
    datos = df[['nombre','edad','raza','foto(url)','autor','Link Base']].head(10)
    return datos

def graficar(datos):
    fig, ax = plt.subplots()
    ax.hist(datos['edad'], density=True, bins=10)
    ax.set_xlabel('Edad')
    ax.set_ylabel('Densidad')
    ax.set_title('Distribución normal de edades')
    plt.show()
    fig, ax = plt.subplots()
    ax.hist(datos['raza'], density=True, bins=10)
    ax.set_xlabel('Raza')
    ax.set_ylabel('Densidad')
    ax.set_title('Distribución normal de edades')
    plt.show()

def interactuar():
    link = entrada.get()
    datos = leer_csv(link)
    graficar(datos)

ventana = tk.Tk()
ventana.title('Gráfica de distribución normal')
etiqueta = tk.Label(ventana, text='Ingresa el link del archivo CSV:')
etiqueta.pack()
entrada = tk.Entry(ventana)
entrada.pack()
boton = tk.Button(ventana, text='Graficar', command=interactuar)
boton.pack()
ventana.mainloop()
