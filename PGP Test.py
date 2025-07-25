###
# By: Sotiris Psofakis
# 25/7/2025
# 
# Code used to demonstrate PGP encryption.
# ###

print("PGP Key Encryption:")

c = int(input("Encript code: "))
n = int(input("Product of prime numbers: "))
pu = int(input("Public Key: "))

e = (c ** pu)%n

print("Encoded code: ",e)

pr = int(input("Private Kay: "))

d = (e ** pr)%n

print("Decoded code: ",d)

input("\nPress Enter to close the window...")