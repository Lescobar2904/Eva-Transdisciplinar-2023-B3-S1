import tkinter as tk
import pygame as pg
from PIL import ImageTk
ventana  =  tk.Tk()
ventana.geometry("1000x700")
nRES=(750,400)
pg.init()
pg.display.set_mode(nRES)


ima_emp = tk.PhotoImage(file="start.png")
ima_emp2 = tk.PhotoImage(file="Formula.png")
ima_emp3 = tk.PhotoImage(file="Valores.png")
ima_emp4 = tk.PhotoImage(file="overa.png")


fondore = tk.Label(ventana, image=ima_emp4)
fondore.place(x=0, y=0, width=1000, height=700)

boton1= tk.Button(ventana, image=ima_emp)
boton2= tk.Button(ventana, text = "Forma 1", bg = "yellow")
boton3= tk.Button(ventana, text = "Forma 2", bg = "yellow")

boton1.place(x=0, y=630, width=153, height=74)
boton2.place(x=381, y=476, width=309, height=112)
boton3.place(x=700, y=476, width=291, height=112)

li = tk.Label(ventana, text="", bg= "black")
li.place(x=372, y=0, width=15, height=700)
li2 = tk.Label(ventana, text="", bg= "black")
li2.place(x=387, y=461, width=614, height=15)


f = tk.Label(ventana, image=ima_emp3)
f.place(x=0, y=430, width=372, height=178)
ecua = tk.Label(ventana, image=ima_emp2)
ecua.place(x=0, y=0, width=203, height=99)

m2 = tk.Entry(ventana, bg= "pink")
m2.place(x=50, y=525, width=50, height=20)
h2 = tk.Entry(ventana, bg= "pink")
h2.place(x=50, y=550, width=50, height=20)
g2 = tk.Entry(ventana, bg= "pink")
g2.place(x=50, y=575, width=50, height=20)



ventana.mainloop()

