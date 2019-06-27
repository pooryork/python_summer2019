#Дана строка, в которой имеются цифры. Найти максимальную цифру.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
max = -sys.maxsize-1;

for i in range(0,len(s)):
    if (s[i].isnumeric()):
        a = int(s[i]);
        if(a>max):
            max = a;

print(max);
