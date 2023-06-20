import pygame as pg         
from pygame.locals import *   

#Modelo Funcional para python 3 (el problema era el nombre de la imagen si funciona en python 3)

#Inicia Pygame
pg.init() 
nVen=[750,400] 
Win=pg.display.set_mode(nVen) 
pg.display.set_caption("Bola cayendo")

#Funcion para convertir imagen a formato pygame
def Load_Image(sFile, transp=False):
    try: 
        image= pg.image.load(sFile)  
    except pg.error.message:        
            raise SystemExit.message         
    image= image.convert()            
    if transp:
        color= image.get_at((0,0))
        image.set_colorkey(color)
    return image

#Inicia coordenadas de bola
nPos_X= -70
nPos_Y= 15

#Fondo y bola 
Sprite= Load_Image("bola.png",True) #Carga imagen png
fondo= Load_Image("piel.PNG") #Carga imagen fondo 
Triang=Load_Image("triangulo.png")
#Funcion para pintar fondo
def pint_fondo():
    Win.blit(fondo,(000,000))
    return

def tri():
    Win.blit(Triang,(-70,20))
    return
#Funcion para pintar bola
def pint_bola():
    Win.blit(Sprite,(nPos_X,nPos_Y))
    return

#Variables esenciales para el civlo principal
velocidad= 3
lGo= True
atc= True
Clock= pg.time.Clock()

#Ciclo principal
while lGo:
    pint_fondo()
    tri()
    pint_bola()
    ev= pg.event.get()
    for e in ev:
        cKey= pg.key.get_pressed()
        if e.type==pg.QUIT: 
            lGo=False 
        elif cKey[pg.K_j]: 
            nPos_X= -70
            nPos_Y= 15
            atc= True
    
    if atc: 
        nPos_Y += velocidad
        nPos_X += velocidad
        if nPos_Y >= 333:
            atc = False
    
    pg.display.flip()
    Clock.tick(60)
pg.quit()