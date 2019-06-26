#Дано целое трехзначное число.
#Определить есть ли среди его цифр одинаковые.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

num = int(input());
x = num % 10;
y = num // 10 % 10;
z = num // 100;

if ((x == y) or (x == z) or (y == z)):
    print('YES');
else:
    print('NO');
