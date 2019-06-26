#Задана последовательность из N целых чисел.
#Необходимо найти порядковый номер числа с максимальным модулем.
#Если таких чисел несколько, вывести наибольший номер.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

n = int(input());
nums = input().split();
maxmod = abs(int(nums[0]));
modpos = 0;

for i in range(0,n):
    nums[i] = int(nums[i]);

    if (abs(nums[i]) >= maxmod):
        maxmod = abs(nums[i]);
        modpos = i;

print(modpos + 1);
