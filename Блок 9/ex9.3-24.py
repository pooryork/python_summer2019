#Задание 3. Постройте несколько функций на одном графике различными
#цветами. Для построенного графика сделайте сетку и легенду.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-2 * np.pi, 2 * np.pi)

y =  1/2*np.cos(2*x+1)
f = np.cos(2*x+1)*x;
g = -1/5*np.sin(3*x-1)

plt.plot(x, y, color='#000000', label = '0.5cos(2x+1)')

plt.plot(x, f, color='#FF4500', label = 'xcos(2x+1)')

plt.plot(x, g, color='#20B2AA',label = '-0.2sin(3x-1)')

plt.legend()
plt.grid()
plt.show()
