
# SE IMPORTAN LAS LIBRERIAS #

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

gravedad = float(input("ingrese el valor de Gravedad: "))
altura_inicial = float(input("ingrese el valor de la Altura inicial: "))
masa = float(input("ingrese la masa de la pelota: "))

t_inicio = 0
t_pasos = 0.01

t_final = np.sqrt(2 * altura_inicial / gravedad)
t = np.arange(t_inicio, t_final, t_pasos)

y = altura_inicial - 0.5 * gravedad * t**2

fig, ax = plt.subplots()
ax.set_xlim(0, t_final)
ax.set_ylim(0, altura_inicial + 1)
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Altura (m)')
ax.set_title('Simulación de caída de una pelota')
ax.grid(True)

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    t = np.arange(t_inicio, frame, t_pasos)
    y = altura_inicial - 0.5 * gravedad * t**2

    line.set_data(t, y)

    #verifica si la pelota alcanzo la altura minima
    altura_minima = 0.1
    if len(y) > 0 and np.min(y) <= altura_minima:
        ani.event_source.stop()
    
    if frame >= t_final:
        ani.event_source.stop()

    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(t_inicio, t_final, num=200), init_func=init, blit=True, interval = 10)
plt.show()