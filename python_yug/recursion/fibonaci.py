# Program to generate Fibonacci series using multiple methods

# Method 1: Iterative Approach
def fibonacci_iterative(n):
    """
    Generates the Fibonacci series up to 'n' terms using iteration.
    """
    if n <= 0:
        return []  # Return an empty list for invalid input
    series = [0, 1]  # First two terms of Fibonacci series
    while len(series) < n:
        series.append(series[-1] + series[-2])  # Add the last two terms
    return series[:n]

# Method 2: Recursive Approach
def fibonacci_recursive(n):
    """
    Generates the nth Fibonacci number using recursion.
    The series can be printed by calling this function repeatedly.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    series = fibonacci_recursive(n - 1)  # Recursively get the series up to n-1
    series.append(series[-1] + series[-2])  # Add the nth term
    return series

# Method 3: Using a Generator
def fibonacci_generator(n):
    """
    Generates Fibonacci numbers up to 'n' terms using a generator.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a  # Yield the current number
        a, b = b, a + b  # Move to the next number

# Main section to test all methods
if __name__ == "__main__":
    # Input from the user
    num_terms = int(input("Enter the number of terms for Fibonacci series: "))

    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        # Using Iterative Method
        print("Fibonacci series (Iterative):", fibonacci_iterative(num_terms))

        # Using Recursive Method
        print("Fibonacci series (Recursive):", fibonacci_recursive(num_terms))

        # Using Generator
        print("Fibonacci series (Generator):", list(fibonacci_generator(num_terms)))
