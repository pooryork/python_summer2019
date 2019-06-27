#Буквы на четных местах в обратном порядке
#Дано слово s1. Получить слово s2, образованное четным
#буквами слова s1, записанными в обратном порядке.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
i = 1;
n = len(s);
ans = '';

while (i<n):
    ans+=s[i];
    i+=2;

print(ans[::-1]);
