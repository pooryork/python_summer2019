#Во входном файле даны числа x - порядковый номер дня месяца
#и y - порядковый номер месяца. Вывести в файл количество дней,
#оставшихся до конца месяца. Считать, что в феврале 28 дней.

import sys
#sys.stdin = open('input.txt', 'r')
#sys.stdout = open('output.txt', 'w')

day,mon = input().split();
day = int(day);
mon = int(mon);

if (mon == 2):
    print(28 - day);
elif ((mon == 1) or (mon == 3) or (mon == 5) or (mon == 7) or (mon == 8) or (mon == 10) or (mon == 12)):
    print(31 - day);
else:
    print(30 - day);
