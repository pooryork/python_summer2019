#Дано предложение. Вывести его в обратном порядке слов.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input().split();
ans = '';
n = len(s)-1;

while (n>=0):
    ans+=s[n];
    n-=1;
    ans+=' ';

print(ans[:len(ans)-1]);
