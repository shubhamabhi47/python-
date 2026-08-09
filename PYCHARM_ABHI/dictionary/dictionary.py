# change values of a specific item by reffering to its key name
#changing key value pair of object if items does not exist then item eill be added
# Adding items to the dictionary
thisDict = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year"  : 1964
}
# update() is generally used to update multiple key-value pairs or update existing keys
# thisDict.update({"Year":2020})

# Direct key assignment is a straightforward way to either add or update a specific key-value pair.
# thisDict["color"] = "Red"

# pop() removess the items with specified key name\
# thisDict.pop("Model")

# del key word removes the item with specified key and also delete the dictionary completelu at a time
# del thisDict["Model"]

# The clear() method empties the dictionary
# thisDict.clear()
print(thisDict["Brand"])  # Output: Ford
print(thisDict["Model"])  # Output: Mustang
print(thisDict["Year"])   # Output: 1964
for key, value in thisDict.items():
    print(f"{key}: {value}")


print(thisDict)