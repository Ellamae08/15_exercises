def digits(num):
    num_str = str(num)
    digits_list = []
    for digit_char in num_str:
        digit = int(digit_char)
        digits_list.append(digit)

    reversed_digits = digits_list[::-1]
    return reversed_digits

try:
    number = int(input("Enter an integer: "))
    reversed_digits = digits(number)
    print("Digits in reverse order:", reversed_digits)
except ValueError:
    print("Please enter a valid integer.")