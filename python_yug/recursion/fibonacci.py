# Python program to fibonacci series using Recursion
# exampll --> if n=3 then f(3) = f(1) + f(2) as f(1)=0 and f(2)=1
# exampll --> if n=3 then f(3) = f(3-2) + f(3-1) as f(1)=0 and f(2)=1
def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return (fibo(n-2) + fibo(n-1))
        
    
n = int(input("Enter the number of terms for Fibonacci series: "))    
for i in range(1 , n+1):
    print(fibo(i))
    # print(fibo(i) , end=" ")
    
    
    
    
    
    
    
    
    
    
# def fibonacci_recursive_series(n):
#     """
#     Generates the Fibonacci series up to 'n' terms using recursion.
#     """
#     # Base cases
#     if n <= 0:
#         return []  # No terms for non-positive input
#     elif n == 1:
#         return [0]  # Series with 1 term
#     elif n == 2:
#         return [0, 1]  # Series with 2 terms
#     else:
#         # Recursive step: Get the series up to (n-1) terms
#         series = fibonacci_recursive_series(n - 1)
#         # Append the nth term as the sum of the last two terms
#         series.append(series[-1] + series[-2])
#         return series

# # Main section
# if __name__ == "__main__":
#     num_terms = int(input("Enter the number of terms for the Fibonacci series: "))

#     if num_terms <= 0:
#         print("Please enter a positive integer.")
#     else:
#         print("Fibonacci series:", fibonacci_recursive_series(num_terms))
