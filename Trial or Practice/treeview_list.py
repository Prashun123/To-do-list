from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Treeview List")
root.geometry("500x500")

my_tree = ttk.Treeview(root)
my_tree['columns'] = ('Name','ID','Number')

my_tree.column("#0", width=120, minwidth=25)
my_tree.column('Name', anchor=W, width=120)
my_tree.column('ID', anchor=CENTER, width=80)
my_tree.column('Number', anchor=W, width=120)

my_tree.heading("#0", text='Label', anchor=W)
my_tree.heading("Name", text='Name', anchor=W)
my_tree.heading("ID", text='ID', anchor=CENTER)
my_tree.heading("Number", text='Number', anchor=W)

my_tree.insert(parent='', index='end', iid=0, text='Parent', values=("John", 1, "9275763773"))
# add child
my_tree.insert(parent='', index='end', iid=1, text='Child', values=("Wenne", 1.2, "5665612365"))
my_tree.move('1','0','0')

my_tree.pack(pady=20)

root.mainloop()