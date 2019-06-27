#24. S = 1/1 – 5/2 + 9/4 – 13/8

a = 5.0;
b = 2.0;
s = 1.0;

e = float(input());

while (abs(a/b) > e):
    s+=a/b;
    a+=4;
    b*=(-2);

print(s);
