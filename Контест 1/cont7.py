#Дана последовательность вещественных чисел Ai, в которой
#первый член неотрицателен, а также присутствует хотя бы один член,
#меньший нуля. Пусть n - номер первого отрицательного
#члена последовательности. Тогда вы должны вычислить следующую
#величину: S=A1−A2+...+(−1)n∗An−1

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

num = map(float, input().split());
c = float(0.000000);
z = True;
for i in num:
    if (i < 0):
        break;
    else:
        if (z == True):
            c += i;
            z = False;
        else:
            c -=i;
            z = True;
c = format(c, ".6f");
print(c);
