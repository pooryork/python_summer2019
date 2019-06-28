#24. Дан текст. Верно ли, что в нем есть пять идущих подряд одинаковых
#символов?

str = input('String: ');
n = len(str);

if (n>=5):
    for i in range(0, n-4):
        s = str[i:i+5];
        if (s[0] == s[1] == s[2] == s[3] == s[4]):
            print('Yes');
            break;
    else:
        print('No');
else:
    print('No');
