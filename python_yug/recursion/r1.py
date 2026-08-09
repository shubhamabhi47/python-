import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(200)
# print(sys.setrecursionlimit)
print(sys.getrecursionlimit())

i=0

def demo():
    global i
    i=i+1
    print("Hello WOrld")
    demo()

demo()


# Advantages of recursion
# 1)clean code
# 2)Complex problems can be solved

# disadvantages of recursion
# 1)Hard to debug
# 2)Not memory efficient (Due to activation record is maintained inside stack )
