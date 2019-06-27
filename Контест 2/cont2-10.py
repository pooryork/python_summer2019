#Дан символ c и натуральное число n.
#Составить слово из n символов c идущих подряд.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
n = int(input());
ans = '';

for i in range (0,n):
    ans+=s;

print(ans);
