#Дан год. Вывести на экран на экран название животного, символизирующего
#этот год по восточному календарю (cock, dog, pig, rat, bull, tiger,
#rabbit, dragon, snake, horse, sheep, monkey).

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

a = int(input()) % 12;

if (a == 11):
    print('sheep');
elif (a == 10):
    print('horse');
elif (a == 9):
    print('snake');
elif (a == 8):
    print('dragon');
elif (a == 7):
    print('rabbit');
elif (a == 6):
    print('tiger');
elif (a == 5):
    print('bull');
elif (a == 4):
    print('rat');
elif (a == 3):
    print('pig');
elif (a == 2):
    print('dog');
elif (a == 1):
    print('cock');
else:
    print('monkey');
