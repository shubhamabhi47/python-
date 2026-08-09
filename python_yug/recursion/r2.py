# Direct recursion --> When function calls itself
# Indirect recursion --> When function calls another function which then calls the first function again

# Write a python program for printing n to 1 sequence

n = int(input("Enter the value of n:"))

def natural(n):
    if n==0:
        return 
    else:
        print(n , end=" ")
        return natural(n-1)
    
natural(n)



#  using indirect recursion

# def num(n):
#     if n<=0:
#         return 
#     print(n , end=" ")
#     num1(n-1)

# def num1(n):
#     print(n, end=" ")
#     num(n-1)
    
# num1(10)


# Finding factorial of a number

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

f =  int(input("\nEnter a number to find factorial:"))
print("factorial of n:",fact(f))