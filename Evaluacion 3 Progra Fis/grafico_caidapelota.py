import matplotlib.pyplot as plt
import numpy as np
#===========================================================
# Parámetros de la simulación
#============================================================

altura_inicial = 10  
gravedad = 9.8

#============================================================
# Tiempo de simulación
#=============================================================

t_inicio = 0
t_final = np.sqrt(2 * altura_inicial / gravedad) 
t_pasos = 0.01  
t = np.arange(t_inicio, t_final, t_pasos)

#========================================================
# Posición de la pelota en cada instante de tiempo
#========================================================

y = altura_inicial - 0.5 * gravedad * t**2

#================================================================
#graficar el grafico                                            =
#================================================================

plt.plot(t, y)
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura (m)')
plt.title('Simulación de caída de una pelota')
plt.grid(True)
plt.show()
