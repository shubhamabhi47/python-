# def is_prime(n):
#     if n <= 1:
#         return False  # 0 and 1 are not prime
#     for i in range(2, int(n**0.5) + 1):  # Check divisors up to √n
#         if n % i == 0:
#             return False
#     return True


# def is_prime(n):
#     if n <= 1:
#         return False  # Numbers less than or equal to 1 are not prime
#     for i in range(2, int(n**0.5) + 1):  # Check divisors up to the square root of n
#         if n % i == 0:
#             return False
#     return True

# # Get user input and check if the number is prime
# try:
#     num = int(input("Enter a number to check if it is a prime number: "))
#     if is_prime(num):
#         print(f"{num} is a prime number.")
#     else:
#         print(f"{num} is not a prime number.")
# except ValueError:
#     print("Please enter a valid integer.")
    
    
    
    
    
    
    
import math

def main():
    count = 0  # Initialize count to zero
    x = int(input("Please enter a number (only positive integers): "))  # Input from user

    val1 = math.ceil(math.sqrt(x))  # Find the square root of the input
    val2 = x  # Store the input for later checks

    # Loop to check divisibility from 2 to the square root of the number
    for i in range(2, val1 + 1):
        if val2 % i == 0:  # Check if val2 is divisible by i
            count = 1  # Set count to 1 if divisible

    # Check prime conditions: numbers divisible only by 1 and themselves
    if (count == 0 and val2 != 1) or val2 == 2 or val2 == 3:
        print(f"{val2} is a prime number")  # Output if prime
    else:
        print(f"{val2} is not a prime number")  # Output if not prime

if __name__ == "_main_":
    main()



