###
# By: Sotiris Psofakis
# 25/7/2025
# 
# Code used to demonstrate Diffie–Hellman key exchange encryption.
# ###

import random

print("Diffie–Hellman key exchange:")

x = int(input("1st prime number:"))
y = int(input("2nd prime number:"))

a = random.randint(100000,999999)
b = random.randint(100000,999999)

A = ((x)**a)%y 
B = ((x)**b)%y 

S1 = ((B)**a)%y 
S2 = ((A)**b)%y 

print("\nPublic Information pre-agreed :          (x = ", x, ",y = ", y,")")
print("\nSecret Values :                          (a = ", a, ",b = ", b,")")
print("\nExcanged Values  (A, B) = ((x)^(a,b)%y : (A = ", A, ",B = ", B,")")
print("\nSecret Key          S = ((B,A)^a)%y :    (S = ",S1, ",S = ",S2,")")

input("\nPress Enter to close the window...")