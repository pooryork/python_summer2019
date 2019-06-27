#Дано натуральное число N.
#Определить, является ли оно квадратом простого числа.

import math
import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

def isSimple(x):
    if (x > 2):
        for k in range(2, x):
            if (x % k == 0):
                return False;
    if (x == 1):
        return False;

    return True;

num = int(input());

i = math.sqrt(num);
if (isSimple(int(i)) and (i - math.sqrt(num) // 1) == 0):
    print('Yes');
else:
    print('No');
