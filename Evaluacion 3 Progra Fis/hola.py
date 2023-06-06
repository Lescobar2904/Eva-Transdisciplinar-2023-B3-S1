import tkinter as tk
import pygame as pg
from PIL import ImageTk
ventana  =  tk.Tk()
ventana.geometry("1000x700")
nRES=(750,400)
pg.init()
pg.display.set_mode(nRES)


ima_emp  = tk.PhotoImage(file="start.png")
ima_emp2 = tk.PhotoImage(file="Formula.png")
ima_emp3 = tk.PhotoImage(file="Valores.png")
ima_emp4 = tk.PhotoImage(file="overa.png")
ima_emp5 = tk.PhotoImage(file="Reset.png")

#----------------------------------------
# interfaz y ventana
#----------------------------------------

fondore = tk.Label(ventana, image=ima_emp4)
fondore.place(x=0, y=0, width=1000, height=700)


li = tk.Label(ventana, text="", bg= "black")
li.place(x=372, y=0, width=15, height=700)
li2 = tk.Label(ventana, text="", bg= "black")
li2.place(x=387, y=461, width=614, height=15)


f = tk.Label(ventana, image=ima_emp3)
f.place(x=0, y=430, width=372, height=178)
ecua = tk.Label(ventana, image=ima_emp2)
ecua.place(x=0, y=0, width=203, height=99)


#------------------------------------------------
# funcion de formula
#------------------------------------------------

def formula():
    try:
        m = m2.get()
        g = g2.get()
        h = h2.get()
        resu = int(m) * int(g) * int(h)
        return resu
    except:
        global men, dele
        men = tk.Entry(ventana, bg= "orange")
        men.place(x=110, y=550, width=250, height=20)
        men.insert(0,"datos incorrectos, presione RESET e intentelo")
        dele = tk.Entry(ventana, bg= "orange")
        dele.place(x=110, y=570, width=60, height=20)
        dele.insert(0,"de nuevo")
        return

def del_form():
    try:
        global men, dele
        m2.delete(0, 'end')
        g2.delete(0, 'end')
        h2.delete(0, 'end')
        men.delete(0,'end')
        dele.delete(0,'end')
    except:
        print("miau")



#-------------------------------------------------
# entradas de texto
#-------------------------------------------------

m2 = tk.Entry(ventana, bg= "pink")
m2.place(x=50, y=525, width=50, height=20)
g2 = tk.Entry(ventana, bg= "pink")
g2.place(x=50, y=550, width=50, height=20)
h2 = tk.Entry(ventana, bg= "pink")
h2.place(x=50, y=575, width=50, height=20)



#---------------------------------------------------
# botones
#---------------------------------------------------

boton1= tk.Button(ventana, image=ima_emp, command=formula)
boton2= tk.Button(ventana, text = "Forma 1", bg = "yellow")
boton3= tk.Button(ventana, text = "Forma 2", bg = "yellow")
boton4= tk.Button(ventana, image=ima_emp5, command=del_form)

boton1.place(x=0,   y=630, width=153, height=74)
boton2.place(x=386, y=476, width=291, height=112)
boton3.place(x=700, y=476, width=291, height=112)
boton4.place(x=200, y=630, width=153, height=74)


ventana.mainloop()

