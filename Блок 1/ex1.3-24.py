#24. Проверить истинность высказывания: "Цифры данного трехзначного числа
#являются одинаковыми"

num = int(input('num = '));

a = num % 10;
b = num // 10 % 10;
c = num // 100;

if (a == b and b == c):
    print("Yes");
else:
    print("No");
