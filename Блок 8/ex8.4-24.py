#Написать программу, реализующую алгоритм из индивидуального задания
#с использованием list, замерить время выполнения и сравнить с готовой
#реализацией алгоритма из библиотеки NumPy
#10х10, 100х100, 500х500
#24. Создать единичную матрицу.

import numpy as np
import random
import time

#10x10
n = 10;
print('for',n,'elements:');

time1 = time.time();

a = list();
for i in range(n):
    a2 = list();
    for j in range(n):
        if (i == j):
            a2.append(1);
        else:
            a2.append(0);
    a.append(a2);

time2 = time.time();
print ((time2 - time1)*1000, 'ms by list');

time1 = time.time();
a1 = np.eye(n);
time2 = time.time();
print ((time2 - time1)*1000, 'ms by NumPY');
print('');

#100x100
n = 100;
print('for',n,'elements:');

time1 = time.time();

a = list();
for i in range(n):
    a2 = list();
    for j in range(n):
        if (i == j):
            a2.append(1);
        else:
            a2.append(0);
    a.append(a2);

time2 = time.time();
print ((time2 - time1)*1000, 'ms by list');

time1 = time.time();
a1 = np.eye(n);
time2 = time.time();
print ((time2 - time1)*1000, 'ms by NumPY');
print('');

#500x500
n = 500;
print('for',n,'elements:');

time1 = time.time();

a = list();
for i in range(n):
    a2 = list();
    for j in range(n):
        if (i == j):
            a2.append(1);
        else:
            a2.append(0);
    a.append(a2);

time2 = time.time();
print ((time2 - time1)*1000, 'ms by list');

time1 = time.time();
a1 = np.eye(n);
time2 = time.time();
print ((time2 - time1)*1000, 'ms by NumPY');
