#Дано слово. Добавить к нему в начала и конце
#столько звёздочек, сколько букв в этом слове.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

s = input();
s1 = '';

for i in range (0,len(s)):
    s1+='*';

print(s1+s+s1);
