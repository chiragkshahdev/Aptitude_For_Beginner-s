import math 

def hcf(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcm_of_list(arr):
    res = arr[0]
    for n in arr[1:]:
        res = lcm(res, n)
    return res

# Example
a, b = 24, 36
print(f"Numbers: {a}, {b}")
print(f"HCF: {hcf(a, b)}")
print(f"LCM: {lcm(a, b)}")
print(f"Formula Check a*b == HCF*LCM : {a * b == hcf(a, b) * lcm(a, b)}")

# Smallest 4-digit divisible by 5,10,15,20
l = lcm_of_list([5, 10, 15, 20])
smallest = ((1000 + l - 1)//l) * l
print(f"Smallest 4-digit divisible by { [5, 10, 15, 20]} is {smallest}")

# Remainder Trick
print(f"Greatest no dividing 403,465 leaving rem 5 is HCF of 398,460 = {hcf(398, 460)}")