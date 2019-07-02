'''24 вариант
1. Сгенерировать матрицу размером 6*2, заполненную целыми числами.
2. Вывести на экран элемент с индексами [4,2].
3. Вывести на экран 3 столбец матрицы.
4. Вывести на экран 1 столбец матрицы в обратном порядке
5. Изменить форму матрицы с 6*2 на 3*4.
6. Умножить каждый элемент матрицы на заданное число
7. Найти минимум в каждой строке
8. Найти максимальный элемент в последнем столбце
9. Дан одномерный массив числовых значений, насчитывающий N
элементов. Найти среднее арифметическое последних подряд идущих
отрицательных элементов
10. Подсчитать сумму нечетных элементов матрицы, расположенных в
шахматном порядке, начиная с элемента [0][1].'''

import numpy as np
import random

print('1. Сгенерировать матрицу размером 6*2, заполненную целыми числами.');
a = np.empty ((2, 6), dtype = int);
for i in range(2):
    for j in range(6):
        a[i, j] = random.randint(-100, 100);
print(a);

print('2. Вывести на экран элемент с индексами [4,2].');
print(a[1][3]);

print('3. Вывести на экран 3 столбец матрицы.');
a0 = list();
for i in range(2):
    a0.append(a[i][3]);
print(a0);

print('4. Вывести на экран 1 столбец матрицы в обратном порядке');
a1 = list();
for i in range(2):
    a1.append(a[i][0]);
a1.reverse();
print(a1);

print('5. Изменить форму матрицы с 6*2 на 3*4.');
a.resize(((3,4)));
print(a);

print('6. Умножить каждый элемент матрицы на заданное число');
k = int(input('k = '));
a*=k;
print(a);

print('7. Найти минимум в каждой строке');
for i in range(3):
    a2 = list();
    for j in range(4):
        a2.append(a[i][j]);
    print('min in ', i, ' string : ', min(a2));

print('8. Найти максимальный элемент в последнем столбце');
for i in range(3):
    a2 = list();
    a2.append(a[i][3]);
    print(a[i][3]);
print('max in 4 column: ', max(a2));

print('9. Дан одномерный массив числовых значений, насчитывающий N элементов. Найти среднее арифметическое последних подряд идущих отрицательных элементов');
n = int(input('n = '));
a3 = list(map(int, input('Введите числа: ').split()));
a4 = list();

a3.reverse();
i=0;
while (i < len(a3) and a3[i] >= 0):
    i+=1;
if (i != len(a3)):
    while (a3[i] < 0):
        a4.append(a3[i]);
        i+=1;

    print(sum(a4)/len(a4));

print('10. Подсчитать сумму нечетных элементов матрицы, расположенных в шахматном порядке, начиная с элемента [0][1].');
s = 0;
print(a);
for i in range(0,3):
    if (i%2==0):
        j1 = 1;
    else:
        j1 = 0;
    for j in range(j1,4, 2):
        if (a[i][j] % 2 != 0):
            s+=a[i][j];
print(s);
