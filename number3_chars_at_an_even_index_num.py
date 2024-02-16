user_input = input("please input a word to determine if it is a pynative: ")
print("orignal string is " + user_input)

def even_index_chars(user_input):
    even_index_chars = [user_input[i] for i in range(len(user_input)) if i % 2 == 0]
    return even_index_chars

input_string = "example"
result = even_index_chars(input_string)
print(result)

print("Characters at even index positions:", even_index_chars)