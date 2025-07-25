###
# By: Sotiris Psofakis
# 25/7/2025
# 
# Code used to Generate random prime numbers for PGP encryption.
# ###

import random
import math

print("Generating a random 3-digit prime number:")

while True:
    while True:
        generated_prime = random.randint(100, 999)
        
        is_num_prime = True
        
        if generated_prime % 2 == 0:
            is_num_prime = False
        else:
            divisor = 3
            limit = int(math.sqrt(generated_prime))
            while divisor <= limit:
                if generated_prime % divisor == 0:
                    is_num_prime = False
                    break
                divisor += 2

        if is_num_prime:
            break

    print(f"Generated prime number: {generated_prime}")
    input("\nPress Enter to generate new number...")