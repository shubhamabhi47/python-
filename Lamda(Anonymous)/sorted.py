# Using lambda with the sorted function so sorted function expect a funtion as key which we are passing and sorted function is responsible for calling that function 
# as we can see first we are passing len function then func function , then lambda function depend on the choice 

def func(name):
    return name.split()[1]


data = [
  "Mahatma Gandhi",
  "Subhas Chandra Bose",
  "Bhagat Singh",
  "Chandrashekhar Azad",
  "Sardar Vallabhbhai Patel",
  "Jawaharlal Nehru",
  "Bal Gangadhar Tilak",
  "Lala Lajpat Rai",
  "Bipin Chandra Pal",
  "Rani Lakshmibai",
  "Mangal Pandey",
  "Ram Prasad Bismil",
  "Ashfaqulla Khan",
  "Sarojini Naidu",
  "Annie Besant",
  "Dadabhai Naoroji",
  "Gopal Krishna Gokhale",
  "Maulana Abul Kalam Azad",
  "Rajendra Prasad",
  "Aruna Asaf Ali"
]

# print(sorted(data , key = len))

print(sorted(data , key = func))
print(sorted(data , key = lambda name: name.split()[1]))