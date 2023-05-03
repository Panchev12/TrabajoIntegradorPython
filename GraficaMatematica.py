import matplotlib.pyplot as plt
import numpy as np
import math as mt

def move_spines():
    """Esta funcion divide pone al eje y en el valor 
    0 de x para dividir claramente los valores positivos y
    negativos."""
    fix, ax = plt.subplots()
    for spine in ["left", "bottom"]:
        ax.spines[spine].set_position("zero")
    
    for spine in ["right", "top"]:
        ax.spines[spine].set_color("none")
    
    return ax

y = 10
x = np.linspace(-2, 6, num=30)

y = 10
x = np.linspace(-2, 6, num=30)

ax = move_spines()
ax.grid()
ax.plot(x,x + 3)
plt.title(r"Grafico de $f(x)=\sqrt{x + 2}$")
plt.ylabel('f(x)')
plt.xlabel('x')
plt.show()
