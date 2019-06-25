#24. Задана точка в трехмерной цилиндрической системе координат. Найти ее
#координаты в декартовой системе.

import math

r = float(input('r = '));
f = float(input('f (in rad) = '));
z = float(input('z = '));

#x = r*cos(f)
#y = r*sin(f)
#z = z

x = r*math.cos(f);
y = r*math.sin(f);

print('(',x,',',y,',',z, ')');
