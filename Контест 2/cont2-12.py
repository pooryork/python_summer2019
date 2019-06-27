#Дано предложение, В нем слова разделены пробелами (символ −
#в предложении
#отсутствует). Верно ли, что число слов в предложении больше трёх?

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input().split();

if (len(s)>3):
    print('yes');
else:
    print('no');
