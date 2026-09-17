# Day 01 - Number System Practice in Python - By Chirag

# Q1. Check divisibility by 3
def is_divisible_by_3(n):
    digit_sum = sum(int(d) for d in str(n))
    return digit_sum % 3 == 0

print("12345 divisible by 3?", is_divisible_by_3(12345)) # True

# Q2. Find Prime Numbers between 1 to 50
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primes = [i for i in range(1, 51) if is_prime(i)]
print("Primes 1 to 50:", primes)

# Q3. Unit digit of 2^100
def unit_digit_of_power(base, power):
    cycle = [2, 4, 8, 6] # cycle of 2
    # for base 2
    rem = power % 4
    if rem == 0:
        return cycle[3]
    return cycle[rem-1]

print("Unit digit of 2^100:", unit_digit_of_power(2, 100)) # 6

# Q4. Sum of first n natural numbers
def sum_n(n):
    return n*(n+1)//2

print("Sum 1 to 100:", sum_n(100)) # 5050

# Q5. HCF of two numbers (Day 2 ka trailer)
import math
print("HCF of 12 and 18:", math.gcd(12, 18))