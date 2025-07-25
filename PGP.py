###
# By: Sotiris Psofakis
# 25/7/2025
# 
# Code used for a demonstration of PGP key generation.
# ###

import random
import math

print("PGP Shared Key Generator:")

x = int(input("1st prime number:"))
y = int(input("2nd prime number:"))

prim = [541, 523, 521, 509, 503, 499, 491, 487, 479, 467, 463, 461, 457, 449, 443, 439, 433, 431, 421, 419, 409, 401, 397, 389, 383, 379, 373, 367, 359, 353, 349, 347, 337, 331, 317, 313, 311, 307, 293, 283, 281, 277, 271, 269, 263, 257, 251, 241, 239, 233, 229, 227, 223, 211, 199, 197, 193, 191, 181, 179, 173, 167, 163, 157, 151, 149, 139, 137, 131, 127, 113, 109, 107, 103, 101, 97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]

n = x * y
n_EulTot = (x-1)*(y-1)

for i in range(len(prim)):
    if ((n_EulTot % prim[i]) != 0):
        publK = prim[i]
        
        print("Public Key: ",n, ", ", publK)
        
        break

x1, y1 = 1, 0 
x2, y2 = 0, 1

a = publK
b = n_EulTot

while b != 0:
    quotient = a // b

    a, b = b, a % b

    x_temp = x1 - quotient * x2
    y_temp = y1 - quotient * y2
    
    x1, y1 = x2, y2
    x2, y2 = x_temp, y_temp

privK = x1 % n_EulTot

print("Private Key: ",n, ", ", privK)
input("\nPress Enter to close the window...")