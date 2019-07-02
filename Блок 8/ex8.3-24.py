#24. Дан вектор x и матрица А. Умножить все нечетные столбцы матрицы
#А на вектор x в обратном порядке. Результат записать в новую матрицу
#и найти сумму ее элементов.

import numpy as np
import random

n = int(input('n = '));
m = int(input('m = '));

a = np.empty ((n, m), dtype = int);
for i in range(n):
    for j in range(m):
        a[i, j] = random.randint(-100, 100);

print(a);

x = list(map(float, input('Введите числа: ').split()));
x.reverse();

if(len(x) == n):
    a1 = np.empty ((n, m//2), dtype = int);

    for i in range(0, n):
        a_buf = list();

        for j in range(1, m, 2):
            a_buf.append(a[i,j]);
        a1[i] = a_buf;

    for i in range(m//2):
        for j in range(n):
            a1[j][i]*=x[j];

    print(a1);
else:

        print('Невозможно выполнить операцию');
