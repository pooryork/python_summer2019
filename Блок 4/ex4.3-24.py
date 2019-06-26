#24. Дано предложение напечатать все его слова содержащие заданную
#букву

str = input('String: ');
a = input('Letter: ');

n = len(str);
sub_str = '';

for i in range(0,n):
    while(str[i].isalpha() and i<n):
        sub_str+=str[i];
        i+=1;
    if (sub_str.find(a) != -1):
        print(sub_str);
