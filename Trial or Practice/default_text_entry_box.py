import tkinter as tk


root = tk.Tk()
root.geometry("200x100")

text = tk.StringVar()
text.set("This is the default text")
textBox = tk.Entry(root,textvariable = text)

textBox.pack()

root.mainloop()
