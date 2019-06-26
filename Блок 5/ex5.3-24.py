#Задание 3. Дан двумерный массив чисел (матрица)
#24.Выполнить обработку элементов прямоугольной матрицы A,
#имеющей строк N и столбцов M. Дан номер строки L и номер
#столбца K, при помощи которых исходная матрица разбивается на
#четыре части. Найти сумму элементов каждой части.

import numpy as np

n = int(input('n = '));
m = int(input('m = '));

a = np.empty ((n, m), dtype = float);

for i in range(n):
    for j in range(m):
        a[i, j] = int(input());

print(a);

k = int(input('k = '));
l = int(input('l = '));

if(k<=n and l<=m):
    sum = 0;
    #сумма элементов слева сверху
    for i in range(0, k):
        for j in range(0, l):
            sum += a[i, j];

    print('Cумма элементов слева сверху', sum);

    sum = 0;
    #сумма элементов справа сверху
    for i in range(0, k):
        for j in range(l, m):
            sum += a[i, j];

    print('Cумма элементов справа сверху', sum);

    sum = 0;
    #сумма элементов слева снизу
    for i in range(k, n):
        for j in range(0, l):
            sum += a[i, j];

    print('Cумма элементов слева снизу', sum);

    sum = 0;
    #сумма элементов справа снизу
    for i in range(k, n):
        for j in range(l, m):
            sum += a[i, j];

    print('Cумма элементов справа снизу', sum);
else:
    print('Введены неверные значения');
