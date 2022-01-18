def inverse(a,b):
    if a < b:
        a,b = b,a
    tmp = a
    lst1 = [0, 1]
    lst2 = []
    while a > 0:
        if a//b != 0:
            lst2.append(-1*(a//b))
        a,b = b,a
        b = b % a
        if b == 1:
            break
    for q in range(0, len(lst2)):
        ans = lst2[q] * lst1[q+1] + lst1[q]
        lst1.append(ans)
    if ans<0:
        ans = ans + tmp
    return(ans)

class Affine(object):
   alphabet = dict()
   alph = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
   m = 0
   a = 0
   b = 0

   def __init__(self):
       for i in range(len(self.alph)):
           self.alphabet[self.alph[i]]=i
 
   def input(self):
       self.a = int(input("Введите а: "))
       self.b = int(input("Введите b: "))
       self.m = len(self.alph)

   def decrypt(self):
       ainv = inverse(self.a,self.m)
       str2 = ""
       str1 = input("Введите слово: ")
       for i in str1:
           int1 = (ainv*(self.alphabet[i]+self.m-self.b))%self.m
           str2 += self.alph[int1]
           print(ainv,'* (',self.alphabet[i],'+',self.m,'-',self.b,') = ', int1,' mod', self.m, ' - ', str2[-1])
       print(str2)


affine = Affine()
while True:
    try:
        affine.input()
        affine.decrypt()
    except:
        print("Ошибка")
    if (input('Введите Enter для продолжения\nВведите что-то иное, чтобы завершить')!=""):
        break