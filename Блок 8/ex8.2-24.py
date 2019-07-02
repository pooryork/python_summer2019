#24. Выполнить обработку элементов прямоугольной матрицы ,
#имеющей n строк и m столбцов. Найти наименьшее значение среди
#средних значений для каждой строки матрицы.

import numpy as np
import random

def mean(a):
    return (sum(a)/len(a));

n = int(input('n = '));
m = int(input('m = '));

a = np.empty ((n, m), dtype = int);
for i in range(n):
    for j in range(m):
        a[i, j] = random.randint(-100, 100);

a1 = list();
print(a);

for i in range(n):
    print('mean in', i, '(',a[i],')', 'string:', mean(a[i]));
    a1.append(mean(a[i]));

print(min(a1));
