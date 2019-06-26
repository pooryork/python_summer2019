#24. Дан текст. Верно ли, что в нем есть пять идущих подряд одинаковых
#символов?

str = input('String: ');
yes = 0;
n = len(str);

if (n>=5):
    for i in range(0, n-4):
        s = str[i:i+5];
        if (s[0]==s[1] and s[1]==s[2] and s[2]==s[3] and s[3]==s[4]):
            print('Yes');
            yes = 1;
            break;
else:
    print('No');

if (yes == 0):
    print('No');
