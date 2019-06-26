#Даны три числа k, m, n. Считая эти числа знаменателями трёх
#простых дробей, найдите общий знаменатель этих дробей.

import math
import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

num1,num2,num3 = map(int, input().split());

n = int(num1 * num2 / math.gcd(num1, num2));
nn = int(n * num3 / math.gcd(n, num3));
print(nn);
