#Дано натуральное число N.
#Необходимо разложить его на простые множители.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

num = int(input());
n = num;
i = 2;
while (i <= num):
    while (n % i == 0):
        print(i, end=' ');
        n = n // i;
    i += 1;
