#Разработать функцию, которая по заданному n возвращает список n
#первых членов заданной последовательности:
#24.𝑏1 = 2.3, 𝑏2 = −5, 𝑏𝑛 = 𝑏𝑛−2 + 2𝑏𝑛−1.

def f(n):
    a = list();

    a.append(2.3);
    a.append(-5);
    b1 = 2.3;
    b2 = -5;

    for i in range(2,n):
        ans = b1 + 2*b2;
        a.append(ans);
        b1 = b2;
        b2 = ans;

    return a;

n = int(input('n = '));
a = f(n);

print(a);
