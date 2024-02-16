list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

odd_nums_list1 = []
for num in list1:
    if num % 2 != 0:
        odd_nums_list1.append(num)

even_nums_list2 = []
for num in list2:
    if num % 2 == 0:
        even_nums_list2.append(num)

result = odd_nums_list1 + even_nums_list2
print("Result list:", result)