#Строка состоит из двух слов. Поменяйте эти слова местами.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input().split();
print(s[1], s[0]);
