from csv import excel

try:
    f = open("demo.txt")
    try:
        f.write("Write a text inside a file.")
    except:
        print("Something went wrong to the file.")
    finally:
        f.close()
except:
    print("Something went wrong while opening the file.")

# try:
#     k = 5//0
#     print(k)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# finally:
#     print("This is always executed.")