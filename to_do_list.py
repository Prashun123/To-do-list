import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List")
root.geometry("600x400")

def add_task():
    task = entry_task.get()
    time_of_task = time_task.get()
    if task != "":
        if time_of_task !="":
            to_show = "Task :- "+ task +" Time :- "+ time_of_task
            listbox_tasks.insert(tkinter.END, to_show)
            entry_task.delete(0,tkinter.END)
            time_task.delete(0,tkinter.END)
        else:
            tkinter.messagebox.showwarning(title="Warning!", message="You must enter the time")  
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task")

def load_tasks():
    try:
        tasks = pickle.load(open("task.dat","rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="No initial task exist")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat","wb"))

# GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=5, width =50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_task = tkinter.Scrollbar(frame_tasks)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_tasks.yview)

entry_task_label = tkinter.Label(root, text="Task", justify='left')
entry_task_label.pack()
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

time_task_label = tkinter.Label(root, text="Time", justify='left')
time_task_label.pack()
time_task = tkinter.Entry(root, width=50)
time_task.pack()

#button_anytime = tkinter.Button(root, text="Anytime", width=25, command=anytime)
#button_anytime.pack(side=tkinter.RIGHT)

button_add_task = tkinter.Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Load Tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save Tasks", width=48, command=save_tasks)
button_save_tasks.pack()

root.mainloop()