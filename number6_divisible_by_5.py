numbers = [10, 20, 33, 46, 55]

print("Given list is " + str(numbers))
print("Divisible by 5")
for num in numbers:
    if num % 5 == 0:
        print(num)