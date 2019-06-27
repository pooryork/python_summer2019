#Дана строка S, состоящая из слов, разделенных пробелами.
#Выведите все слова из S, которые начинаются и оканчиваются
#одной буквой.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
str = s.split();

for i in range(0,len(str)):
    buf_str = str[i];

    if (buf_str[0]==buf_str[len(buf_str)-1]):
        print(buf_str);
