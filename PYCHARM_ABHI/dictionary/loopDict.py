thisDict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
for key, value in thisDict.items():
    print(f"{key}: {value}")

# Loop through keys
for key in thisDict:
    print(key, ":", thisDict[key])

# Loop through keys and values# Loop through values using values() method
# for value in thisDict.values():
#     print("Value:", value)


for key, value in thisDict.items():
    print(key, ":", value)


# Loop through keys using keys() method
for key in thisDict.keys():
    print(key, ":", thisDict[key])


# List comprehension to create a list of formatted strings
formatted_strings = [f"{key}: {value}" for key, value in thisDict.items()]
print(formatted_strings)

