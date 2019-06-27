#Дано слово, состоящее из латинских букв. Вывести его "столбиком"
#в обратном порядке, начиная с последней буквы.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
s=s[::-1];
for i in range (0,len(s)):
    print(s[i]);
