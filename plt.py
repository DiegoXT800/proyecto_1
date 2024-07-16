import matplotlib.pyplot as plt
import numpy as np 
x = np.linspace(-5,5,100)
y = x**3
plt.plot(x,y , label = "str" ,linewidth = 5)
plt.title("Funcion en python")
plt.legend()
plt.grid()
plt.show()