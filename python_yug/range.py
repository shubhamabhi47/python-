# range() function returns an immutable sequwnce of numbers between the given start and stop integer
# range(start , stop , step) 
# range() #type error
num1 = range(5,1)      #output = [] bcz no ending point (5,6,7,8,9,.......)
print(num1)
print(list(num1))


num2 = range(10, 0 ,-2)
print('length of num2: ', len(num2))
for i in range(len(num2)):
    print(i)
    print('-'*40)
    # print(num2[i])
    

