#Задание 2. Дан одномерный массив чисел.
#24. После максимального из четных элементов вставить 0.

import  sys

a = list(map(int, input('Введите числа: ').split()));
b = [];

i = 0;
max = -sys.maxsize-1;
num = 0;

while (i < len(a)):
    if (a[i] % 2 == 0 and a[i]>max):
        max = a[i];
        num = i;
        i+=1;
    else:
        i += 1;

i=0;
if (max != -sys.maxsize-1):
    while (i != num+1):
        b.append(a[i]);
        i+=1;
    b.append(0);
    while (i<len(a)):
        b.append(a[i]);
        i+=1;
    print(*b);
else:
    print('Четных элементов нет');
