# Program to check if a number is a palindrome using multiple methods

# Method 1: Using String Comparison
def is_palindrome_string(number):
    """
    Converts the number to a string and checks if it is equal to its reverse.
    """
    str_number = str(number)
    return str_number == str_number[::-1]

# Method 2: Using a Loop (Reverse the Number Digit by Digit)
def is_palindrome_reverse(number):
    """
    Reverses the number by extracting digits one by one and comparing the reversed number
    to the original.
    """
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10  # Extract the last digit
        reversed_number = reversed_number * 10 + digit  # Build the reversed number
        number = number // 10  # Remove the last digit

    return original_number == reversed_number

# Method 3: Using Recursion
def is_palindrome_recursive(number):
    """
    Uses recursion to reverse the number and compares it to the original.
    """
    def reverse(num, rev=0):
        if num == 0:
            return rev  # Base case: return the reversed number
        return reverse(num // 10, rev * 10 + num % 10)  # Recursive step

    return number == reverse(number)

# Method 4: Using String Iteration
def is_palindrome_iter(number):
    """
    Iterates through the first half of the string representation of the number
    and compares each character with its counterpart from the end.
    """
    str_number = str(number)
    for i in range(len(str_number) // 2):
        if str_number[i] != str_number[-(i + 1)]:  # Compare characters
            return False
    return True

# Main section to test all methods
if __name__ == "__main__":
    # Input from the user
    num = int(input("Enter a number: "))

    # Call all methods and print their results
    print("Using String Method:", is_palindrome_string(num))
    print("Using Reverse Method:", is_palindrome_reverse(num))
    print("Using Recursive Method:", is_palindrome_recursive(num))
    print("Using Iteration Method:", is_palindrome_iter(num))
