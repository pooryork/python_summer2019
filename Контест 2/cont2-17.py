#Даны две строки. Для каждого буквы первой строки определить,
#входит ли она во вторую строку.

import sys
import string
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
s1 = input();
ans = '';

for i in range(0,len(s)):
    if (s[i] in s1):
        ans+='True ';
    else:
        ans+='False ';

print(ans[:len(ans)-1]);
