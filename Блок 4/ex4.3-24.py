#24. Дано предложение напечатать все его слова содержащие заданную
#букву

str = input('String: ');
a = input('Letter: ');


n = len(str);
sub_str = '';
i=0;

while (i<n):
    while(i<n and str[i].isalpha()):
        sub_str+=str[i];
        i+=1;

    #if (sub_str.find(a.lower()) != -1 or sub_str.find(a.upper()) != -1):
    if (a.lower() in sub_str.lower()):

        print(sub_str);

    sub_str = '';
    i+=1;
