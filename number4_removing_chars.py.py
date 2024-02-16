def remove_chars(s, n):
    if n < len(s):
        new_string = s[n:]
        return new_string
    else:
        print("The input must be less than the length of the string.")
        return 

user_input = input("Enter a word: ")
removed_chars = int(input("Enter the number of characters to remove: "))

result = remove_chars(user_input, removed_chars)
print("Output:", result)