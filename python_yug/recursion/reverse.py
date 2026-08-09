# Function to check if a number is a palindrome
def is_palindrome(number):
    # Convert the number to a string
    str_number = str(number)
    # Check if the string is equal to its reverse
    return str_number == str_number[::-1]

# Input from the user
num = int(input("Enter a number: "))

# Check and print result
if is_palindrome(num):
    print(f"{num} is a palindrome!")
else:
    print(f"{num} is not a palindrome.")
