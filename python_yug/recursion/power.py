# python program to find power of a given number using recursion
def pow(base, power):
    if power == 0:  # Base case: Any number raised to power 0 is 1
        return 1
    elif power < 0:  # Handling negative powers
        return 1 / pow(base, -power)
    else:
        return base * pow(base, power - 1)  # Recursive case

n = int(input("Enter the base number: "))
p = int(input("Enter the power: "))

result = pow(n, p)
print(f"{n} raised to the power {p} is {result}")



    
print("Another method to find power")

def power(n , b):
    if p==0:
        return 1
    else:
        return n*power(n , p-1)

print(power(2,5))



#logical error in my code 😒😒😒😒😒
# n = int(input("Enter a number to find power:"))
# count = 1

# def pow(base , power):
#     global count
#     if count==power:
#         return n
#     else:
#         count+=1
#         return n*pow(n , 3)
    

# result = pow(n , 3)
# print(f"power of base {n} is {result}")