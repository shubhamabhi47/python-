# Write a python program for checking number is prime or not (use recursive way)

def prime(n , i):
    if i==1:
        return 1
    if n%i==0:
        return 0
    else:
        return prime(n,i-1)
            

   
n = int(input("Enter a number to check prime:"))   
rs = prime(n , n-1)

# if rs==1:
#     print(f"{n} is prime number.")
# if rs==0:
#     print(f"{n} is not a prime number.")

if n <= 1:
    print(f"{n} is not a prime number.")
else:
    rs = prime(n , n-1)
    if rs == 1:
        print(f"{n} is prime number.")
    else:
        print(f"{n} is not a prime number.")
 
# Only check up to sqrt(n) instead of n-1 for better efficiency.
    
    
    
    
    
    
    
# def prime(n, i):
#     # Base case: if `i` reaches 1, then the number is prime
#     if i == 1:
#         return True
#     # If `n` is divisible by `i`, it is not a prime number
#     if n % i == 0:
#         return False
#     # Recursive case: check for next smaller divisor
#     return prime(n, i - 1)

# # Input from the user
# n = int(input("Enter a number to check prime:"))

# # Handle edge cases for numbers less than 2
# if n < 2:
#     print(f"{n} is not a prime number.")
# else:
#     # Start the recursion with `n-1` as the initial divisor
#     if prime(n, n - 1):
#         print(f"{n} is a prime number.")
#     else:
#         print(f"{n} is not a prime number.")
