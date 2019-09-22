#Для построенного в задании 1 графика измените: цвет линии,
#тип линии и маркеров, шаг выборки данных. Сохраните полученный
#график в файл

import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-2 * np.pi, 2 * np.pi)
y =  1/2*np.cos(2*x+1)
#изменение шага выборки
plt.xticks(np.arange(min(x), max(x)+1, 0.5))
#изменение цвета линии
myhex = '#660099'
plt.plot(x,y,color = myhex)
#изменение типа линиии
plt.plot(x, y, '--xb')
#сохраниение в файл
plt.savefig('pic.png')
plt.show()
