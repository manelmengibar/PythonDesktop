
from tkinter import *
from tkinter import filedialog
import os


root = Tk()
root.title('Codemy.com')
root.geometry("600x400")

#Función que abrirá el programa.
def open_program():
    my_program =filedialog.askopenfilename()
    #Esto nos muestra la ruta del programa que queremos abrir en la label creada más abajo.
    my_label.config(text="Ruta de la aplicación:" + my_program )
    #Abripmos el programa seleccionado con el comando bash "open "directorio en el que se encuentra la app"
    #En este caso la ruta de la app se guarda en la variable my_program.
    os.system("open " + my_program)



#Botón que llamará a la función para abrir el programa
my_button = Button(root, text='Open Program', command=open_program)
my_button.pack(pady=30)

#Etiqueta que nos muestra la ruta del programa seleccionado.
my_label = Label(root, text="")
my_label.pack(pady=50)

root.mainloop()
