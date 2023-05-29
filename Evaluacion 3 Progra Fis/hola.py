import tkinter as tk
import pygame as pg

ventana  =  tk.Tk()
ventana.geometry("1000x700")

boton1= tk.Button(ventana, text = "Empieza", width = 13, height= 10  )

boton1.grid(row = 2, column = 0)
boton1.place(x=10, y=10, width=100, height=30)
ventana.mainloop()

