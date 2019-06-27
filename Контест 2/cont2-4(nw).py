#Требуется определить, является ли введенная фраза палиндромом.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
s1 = '';
a1 = '';

for i in range(0,len(s)):
    if (s[i].isalpha() or s[i]==' '):
        a1=s[i].lower();
        s1+=a1;

a = s1[::-1];
a = s1.lower();
if (s1 == a):
  print("Yes");
else:
  print("No");
