#24. Проверить истинность высказывания: "Цифры данного трехзначного
#числа
#являются одинаковыми"

num = abs(int(input('num = ')));

a = num % 10;
b = num // 10 % 10;
c = num // 100;

if (a == b == c):
    print("Yes");
else:
    print("No");
