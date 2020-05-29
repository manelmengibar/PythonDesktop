from tkinter import *
import os
os.system('clear')

#Creamos una ventana con su título y las dimensiones.

root = Tk()
root.title('Manel Mengíbar - My first desktop App')
root.geometry("400x600")

#Creamos una funció que llamaremos más adelante:

def hello():

    #hello_label toma como valor lo que hayamos introducido en myTextbox
    hello_label = Label(root, text="Hello " + myTextbox.get())
    #pack sirve para introducirlo en la ventana creada.
    hello_label.pack()



#Añadimos varios elementos a la ventana.

myLabel = Label(root , text="Enter your fist name:")
myLabel.pack()

myTextbox = Entry(root, width=30)
myTextbox.pack()

#Al presionar el boton llamaremos a la función hello.
myButton = Button(root, text="Submit", command=hello)
myButton.pack()




#Este loop nos permite actualizar la ventana cada poco tiempo para mostrar los cambios
#por ejemplo cuando movemos el ratón.

root.mainloop()
