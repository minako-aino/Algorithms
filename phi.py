from collections import Counter
num = int(input("enter a number "))

def phi(n):
    c = 1
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    count = Counter(Ans)
    for key, value in count.items():
        b = pow(key, value) - pow(key, value - 1)
        print(key, "^", value, "-", key, "^", value - 1, "=", pow(key, value), "-", pow(key, value - 1), "=", b)
        c *= b
    print(c)
    return Ans

phi(num)