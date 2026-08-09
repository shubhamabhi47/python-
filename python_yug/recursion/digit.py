# Python program to counting number of digits in given number using recursion
# A number or a word or a phrase if read backwards gives the same number or a word or a phrase it is being read forward

n = int(input("Enter a number to find number of digit:"))
# count = 0 


def countt(n):
    if n<10:
        return 1
    else:
        return 1 + countt(n//10)

result = countt(n)
print("Total number of digit:" , result)




# n = int(input("Enter a number to find number of digit:"))
# count = 0 


# def countt(n):
#     global count
#     if n==0:
#         return count
#     else:
#         count+=1
#         return countt(n//10)

# result = countt(n)
# print("Total number of digit:" , result)








# def is_palindrome_recursive(number):
#     # Helper function to reverse the number
#     def reverse(num, rev=0):
#         if num == 0:
#             return rev
#         return reverse(num // 10, rev * 10 + num % 10)
    
#     return number == reverse(number)
