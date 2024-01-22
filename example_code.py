import math
def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2
 
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True

c = 0
 
for n in range(1,100000):
    x = is_prime(n)
    c += x
print("Total prime numbers in range :", c)