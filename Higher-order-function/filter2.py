str1 = "Shubham"
vowels_list = ['a' ,'e' ,'i' ,'o' ,'u']


for char in str1:
    if str1 in vowels_list:
        print(str1)

# **1. Input setup:**
# str1 = input("Enter the string: ")
# print(str1)
# print(type(str1))


# **2. First code attempt (Error causing):**
vowels = ['a', 'e', 'i', 'o', 'u']

def vowels(c):
    if c in vowels: 
        return True

# filter(vowels, str1) # Raises TypeError


# **3. Corrected vowel filtering:**
vowels_list = ['a', 'e', 'i', 'o', 'u']

def check_vowels(c):
    if c in vowels_list:
        return True

filtered_obj = filter(check_vowels, "shantanu")
print(list(filtered_obj))


# **4. Lambda expression:**
result = filter(lambda char: char in vowels_list, "shantanu")


# **5. Dictionary access check:**
data = {"Nitesh": 85, "Rahul": 98, "Raj": 91, "Amar": 90, "Abhi": 81}
print(data["Rahul"])


# **6. Dictionary filtering:**
def toppers(student):
    return data[student] >= 90

result = filter(toppers, data)
print(list(result))

# Exactly — the key point is:

# > **`filter()` does NOT pass the whole `data` dictionary to `toppers()`. It passes each element of `data` one by one.**

# Let's walk through it.

# Your dictionary is:

# ```python
# data = {"Nitesh": 85, "Rahul": 98, "Raj": 91, "Amar": 90, "Abhi": 81}
# ```

# When you do:

# ```python
# result = filter(toppers, data)
# ```

# Python iterates over the dictionary. **Iterating over a dictionary gives its keys**:

# ```text
# "Nitesh"
# "Rahul"
# "Raj"
# "Amar"
# "Abhi"
# ```

# So conceptually, `filter()` is doing something like:

# ```python
# toppers("Nitesh")
# toppers("Rahul")
# toppers("Raj")
# toppers("Amar")
# toppers("Abhi")
# ```

# Now look at your function:

# ```python
# def toppers(student):
#     return data[student] >= 90
# ```

# The `student` parameter receives **one key at a time**.

# ### First call

# ```python
# toppers("Nitesh")
# ```

# Inside the function:

# ```python
# data[student]
# ```

# becomes:

# ```python
# data["Nitesh"]
# ```

# which gives:

# ```python
# 85
# ```

# Then:

# ```python
# 85 >= 90
# ```

# is:

# ```python
# False
# ```

# So `"Nitesh"` is rejected.

# ---

# ### Second call

# ```python
# toppers("Rahul")
# ```

# Inside:

# ```python
# data[student]
# ```

# becomes:

# ```python
# data["Rahul"]
# ```

# which gives:

# ```python
# 98
# ```

# Then:

# ```python
# 98 >= 90
# ```

# → `True`

# So `"Rahul"` is kept.

# The process looks like this:

# ```text
# filter(toppers, data)

#           ↓

# toppers("Nitesh") → data["Nitesh"] → 85 >= 90 → False
# toppers("Rahul")  → data["Rahul"]  → 98 >= 90 → True
# toppers("Raj")    → data["Raj"]    → 91 >= 90 → True
# toppers("Amar")   → data["Amar"]   → 90 >= 90 → True
# toppers("Abhi")   → data["Abhi"]   → 81 >= 90 → False

#           ↓

# ["Rahul", "Raj", "Amar"]
# ```

# So the important distinction is:

# ```python
# filter(toppers, data)
#        ↑        ↑
#     function   iterable
# ```

# `filter()` effectively does:

# ```python
# for item in data:
#     if toppers(item):
#         yield item
# ```

# Since `item` is each **dictionary key**, `student` receives each key.

# And that's why this works:

# ```python
# data[student]
# ```

# because `student` is `"Rahul"`, `"Raj"`, etc., which are valid dictionary keys.

# One subtle point: `filter()` is **lazy**. The function isn't necessarily called immediately when you write:

# ```python
# result = filter(toppers, data)
# ```

# The calls happen when you consume it, such as with:

# ```python
# list(result)
# ```

# That's when Python actually starts calling `toppers()` for each key.
