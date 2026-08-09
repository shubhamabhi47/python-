# def total_cost(items , currency = 'INR'):
#     total = sum(items.values())        #[1.00 , 0.75 , 1.25]
#     # total = sum(items.keys())          #['Apple' , 'Banana' , 'Orange']
#     print("Total cost is:",total , currency)

# carts = {"Apple":1.00, "Banana":0.75 , "Orange":1.25}

# # total_cost(carts,'USD')
# total_cost(carts)



# def details(name = "ABC", age = 0):
#     print(f"name is {name} and age is {age}")

# details()
# print(details.__defaults__)
# details()
# print(details.__defaults__)
# details()


# def add_item(name , employee_data = []):
#     employee_data.append(name)
#     print("Updated data is :",employee_data)

# add_item("jay")
# print(add_item.__defaults__)
# add_item("Viru")
# print(add_item.__defaults__)
# add_item("Basanti")
# print(add_item.__defaults__)
# add_item("Thakur")



# def add_item(name , employee_data = None):
#     if(employee_data is None):
#         employee_data = []
#     employee_data.append(name)
#     print("Updated data is :",employee_data)

# add_item("jay")
# print(add_item.__defaults__)
# add_item("Viru")
# print(add_item.__defaults__)
# add_item("Basanti")
# print(add_item.__defaults__)
# add_item("Thakur")



def add_item(name , employee_data = "Abhimanyu"):
    employee_data = employee_data + "RRR"
    print("Updated data is :",employee_data)

add_item("jay")
print(add_item.__defaults__)
add_item("Viru")
print(add_item.__defaults__)
add_item("Basanti")
print(add_item.__defaults__)
add_item("Thakur")