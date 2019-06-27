#Дана строка S.
#Подсчитайте количество цифр, которые в ней содержатся.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
ans = 0;

for i in range (0,len(s)):
    if (s[i].isnumeric()):
        ans+=1;

print(ans);
