numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def checking(nums):
    if len(nums) >= 1:
        return nums[0] == nums[-1]
    else:
        return False

print("Given list: " + str(numbers_x))
print("result is", checking(numbers_x))

print("\nGiven list: " + str(numbers_y))
print("result is", checking(numbers_y))