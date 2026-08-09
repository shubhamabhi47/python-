# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



name = input("Enter name:")
for char in name:
    if char == 'm':
        break
    # print(char)
    # print(char , end = "")
    # print(char , end = " ")

rev = input("Enter any stirng to reverse : ")
print("sliced string is: ", rev[-1::])       #by default the start index is 0,character at stop index is not printed and step index is 1 and 
print("Reversed string is: ", rev[-1::-1])       #by default the step value is 1    (end  = stop - 1)
print("Empty string is: ", rev[-1:-1:-1])       #empty string  