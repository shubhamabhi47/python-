
class Demo:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object finalized")


obj1 = Demo()
obj2 = obj1

# del obj1

print("obj2 still refers to the object")

# del obj2

