#Дано целое четырехзначное число. Выяснить, является ли оно
#палиндромом, то есть таким числом, десятичная
#запись которого читается одинаково слева направо и справа налево.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

num = int(input());
a = num % 10;
num//=10;
b = num % 10;
num//=10;
c = num % 10;
d=num//10;


if (a == d and b == c):
    print('YES');
else:
    print('NO');
