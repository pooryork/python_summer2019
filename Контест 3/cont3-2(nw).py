#Дан одномерный массив, элементы которого - целые числа.
#Удалите из него все элементы с номера K1 по номер K2 включительно
#(K1 и K2 заданы). Элементы массива нумеруются с единицы.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

n,k1,k2 = input().split();
n = int(n);
k1 = int(k1);
k2 = int(k2);

k1-=1;
k2-=1;

a = list(map(int, input().split()));

while (k1 <= k2):
    a.remove(a[k1]);
    k2-=1;

ans = '';
for i in range (len(a)):
    ans+=str(a[i]);
    ans+=' ';

print(ans);
