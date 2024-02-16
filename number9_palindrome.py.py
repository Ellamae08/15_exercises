number = input("Give a number: ")

def main(word):
    palindrome= ""
    for x in word:
        palindrome = x + palindrome

    return palindrome == word

if main(number):
    print("Yes, given number is a palindrome number.")
else:
    print("No, given number is not a palindrome number.")