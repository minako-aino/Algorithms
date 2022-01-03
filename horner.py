# Horner's method
# 2021 

import math

e = [1,0,0,1,1,0,1]


def gordon(e,n,X):
	print(e)
	Y = 1
	for i in e:
		temp = Y
		Y = (pow(Y,2))%n
		print("---------------------------------")
		print("I = ", i)
		print("Y = ", temp,"^2 mod", n, "=", Y)
		if i == 1:
				temp2 = Y
				Y = (X*Y)%n
				print("Y = ", X,"*",temp2, "mod", n, "=", Y)


gordon(e,221,22)
