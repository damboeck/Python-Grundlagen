import numpy as np
# Plotten mit Python
import matplotlib.pyplot as plt
# Ein Feld der x-Werte erzeugen
x=np.arange(-2,6,0.01)
# y-Werte berechnen
y=x**3-7*x**2+7*x+15
#plotten
plt.plot(x,y)
plt.show()