#Требуется определить, является ли введенная фраза палиндромом.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
a1 = [];

for i in range(len(s)):
    if (s[i].isalpha()):
        a1.append(s[i].lower());

a1 = ''.join(a1);
a = a1[::-1];

if (a1 == a):
  print("Yes");
else:
  print("No");
