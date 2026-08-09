import tkinter as tk
def on_button_click():
    label.config(text = "Shubham")

root = tk.Tk()
root.title("Tkinter Example")
label = tk.Label(root,text="Click the button below")
label.pack(pady = 40)
button = tk.Button(root,text = "Click Me",command = on_button_click)
button.pack(pady = 40)
root.mainloop()

# wap to Implement the folllowing operation
# 1)sqrt
# 2)Radian
# 3)sin cos tan
# 4)Degree
# 5)Random floating point btw 0 and 1
# 6)Random Number   btw 0 and 100
# 7)Random Element from a list as per your choice
# 8)Number of seconds since january 1st 1917
# 9)Convert number of seconds to date