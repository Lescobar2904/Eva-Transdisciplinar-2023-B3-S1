#Codigo Unido
import tkinter as tk
import pygame as pg
from PIL import ImageTk,Image      
from pygame.locals import *   

#------------------------------------------------
# inicia pygame
#------------------------------------------------
#Funcion para convertir imagen a formato pygame
def Load_Image(sFile, superficie,transp=False):
    try: 
        image= pg.image.load(sFile)  
    except pg.error.message:        
            raise SystemExit.message         
    image= image.convert(superficie)            
    if transp:
        color= image.get_at((0,0))
        image.set_colorkey(color)
    return image

pg.init()
ancho = 610
alto = 460
superficie = pg.Surface((ancho,alto))
pg.display.set_caption("Bola cayendo")
#Fondo y bola 
Sprite= Load_Image("bola1.png",superficie,True) #Carga imagen png

#------------------------------------------------
# inicia tkinter
#------------------------------------------------

ventana  =  tk.Tk()
ventana.geometry("1000x700")
ventana.resizable(0,0)

#------------------------------------------------
# carga de imagenes
#------------------------------------------------
ima_emp  = tk.PhotoImage(file="start.png")
ima_emp2 = tk.PhotoImage(file="Formula.png")
ima_emp3 = tk.PhotoImage(file="Valores.png")
ima_emp4 = tk.PhotoImage(file="fpulentox.png")
ima_emp5 = tk.PhotoImage(file="Reset.png")

#------------------------------------------------
# interfaz
#------------------------------------------------

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
etiqueta = tk.Label(ventana)

#------------------------------------------------
# funcion de RESET
#------------------------------------------------

def del_form():
    try:
        global men, dele
        m2.delete(0, 'end')
        g2.delete(0, 'end')
        h2.delete(0, 'end')
        dele.destroy()
        men.destroy()
    except:
        print("error")
    return

#-------------------------------------------------
# entradas de texto
#-------------------------------------------------

m2 = tk.Entry(ventana, bg= "pink")
m2.place(x=50, y=525, width=50, height=20)
h2 = tk.Entry(ventana, bg= "pink")
h2.place(x=50, y=550, width=50, height=20)
g2 = tk.Entry(ventana, bg= "pink")
g2.place(x=50, y=575, width=50, height=20)
etiqueta.place(x=388, y=0, width=ancho, height=alto)

#---------------------------------------------------
# botones
#---------------------------------------------------
boton3= tk.Button(ventana, text = "Forma 2", bg = "yellow")
boton4= tk.Button(ventana, image=ima_emp5, command=del_form)
boton3.place(x=700, y=476, width=291, height=112)
boton4.place(x=200, y=630, width=153, height=74)

def update_image1(): 
    global nPos_X, nPos_Y
    superficie.fill((255, 205, 197))
    nPos_X= int(480/2)
    nPos_Y= 0
    superficie.blit(Sprite,(nPos_X,nPos_Y))
    datos_bytes_pyga = pg.image.tostring(superficie, "RGB")
    imagen = Image.frombytes('RGB',  superficie.get_size(), datos_bytes_pyga)
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta.config(image=imagen_tk)
    etiqueta.image= imagen_tk
    return

def update_image():
    global nPos_X, nPos_Y
    superficie.fill((255, 205, 197))
    velocidad= grav
    superficie.blit(Sprite,(nPos_X,nPos_Y))
    if nPos_Y >= 390:
        velocidad=0
    nPos_Y += velocidad
    datos_bytes_pyga = pg.image.tostring(superficie, "RGB")
    imagen = Image.frombytes('RGB',  superficie.get_size(), datos_bytes_pyga)
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta.config(image=imagen_tk)
    etiqueta.image= imagen_tk
    return

def update():
    update_image()
    ventana.after(1000//60, update)
    return

#------------------------------------------------
# funcion de formula
#------------------------------------------------
def formula():
    global grav
    g = h2.get()
    grav= float(g)
    update()
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

boton1= tk.Button(ventana, image=ima_emp, command=formula)
boton1.place(x=0,   y=630, width=153, height=74)
boton2= tk.Button(ventana, text = "Forma 1", bg = "yellow", command=update_image1)
boton2.place(x=386, y=476, width=291, height=112)
boton3= tk.Button(ventana, text = "Forma 2", bg = "yellow")
boton3.place(x=700, y=476, width=291, height=112)
ventana.mainloop()