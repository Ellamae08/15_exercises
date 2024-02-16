previous_number = 0
print("Printing current and previous number and their sum in a range(10)")

for i in range(0, 10):
    x_sum = previous_number + i
    print("Current Number " + str(i) + "Previous Number " + str(previous_number) + " Sum: " + str(x_sum))
    previous_number = i