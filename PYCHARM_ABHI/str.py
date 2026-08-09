text = "i feel puthon language is very easy"

# Capitalize the first letter
capitalized = text.capitalize()

# Convert all letters to uppercase
uppercase = text.upper()

# Convert all letters to lowercase
lowercase = text.lower()

# Swap case (uppercase becomes lowercase, and vice versa)
swapcase = text.swapcase()

# Title case (capitalize the first letter of each word)
titlecase = text.title()

# Count occurrences of a substring ("e")
count_e = text.count('e')

# Find the position of the first occurrence of a substring ("puthon")
find_puthon = text.find('puthon')

# Replace a substring ("puthon" with "python")
replaced = text.replace('puthon', 'python')

# Split the string into a list of words
split_words = text.split()

# Check if the string starts with "i feel"
starts_with = text.startswith('i feel')

# Check if the string ends with "easy"
ends_with = text.endswith('easy')

# Remove whitespace from the beginning and end of the string
stripped = text.strip()

# Center the text within 40 characters, padding with spaces
centered = text.center(40)

# Pad the text with leading zeros to make it 40 characters long
zfilled = text.zfill(40)

# Results
print("Capitalized:", capitalized)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Swapcase:", swapcase)
print("Titlecase:", titlecase)
print("Count of 'e':", count_e)
print("Find 'puthon':", find_puthon)
print("Replaced 'puthon' with 'python':", replaced)
print("Split into words:", split_words)
print("Starts with 'i feel':", starts_with)
print("Ends with 'easy':", ends_with)
print("Stripped:", stripped)
print("Centered (40 chars):", centered)
print("Zfilled (40 chars):", zfilled)
