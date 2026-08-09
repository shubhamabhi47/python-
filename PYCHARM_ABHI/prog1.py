text = "i feel python language is very easy"

capitalized = text.capitalize()
uppercase = text.upper()
lowercase = text.lower()
swapcase = text.swapcase()

titlecase = text.title()
count_e = text.count('e')

find_python = text.find('python')

replaced = text.replace('python', 'Python')

split_words = text.split()

starts_with = text.startswith('i feel')

ends_with = text.endswith('easy')
stripped = text.strip()



# Results
print("1.Capitalized:", capitalized)
print("2.Uppercase:", uppercase)
print("3.Lowercase:", lowercase)
print("4.Swapcase:", swapcase)
print("5.Titlecase:", titlecase)
print("6.Count of 'e':", count_e)

print("7.Replaced 'python' with 'python':", replaced)
print("8.Split into words:", split_words)

print("9.Ends with 'easy':", ends_with)
print("10.Stripped:", stripped)

