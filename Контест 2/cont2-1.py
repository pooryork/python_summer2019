#Дана строка S, состоящая из слов, разделенных пробелами.
#Найдите в строке S слово максимальной длины.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
print(max(s.split(), key=len));
