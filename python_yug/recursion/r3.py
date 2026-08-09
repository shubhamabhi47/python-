#Factrial of number

n = int(input("Enter the vlaue of n to find factorial:"))

def fact(n):
     if n==0:
         return 1
     else:
         return n*fact(n-1)
    
    
# result = fact(n)
# print(f"Factorial of {n} is {result}")

if(n<0):
    print("Factorial of negative numbers cannot be calculated")
elif n==0:
    print(f"factorial of 0 is 1")
else:
    result=fact(n)
    
# print(f"Factorial of {n} is {result}")







# Print your name 10 times without using loop and manually
print("10 times my name by two method")
def name(s , n):
    if n==0:
        return
    else:
        print(s)
        name(s , n-1)
        
name("Abhiii" , 10)


print("2nd Another method")

count = 1 

def printer(name):
    global count
    if count<=10:
        print(name)
        count+=1
        printer(name)

printer("RRRRRRR")