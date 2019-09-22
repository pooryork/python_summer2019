#24. Удалить из строки слова, содержащие повторяющиеся символы

str = input('String: ');
i=0;
str_ans='';
words = ''.join(x for x in str if x.isalpha() or x == ' ').split();


for sub_str in words[:]:

    sub_set = set(sub_str.lower());

    if not(len(sub_set) == len(sub_str)):
        words.remove(sub_str);

words1 = ' '.join(words);
print(words1);
