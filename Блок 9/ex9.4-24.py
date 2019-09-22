# Задание 4.Постройте закрашенную контурную диаграмму и трёхмерный график  для  следующих  функций  двух  переменных,
# определённых  в прямоугольной  области  x ∈[−3;  3], y ∈[−3;  3]. Построенные  графики сохраните в файлы с
# расширением png.
# z = 2sin(xy),

import numpy as np
import matplotlib.pyplot as plt
import pylab
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-3, 3, 0.1)
y = np.arange(-3, 3, 0.1)
xgrid, ygrid = np.meshgrid(x,y)
zgrid = 2*np.sin(xgrid*ygrid)
plt.contourf(xgrid,ygrid,zgrid)
fig = pylab.figure()
axes = Axes3D(fig)
axes.plot_surface(xgrid,ygrid,zgrid,rstride=1, cstride=1, color='#FFF000')
plt.savefig('pic1.png')
plt.show()
