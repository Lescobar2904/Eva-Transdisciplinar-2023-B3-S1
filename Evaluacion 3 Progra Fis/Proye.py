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
ima_emp6 = tk.PhotoImage(file="AgreVal.png")
ima_emp7 = tk.PhotoImage(file="Forma10.png")
ima_emp8 = tk.PhotoImage(file="Forma20.png")

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
g2 = tk.Entry(ventana, bg= "pink")
g2.place(x=50, y=550, width=50, height=20)
h2 = tk.Entry(ventana, bg= "pink")
h2.place(x=50, y=575, width=50, height=20)
etiqueta.place(x=388, y=0, width=ancho, height=alto)


def Forma1(): 
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
    ventana.after_cancel(pgven)
    return
def Forma2(): 
    global nPos_X, nPos_Y
    superficie.fill((255, 205, 197))
    nPos_X= int(480/2)
    nPos_Y= 200
    superficie.blit(Sprite,(nPos_X,nPos_Y))
    datos_bytes_pyga = pg.image.tostring(superficie, "RGB")
    imagen = Image.frombytes('RGB',  superficie.get_size(), datos_bytes_pyga)
    imagen_tk = ImageTk.PhotoImage(imagen)
    etiqueta.config(image=imagen_tk)
    etiqueta.image= imagen_tk
    ventana.after_cancel(pgven)
    return
#------------------------------------------------
# funcion de formula
#------------------------------------------------
def formula():
    global grav, resul
    try:
        m = m2.get()
        g = g2.get()
        h = h2.get()
        masa = float(m)
        grav = float(g)
        altu = float(h)
        resul = masa * grav * altu
        return resul, grav
    except:
        global men, dele
        men = tk.Entry(ventana, bg= "orange")
        men.place(x=110, y=550, width=250, height=20)
        men.insert(0,"datos incorrectos, presione RESET e intentelo")
        dele = tk.Entry(ventana, bg= "orange")
        dele.place(x=110, y=570, width=60, height=20)
        dele.insert(0,"de nuevo")
    return

def update_image():
    global nPos_X, nPos_Y
    superficie.fill((255, 205, 197))
    velocidad= grav
    superficie.blit(Sprite,(nPos_X,nPos_Y))
    Text=str(resul)
    black = (0, 0, 0)
    rose = (255, 205, 197)
    font = pg.font.Font("freesansbold.ttf", 12)
    text = font.render("La E.P.G del objeto es la siguiente: ", True, black, rose)
    text2 = font.render(Text, True, black, rose)  
    text3 = font.render("Joule", True, black, rose)
    textRect = text.get_rect()
    textRec2 = text2.get_rect()
    textRec3 = text3.get_rect()
    textRect.center = (110, 30)
    textRec2.center = (110, 50)
    textRec3.center = (161, 50)
    superficie.blit(text, textRect)
    superficie.blit(text2, textRec2)
    superficie.blit(text3, textRec3)
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
    global pgven
    update_image()
    pgven=ventana.after(1000//60, update)
    return

#---------------------------------------------------
# botones
#---------------------------------------------------
boton1= tk.Button(ventana, image=ima_emp, command=update)
boton1.place(x=0,   y=630, width=153, height=74)
boton2= tk.Button(ventana, image=ima_emp7, command=Forma1)
boton2.place(x=386, y=476, width=291, height=112)
boton3= tk.Button(ventana, image=ima_emp8, command=Forma2)
boton3.place(x=700, y=476, width=291, height=112)
boton4= tk.Button(ventana, image=ima_emp5, command=del_form)
boton4.place(x=200, y=630, width=153, height=74)
boton5= tk.Button(ventana, image=ima_emp6, command=formula)
boton5.place(x=253, y=564, width=100, height=44)

ventana.mainloop()