#24. Удалить из строки слова, содержащие повторяющиеся символы

str = input('String: ');
i=0;
str_ans='';

while (i<len(str)):
    sub_str = '';
    while(i<len(str) and str[i].isalpha()):
        sub_str+=str[i];
        i+=1;

    print('sub_str', sub_str);

    i1=0;
    j1=0;
    n = len(sub_str);
    toDelete = 0;

    while(i1<n):
        j1=i1+1;

        while(j1<n):
            print (sub_str[i1], ' ', sub_str[j1]);
            if (sub_str[i1] == sub_str[j1]):
                toDelete = 1;
                break;
            else:
                j1+=1;

        i1+=1;

    print(toDelete);

    if(toDelete==1):
        str1='';
        if (str[:i] != ''):
            str1+=str[:i];
            print(str1);
        if (str[i+len(sub_str):] != ''):
            str1+=str[i+len(sub_str)];
            print(str1);
        print(str1);

    i+=1;



print(str);
