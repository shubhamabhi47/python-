#mixing variable length positional arguments and keyword arguments

def addition(*num , **nums): 
    print(num) 
    print(nums) 
    return sum(nums.values())                  

     
print(addition(50,60,70,n1 = 10, n2 = 20, n3= 30, n4 = 40))         #pass as dictionary
# print(addition(n1 = 10, n2 = 20, n3= 30,))
# print(addition(n1 = 10, n2 = 20))

