#Дан одномерный массив, элементы которого - целые числа.
#Удалите из него все максимальные элементы.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

n = int(input());
a = list(map(int, input().split()));

maxval = max(a);

while(a.index(maxval) != -1):
    a.remove(maxval);

print(a);
