import pygame as PG, random as RA
from pygame.locals import *
#Cambio en codigo a ver si funcionana 
#Constantes globales
nRES = (1000,700); nTW_X = nTH_Y = 32 ; lOK = True 

#Inicia pygame
def PyGame_Init():
    PG.init()
    PG.display.set_caption('Energia potencial gravitacional')
    return PG.display.set_mode(nRES)

#Convierte imagenes a formato pygame
def Load_Image(sFile,transp = False):
    try: image = PG.image.load(sFile)
    except PG.error,message:
            raise SystemExit,message
    image = image.convert()
    if transp:
        color = image.get_at((0,0))
        image.set_colorkey(color,RLEACCEL)
    return image 

#Inicia tiles o baldosas
def Get_Tiles(nMW_X,nMH_Y,tRng):      
    return [[ RA.randint(tRng[0],tRng[1]) for i in range(0,nMW_X/nTW_X)] for i in range(0,nMH_Y/nTH_Y)]

#Inicia superficie del mega mapa
def Get_Surface(nAncho_X,nAlto_Y):
    return PG.Surface((nAncho_X,nAlto_Y))

#Inicia lista de sprites
def Img_Init():
    aImg = []
    aImg.append(Load_Image('T00.png',False )) 
    aImg.append(Load_Image('T02.png',False ))
    aImg.append(Load_Image('T07.png',False )) 
    aImg.append(Load_Image('BKG2.png',False ))
    return aImg

#Crea mapa
def Make_Mapa(sMem,aTiles,tCF):
    nPx = nPy = 0
    for f in range(0,tCF[1]/nTH_Y):
        for c in range(0,tCF[0]/nTW_X):
            if aTiles[f][c] == 0: 
                sMem.blit(aSprt[0],(nPx,nPy)); nPx += nTW_X
            if aTiles[f][c] == 1: 
                sMem.blit(aSprt[1],(nPx,nPy)); nPx += nTW_X
            if aTiles[f][c] == 2: 
                sMem.blit(aSprt[2],(nPx,nPy)); nPx += nTW_X
        nPx = 0; nPy += nTH_Y
    return

#Pinta el display main
def Pinta_Pantalla():
    sPanta.blit(aSprt[3],(0,0))
    return


#Pinta mapas
def Pinta_Mapas():
    sPanta.blit(sMap_1.subsurface((0,0,849,467)),(381,0))
    sPanta.blit(sMap_2.subsurface((0,0,372,900)),(0,-100))
    sPanta.blit(sMap_3.subsurface((0,0,849,322)),(381,476))
    sPanta.blit(sMap_4.subsurface((0,0,203,99)),(0,0))
    sPanta.blit(sMap_5.subsurface((0,0,153,74)),(0,630))
    sPanta.blit(sMap_6.subsurface((0,0,372,178)),(0,430))
    sPanta.blit(sMap_7.subsurface((0,0,255,93)),(581,180))
    sPanta.blit(sMap_8.subsurface((0,0,619,112)),(381,476))
    return

#Display Main
sPanta = PyGame_Init(); 

#Sprites
aSprt = Img_Init() 

#Mapas
sInfo  = Get_Surface(0345,0230); 
sMap_1 = Get_Surface(3840,1920); 
sMap_2 = Get_Surface(1920,3200); 
sMap_3 = Get_Surface(1920,1920);
sMap_4 = Get_Surface(1000,1000);
sMap_5 = Get_Surface(1000,1000);
sMap_6 = Get_Surface(1000,1000);
sMap_7 = Get_Surface(1000,1000);
sMap_8 = Get_Surface(1000,1000);
#Botones
Img = Load_Image('Formula.png',False)
Img2 = Load_Image('start.png',False)
Img3 = Load_Image('Valores.png',False)
Img4 = Load_Image('Simu.png',False)
Img5 = Load_Image('Formas.png',False)
sMap_4.blit(Img,(0,0))
sMap_5.blit(Img2,(0,0))
sMap_6.blit(Img3,(0,0))
sMap_7.blit(Img4,(0,0))
sMap_8.blit(Img5,(0,0))

aMapTi_1 = Get_Tiles(3840,1920,(0,0)); Make_Mapa(sMap_1,aMapTi_1,(3840,1920)) 
aMapTi_2 = Get_Tiles(1920,3200,(1,1)); Make_Mapa(sMap_2,aMapTi_2,(1920,3200)) 
aMapTi_3 = Get_Tiles(1920,1920,(2,2)); Make_Mapa(sMap_3,aMapTi_3,(1920,1920)) 

aClk = [PG.time.Clock(),PG.time.Clock()] 

#While principal
while lOK:
    cKey = PG.key.get_pressed()
    if cKey[PG.K_ESCAPE]: 
        lOK = False
    ev = PG.event.get()
    for e in ev:
        if e.type == QUIT: 
            lOK = False
    Pinta_Pantalla()
    Pinta_Mapas()
    PG.display.flip()
    aClk[0].tick(100)
PG.quit