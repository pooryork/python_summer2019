#id - случайное пятизначное число
#логин - случайная последовательность из 6 маленьких английских букв
#пароль - случайная последовательность 10 неповторяющихся больших и
#маленьких английских букв и цифр
#Создайте функцию генерации id, функцию генерации логина и функцию
#генерации пароля. С использованием этих трёх функций напишите
#функцию генерации списка из N троек вида (id, логин, пароль), id,
#логины и пароли в тройках не должны повторяться. При этом
#(гласными считаем: aeiou):
#24) Предпоследняя цифра id равна 2. В логине не больше 2 гласных
#букв. Пароль не должен заканчиваться цифрой, но хотя бы одна цифра
# в нём должна присутствовать.

import random
import string

def idGen():
    id =0;
    while (id % 10 != 2):
        id = random.randint(10000, 99999)

    return id;

def loginGen():
    login = '';
    alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'];
    vowels = ['a', 'e', 'i', 'o', 'u'];
    volwesCount = 0;

    for i in range (6):
        letter = random.choice(alphabet);

        if (not(letter in vowels) or volwesCount < 2):
            login+=letter;
            if (letter in vowels):
                volwesCount+=1;
        else:
            while (letter in vowels):
                letter = random.choice(alphabet);
            login+=letter;

    return login;

def passGen():
    password = '';
    alphabet = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'];
    characters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    digit = random.choice(digits);
    digitPlace = random.randint(0,8);

    for i in range (10):

        if (i != digitPlace):
            letter = random.choice(alphabet);
            ifLower = random.randint(0,1);
            if (ifLower == 0):
                password += letter.upper();
            else:
                password += letter;

        else:
            password+=digit;

    return password;

def isUnique(a, a1):
    for i in range(len(a)):
        if (a[i] == a):
            return False;
    return True;

def generate(n):
    a = list();

    for i in range(n):
        a1 = list();
        a1.append(idGen());
        a1.append(loginGen());
        a1.append(passGen());

        if (isUnique(a, a1)):
            a.append(a1);

    return a;

n = int(input('n = '));
a = generate(n);

for i in range (len(a)):
    print(a[i]);
