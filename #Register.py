#Register

from tkinter import *

root = Tk()
root.geometry("500x300")
root.resizable(False, False)

Label(root, text="Login", font="är 20").grid(row=0, column=3)
nameTitle=Label(root, text="Username", font="är 10")
passwordTitle=Label(root, text="Password", font="är 10")

nameTitle.grid(row=1, column=2)
passwordTitle.grid(row=2, column=2)

name = StringVar
password = StringVar

nameInput = Entry(root, textvariable=name)
passwordInput = Entry(root, textvariable=password)

nameInput.grid(row=1, column=3)
passwordInput.grid(row=2, column=3)

Button(root, text="Login").grid(row=5, column=3)

Label(root, text="New to us?").grid(row=6, column=3)
Button(root, text="Register").grid(row=7, column=3)

root.mainloop()