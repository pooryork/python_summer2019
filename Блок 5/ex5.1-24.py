#Дан одномерный массив чисел. Найти/определить
#24. максимальный из элементов, имеющих четный индекс.

import  sys

a = list(map(int, input('Введите числа: ').split()));

i = 0;
max = -sys.maxsize-1;

while (i < len(a)):
    if (i % 2 == 0 and a[i]>max):
        max = a[i];
        i+=1;
    else:
        i += 1;

print(max);
