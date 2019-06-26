#24. Удалить из строки слова, содержащие повторяющиеся символы

str = input('String: ');
i=0;
str_ans='';

while (i<len(str)):
    sub_str = '';
    while(i<len(str) and str[i].isalpha()):
        sub_str+=str[i];
        i+=1;

    i1=0;
    j1=0;
    n = len(sub_str);
    toDelete = 0;

    while(i1<n):
        j1=i1+1;

        while(j1<n):
            if (sub_str[i1] == sub_str[j1]):
                toDelete = 1;
                break;
            else:
                j1+=1;

        i1+=1;

    if(toDelete==1):
        i1=0;

        while (i1<len(str)-len(sub_str)+1):
            str1=str[i1:i1+len(sub_str)];
            if (str1==sub_str):
                str=str[:i1]+str[i1+len(sub_str):];
                i-=len(sub_str);
                break;
            else:
                i1+=1;

    i+=1;

print(str);
