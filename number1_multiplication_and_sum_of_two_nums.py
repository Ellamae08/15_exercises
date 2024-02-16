def multiply_or_add(number1, number2):
    if number1 * number2 <= 1000:
        return number1 * number2
    else:
        return number1 + number2

result = multiply_or_add(20, 30)
print("The result is", result)

result = multiply_or_add(40, 30)
print("The result is", result)