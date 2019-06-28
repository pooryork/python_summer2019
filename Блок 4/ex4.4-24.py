#24. Удалить из строки слова, содержащие повторяющиеся символы

str = input('String: ');
i=0;
str_ans='';
words = ''.join(x for x in str if x.isalpha() or x == ' ').split();


for sub_str in words[:]:

    sub_set = set(sub_str.lower());

    if not(len(sub_set) == len(sub_str)):
        words.remove(sub_str);

    '''i1=0;
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

        i1+=1;'''

    '''if(toDelete==1):
        i1=0;

        while (i1<len(str)-len(sub_str)+1):
            str1=str[i1:i1+len(sub_str)];
            if (str1==sub_str):
                str=str[:i1]+str[i1+len(sub_str):];
                i-=len(sub_str);
                break;
            else:
                i1+=1;

    i+=1;'''

words1 = ''.join(words);
print(words1);
