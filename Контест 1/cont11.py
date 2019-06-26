#Дано натуральное число N. Определить, можно ли данное число
#представить в виде произведения двух простых чисел.

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

n = int(input());
nn = n // 2 + 1;

for i in range(2, nn):
    if ((n % i == 0) and isSimple(i) and isSimple(n // i)):
        print('Yes');
        n = -1;
        break;
if (n != -1):
    print('No');
