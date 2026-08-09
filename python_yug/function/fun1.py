# def simple_interest(p , r , t):
#     print("Principle amount:", p)
#     print("Rate of interest:", r)
#     print("Number of years:", t)

#     si = (p*r*t)/100

#     print("Simple interest is:", si)

# simple_interest(1000, 2 , 12.5)
# print("-"*50)
# simple_interest(1000, 2 , 12.5)


# def sub_list(li, start_index, end_index):
#     new_li = []
#     for i in range(start_index, end_index + 1):
#         new_li.append(li[i])
#     return new_li
# li = [2, 23, 49, 6, 71, 55]
# print(sub_list(li, 2, 4))  # Output: [49, 6, 71]


li = [2, 3, 4, 5, 6]
n = 2

def left_shift(li, n):
    for i in range(n):
        a = li.pop(0)
        li.append(a)
    return li
print(left_shift([2, 3, 4, 5, 6], 2))  # Output: [4, 5, 6, 2, 3]