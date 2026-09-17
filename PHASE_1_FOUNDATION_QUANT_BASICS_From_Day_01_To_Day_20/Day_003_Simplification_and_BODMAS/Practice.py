# Day 003 - Simplification & BODMAS Practice

def bodmas_examples():
    # Python already follows BODMAS
    print("--- BODMAS Practice ---")
    # Ex 1: 8 + 6 * 2
    print(f"8 + 6 * 2 = {8 + 6 * 2}") # 20

    # Ex 2: (8 + 6) * 2
    print(f"(8 + 6) * 2 = {(8 + 6) * 2}") # 28

    # Ex 3: 100 / 5 * 2
    print(f"100 / 5 * 2 = {100 / 5 * 2}") # 40.0

    # Ex 4: Complex -  27 - [38 - {46 - (15 - 13*2)}]
    result = 27 - (38 - (46 - (15 - 13*2)))
    print(f"27 - [38 - {{46 - (15 - 13*2)}}] = {result}")

    # Ex 5: Using Formulas
    a, b = 12, 8
    print(f"a^2 - b^2 = {(a+b)*(a-b)} | Direct = {a**2 - b**2}")

def simplification_tricks():
    # Trick 1: Multiply by 5
    n = 126
    print(f"{n} * 5 = {n*10//2}")

    # Trick 2: Square of 35
    n = 35
    first = n // 10
    sq = first * (first+1)
    print(f"{n}^2 = {sq}25")

if __name__ == "__main__":
    bodmas_examples()
    simplification_tricks()