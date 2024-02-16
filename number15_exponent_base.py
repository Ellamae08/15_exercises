def exponent(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result

print("base: 2")
print ("exponent: 5")
print("2 raises to the power of 5:", exponent(2, 5)) 
print("\nbase: 5")
print ("exponent: 4")
print("5 raises to the power of 4 is:", exponent(5, 4))  