#Дан одномерный массив, элементы которого - целые числа. Также дано
#целое число X. Вставьте в заданный массив элемент X перед первым
#отрицательным элементом.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

n,k = input().split();
n = int(n);
k = int(k);

a = list(map(int, input().split()));

for i in range(len(a)):
    if (a[i] < 0):
        a.insert(i, k);
        break;

print(a);
