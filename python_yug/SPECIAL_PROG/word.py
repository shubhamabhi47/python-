sentence = input("Enter any valid sentence: ")

# Method 1: Using a dictionary to manually count occurrences
# Logic: Check if the character exists in the dictionary, increment its count, otherwise add it
char_count_dict = {}
for char in sentence:
    if char in char_count_dict:
        char_count_dict[char] += 1  # Increment count for existing character
    else:
        char_count_dict[char] = 1  # Initialize count for new character
print("Method 1: Using dictionary")
for char, count in char_count_dict.items():
    print(f"{char} appears {count} times.")

# Method 2: Using collections.Counter
# Logic: Counter automatically counts each character's occurrences in the string
from collections import Counter
char_count_counter = Counter(sentence)
print("\nMethod 2: Using collections.Counter")
for char, count in char_count_counter.items():
    print(f"{char} appears {count} times.")

# Method 3: Using nested loops
# Logic: For each unique character, traverse the entire string to count its occurrences
print("\nMethod 3: Using nested loops")
for char1 in set(sentence):  # Using set to avoid duplicate counts
    count = 0
    for char2 in sentence:  # Count how many times char1 appears in the string
        if char1 == char2:
            count += 1
    print(f"{char1} appears {count} times.")

# Method 4: Using list comprehension
# Logic: Use a compact form to count occurrences for each unique character
print("\nMethod 4: Using list comprehension")
for char in set(sentence):  # Loop over unique characters only
    count = sum(1 for c in sentence if c == char)  # Count matches in the sentence
    print(f"{char} appears {count} times.")

# Method 5: Using str.count()
# Logic: Directly use the string's built-in method to count occurrences of each character
print("\nMethod 5: Using str.count()")
for char in set(sentence):  # Avoid duplicate checks by iterating over unique characters
    print(f"{char} appears {sentence.count(char)} times.")

# Method 6: Using collections.defaultdict
# Logic: Use defaultdict to automatically handle missing keys with default integer value 0
from collections import defaultdict
char_count_defaultdict = defaultdict(int)
for char in sentence:
    char_count_defaultdict[char] += 1  # Increment count for each character
print("\nMethod 6: Using collections.defaultdict")
for char, count in char_count_defaultdict.items():
    print(f"{char} appears {count} times.")

# Method 7: Using pandas
# Logic: Convert the sentence into a DataFrame and use value_counts() to count occurrences
import pandas as pd
df = pd.DataFrame(list(sentence), columns=["Character"])  # Convert characters to a DataFrame
char_count_pandas = df["Character"].value_counts()  # Get counts for each character
print("\nMethod 7: Using pandas")
for char, count in char_count_pandas.items():
    print(f"{char} appears {count} times.")
