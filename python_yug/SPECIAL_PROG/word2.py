sentence = "Almost nothing was more annoying than having out wasted time time time"
words = sentence.split()

dictionary = {}

for w in words:
    if w in dictionary:
        dictionary[w]+=1
    else:
        dictionary[w]=1

print(dictionary)
for x in dictionary.keys():
        print(f"{x} occurs {dictionary[x]} times")