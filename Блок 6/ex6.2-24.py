#Написать функцию, которая изменяет исходный список в
#соответствии с заданием.
#24. удалить кратные 3 из первой половины списка.

def f(a):

    i = 0;
    j = 0;
    n = len(a)//2;
    while (i < len(a)//2 and j<n):
        if (a[i] % 3 == 0):
            a.remove(a[i]);
        else:
            i+=1;
        j+=1;

    return a;

a = list(map(int, input('Введите числа: ').split()));

print(f(a));
