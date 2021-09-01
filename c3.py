from tkinter import *
import random

root = Tk()
root.title("Tarea POO")
root.geometry("300x120")
root.resizable(False,False)
label=Label(root,text="Ingrese sus datos",background="aqua",foreground="blue").grid(row=0,column=1)
label1=Label(root,text="Título").grid(row=1,column=0, sticky=W)
label2=Label(root,text="Ruta").grid(row=2,column=0,sticky=W)
label3=Label(root,text="Descripción").grid(row=3,column=0,sticky=W)

titulo=StringVar()
ruta=StringVar()
descripcion=StringVar()

titulo_entry=Entry(textvariable=titulo,width="40").grid(row=1,column=1)
ruta_entry=Entry(textvariable=ruta,width="40").grid(row=2,column=1)
descripcion_entry=Entry(textvariable=descripcion,width="40").grid(row=3,column=1)


def ck1():
	titulo_entry=str(titulo.get())
	ruta_entry=str(ruta.get())
	descripcion_entry=str(descripcion.get())
	print("Nueva alta de datos")
	print(titulo_entry, "\t", ruta_entry, "\t", descripcion_entry)


def ck2():
	_random_colors=ranint.choice(0,65536)
	root.config(background_=_random_colors)

b1=Button(root,text="Alta", command=ck1).grid(row=4,column=0)
b2=Button(root,text="Sorpresa", command=ck2).grid(row=4, column=1)

mainloop()