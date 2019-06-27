#Буквы на нечетных местах
#Дано слово s1. Получить слово s2, образованное нечетными
#буквами слова s1.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
i = 0;
n = len(s);
ans = '';

while (i<n):
    ans+=s[i];
    i+=2;

print(ans);
