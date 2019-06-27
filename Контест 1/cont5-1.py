#Составить программу нахождения среднего арифметического значения
#всех делителей заданного натурального числа N, кратных 3.
#Вывести 0, если нет делителей.
#(Само число и единица включаются в число делителей.)

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

num = int(input());
sum = 0;
c = 0;

for i in range(1, num + 1):
    if ((num % i == 0) and (i % 3 == 0)):
        sum += i;
        c += 1;

if c == 0:
    print(0);
else:
    res = format(sum / c, ".10f");
    print(res);
