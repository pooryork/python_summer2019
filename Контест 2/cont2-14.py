#Дана строка, в которой имеются цифры. Найти их сумму.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
ans = 0;

for i in range(0,len(s)):
    if (s[i].isnumeric()):
        a = int(s[i]);
        ans+=a;

print(ans);
