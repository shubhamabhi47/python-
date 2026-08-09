# Python program for sum of first n numbers using recursion

def add(n):
    if n==1:
        return 1
    else:
        return n + add(n-1)

n = int(input("enter the number of terms for sum:"))
print("Sum:",add(n))

def sum1(n , result):
    if n==0:
        return result
    else:
        result=result+n
        return sum1(n-1 , result)
    
print("Sum:", sum1(10,result=0))