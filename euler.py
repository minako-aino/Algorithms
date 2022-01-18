from collections import Counter
base = int(input("enter a base "))
power = int(input("enter a power "))
mod = int(input("enter a modulo "))

def inverse(a, b):
    if a < b:
        a,b = b,a
    tmp = a
    lst1 = [0, 1]
    lst2 = []
    while a > 0:
        print(a, " = ", b, " * ", a//b, " + ", a%b)
        if a//b != 0:
            lst2.append(-1*(a//b))
        a,b = b,a
        b = b % a
        if b == 1:
            break
    for q in range(0, len(lst2)):
        ans = lst2[q] * lst1[q+1] + lst1[q]
        lst1.append(ans)
    print("    ",lst2)
    print(lst1)
    if ans<0:
        ans = ans + tmp
    print(ans)
    return ans

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
    return c

np = phi(mod)
if (power > np):
    print(power, "=", np, "*", power//np, "+", power%np)
    ans = pow(base, power%np) % mod
    print(ans)
elif (power == np):
    ans = 1
    print(ans)
else:
    print(pow(base, np - power), mod)
    inverse(pow(base, np - power), mod)
