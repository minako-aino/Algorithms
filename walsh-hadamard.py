#!/usr/bin/env python
import math
import sys

def scalarMult(a, b):
    ab = 0
    for i in range(0, len(a)):
        ab += int(a[i])*int(b[i])
    return ab

def generate_gray_list(my_val):
    if (my_val <= 0):
      return
    my_list = list()
    my_list.append("0")
    my_list.append("1")
    i = 2
    j = 0
    while(True):
        if i >= 1 << my_val:
            break
        for j in range(i - 1, -1, -1):
            my_list.append(my_list[j])
        for j in range(i):
            my_list[j] = "0" + my_list[j]
        for j in range(i, 2 * i):
            my_list[j] = "1" + my_list[j]
        i = i << 1
    return my_list


verbose = False
fArgPos = -1
for i in range(0, len(sys.argv)):
    if sys.argv[i][0] != '-':
        fArgPos = i
if len(sys.argv) < 2 or '-h' in sys.argv or fArgPos == -1:
    print('Example of usage:\n./walsh-hadamard.py 00010111\n\n-v - verbose output')
    exit()
if '-v' in sys.argv:
    verbose=True
f = list()
for i in sys.argv[fArgPos]:
    f.append(int(i))
deg = math.log(len(f), 2) # degre of the boolean funciton
if deg - int(deg) != 0:
    print('Invalid length of the input vector!')
    exit()

deg = int(deg)
coefs = list() # answer
alphas = generate_gray_list(deg) # 000, 001, 010 ... if degree is 3
alphas.sort()
revAlphas = reversed(alphas)

for alpha in alphas: # len(alphas) == len(f)
    c = 0
    if verbose:
        print('alpha = ', alpha, sep='')
    for i in range(0, len(f)):
        if verbose:
            print('(-1)^(', f[i], ' xor ', scalarMult(alpha, alphas[i])%2, ')', end='', sep='')
            if i != len(f)-1:
                print(' + ', end='')
            else:
                print(' = ', end='')
        c -= pow(-1, f[i]^(scalarMult(alpha, alphas[i])%2))
    if verbose:
        print(c)
    coefs.append(-c)

if verbose:
    print()
print('Walsh-Haddamard coefficients for the boolean function \"', sys.argv[fArgPos],'\":', sep='')
for i in range(0, len(f)):
    print('C', alphas[i], ' = ', coefs[i], sep='')
