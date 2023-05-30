import tkinter as tk
import pygame as pg
nRES=(750,400)
pg.init()
pg.display.set_caption('Energia potencial gravitacional')
pg.display.set_mode(nRES)

ventana  =  tk.Tk()
ventana.geometry("1000x700")

fondore = tk.Label(ventana, text="", bg= "sky blue")
fondore.place(x=0, y=0, width=1000, height=700)

boton1= tk.Button(ventana, text = "Empieza", bg = "green")
boton2= tk.Button(ventana, text = "Forma 1", bg = "yellow")
boton3= tk.Button(ventana, text = "Forma 2", bg = "yellow")

boton1.place(x=0, y=630, width=153, height=74)
boton2.place(x=381, y=476, width=309, height=112)
boton3.place(x=700, y=476, width=291, height=112)

li = tk.Label(ventana, text="", bg= "black")
li.place(x=372, y=0, width=15, height=700)
li2 = tk.Label(ventana, text="", bg= "black")
li2.place(x=387, y=461, width=614, height=15)

f = tk.Label(ventana, text="", bg= "orange")
f.place(x=0, y=430, width=372, height=178)
ecua = tk.Label(ventana, text="EPG= m * g * h", bg= "orange")
ecua.place(x=0, y=0, width=203, height=99)

fondo=tk.Label(ventana, text= "Eliga sus valores (m en kg) y (h en metros)", bg= "red")
fondo.place(x=0, y=390, width=372, height=50)
m=tk.Label(ventana, text= "m= ", bg= "orange")
g=tk.Label(ventana, text= "g= ", bg= "orange")
h=tk.Label(ventana, text= "h= ", bg= "orange")
m.place(x=0, y=490, width=60, height=30)
h.place(x=0, y=520, width=60, height=30)
g.place(x=0, y=550, width=60, height=30)

m2 = tk.Entry(ventana, bg= "pink")
m2.place(x=50, y=495, width=50, height=20)
h2 = tk.Entry(ventana, bg= "pink")
h2.place(x=50, y=525, width=50, height=20)
g2 = tk.Entry(ventana, bg= "pink")
g2.place(x=50, y=555, width=50, height=20)



ventana.mainloop()

