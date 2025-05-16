import numpy as np
import matplotlib.pyplot as plt

fs= 100
t= np.linspace(0, 2, 2*fs)
print(t)
print(len(t))

acel = np.zeros_like(t)
#print(acel)
#print(t)

acel[:51] = 20
#print(acel)


vel=np.cumsum(acel) / fs
altura = np.cumsum(vel) / fs
#print(vel)

plt.plot(t, vel)
plt.tittle('Aluta vs Tiempo')
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura (m)')
plt.show()

