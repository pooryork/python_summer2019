# Постройте графики следующих функций, используя шаг 0.1 по
#абсциссе:
#24. 1/2cos(2x+1) на отрезке [-2π, 2π];

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-2 * np.pi, 2 * np.pi)
y =  1/2*np.cos(2*x+1)
plt.plot(x, y)
plt.xticks(np.arange(min(x), max(x)+1, 0.1))
plt.show()
