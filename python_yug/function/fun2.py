#variable length positional arguments 

# def addition(*nums):
#     print(nums)
#     # pass
     
# print(addition(10,20,30.40))
# print(addition(10,20,30))
# print(addition(10,20,))




# def addition(*nums):      #(10,20,30)
#     sum = 0
#     for n in nums:
#         sum+= n
#     return sum
     
# print(addition(10,20,30,40))     #pass as a tuples and we can iterate
# print(addition(10,20,30))      #pass as a tuples and we can iterate
# print(addition(10,20,))       #pass as a tuples and we can iterate






#variable length keyword arguments  (double asterick)

# def addition(**nums):  
#     print('--'*25)                  #{'n1': 10, 'n2': 20, 'n3': 30, 'n4': 40}
#     print(nums)
#     print('--'*25)                  
#     print(type(nums))
#     print('--'*25)                  
#     print(nums.values())
#     print('--'*25)                  
#     print(sum(nums.values()))
#     # pass
     
# print(addition(n1 = 10, n2 = 20, n3= 30, n4 = 40))         #pass as dictionary
# print(addition(n1 = 10, n2 = 20, n3= 30,))
# print(addition(n1 = 10, n2 = 20))





def addition(**nums):  
    return sum(nums.values())                  #{'n1': 10, 'n2': 20, 'n3': 30, 'n4': 40}

     
print(addition(n1 = 10, n2 = 20, n3= 30, n4 = 40))         #pass as dictionary
print(addition(n1 = 10, n2 = 20, n3= 30,))
print(addition(n1 = 10, n2 = 20))
