# Find inverse element for mod
# March 2021

a = int(input("enter number "))
b = int(input("enter a modulo "))

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

inverse(a, b)
