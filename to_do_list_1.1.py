from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pickle
import datetime

root = Tk()
root.title("To-Do List")
root.geometry("600x600")

# Defining Functions
priority_number = 0
def add_task():
    global priority_number
    task = entry_task.get()
    if task != "":
        time_option_task = time_task_options_dropdown.get()
        if time_option_task == 'Specific Time':
        
            hour_task = time_task_hour_dropdown.get()
            minute_task = time_task_minute_dropdown.get()
            day_task = date_task_date_dropdown.get()
            month_task = date_task_month_dropdown.get()
            year_task = date_task_year_dropdown.get()
            Time_to_perform = hour_task +":"+ minute_task
            Date_to_perform = day_task +" "+ month_task +" "+ year_task
            listbox_tasks.insert(parent='', index='end', iid=priority_number ,text=(priority_number+1), values=( entry_task.get(), Time_to_perform, week_task_dropdown.get(),Date_to_perform))
            priority_number = priority_number + 1
            entry_task.delete(0,END)
        else :

            day_task = date_task_date_dropdown.get()
            month_task = date_task_month_dropdown.get()
            year_task = date_task_year_dropdown.get()
            Time_to_perform = "Anytime"
            Date_to_perform = day_task +" "+ month_task +" "+ year_task
            listbox_tasks.insert(parent='', index='end', iid=priority_number ,text=(priority_number+1), values=( entry_task.get(), Time_to_perform, week_task_dropdown.get(),Date_to_perform))
            priority_number = priority_number + 1
            entry_task.delete(0,END)

    else:
        messagebox.showwarning(title="Warning!", message="You must enter a task")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        messagebox.showwarning(title="Warning!", message="You must select a task")

def load_tasks():
    try:
        tasks = pickle.load(open("task.dat","rb"))
        listbox_tasks.delete(0, END)
        for task in tasks:
            listbox_tasks.insert(END, task)
    except:
        messagebox.showwarning(title="Warning!", message="No initial task exist")

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat","wb"))

def donothing(event):
    pass

def timeoption(event):
    time_option_task = time_task_options_dropdown.get()
    if time_option_task == 'Anytime':
        time_task_hour_dropdown = ttk.Combobox(state='disabled')
        time_task_minute_dropdown = ttk.Combobox(state='disabled')
    else:
        time_task_hour_dropdown = ttk.Combobox(state='readonly')
        time_task_minute_dropdown = ttk.Combobox(state='readonly')
# GUI
# Setting Frame for view of List
frame_tasks = Frame(root)
frame_tasks.pack()

# Setting The view for List
listbox_tasks = ttk.Treeview(frame_tasks)
listbox_tasks.pack(side=LEFT)

# Set columns
listbox_tasks['columns'] = ('Task','Time','Week','Date')

listbox_tasks.column('#0', width=80, minwidth=25)
listbox_tasks.column('Task', anchor=W, width=200)
listbox_tasks.column('Time', anchor=W, width=80)
listbox_tasks.column('Week', anchor=CENTER, width=80)
listbox_tasks.column('Date', anchor=W, width=80)

listbox_tasks.heading("#0", text='Priority', anchor=W)
listbox_tasks.heading("Task", text='Task', anchor=W)
listbox_tasks.heading("Time", text='Time', anchor=W)
listbox_tasks.heading("Week", text='Week', anchor=CENTER)
listbox_tasks.heading("Date", text='Date', anchor=W)

listbox_tasks.pack(pady=20)

# Set Scrollbar
scrollbar_task_y = Scrollbar(frame_tasks)
scrollbar_task_y.pack(side=RIGHT, fill=Y)

listbox_tasks.config(yscrollcommand=scrollbar_task_y.set)
scrollbar_task_y.config(command=listbox_tasks.yview)

# Set Frame for entry boxes
entrybox_frame_tasks = Frame(root)
entrybox_frame_tasks.pack()

# Labels for entry boxes
entry_task_label = Label(entrybox_frame_tasks, text="Task")
entry_task_label.grid(row=0,column=0)

time_task_label = Label(entrybox_frame_tasks, text="Time")
time_task_label.grid(row=0,column=2)

time_task_label_hour = Label(entrybox_frame_tasks, text="H")
time_task_label_hour.grid(row=1,column=1)

time_task_label_minute = Label(entrybox_frame_tasks, text="M")
time_task_label_minute.grid(row=1,column=2)

time_task_label_options = Label(entrybox_frame_tasks, text="Time option")
time_task_label_options.grid(row=1,column=3)

week_task_label = Label(entrybox_frame_tasks, text="Week")
week_task_label.grid(row=3,column=0)

date_task_label = Label(entrybox_frame_tasks, text="Date")
date_task_label.grid(row=3,column=2)

date_task_label_date = Label(entrybox_frame_tasks, text="DD")
date_task_label_date.grid(row=4,column=1)

date_task_label_month = Label(entrybox_frame_tasks, text="MM")
date_task_label_month.grid(row=4,column=2)

date_task_label_year = Label(entrybox_frame_tasks, text="YY")
date_task_label_year.grid(row=4,column=3)

# Entry Boxes
entry_task = Entry(entrybox_frame_tasks)
entry_task.grid(row=2,column=0)

# Dropdown Boxes
hour = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
current_hour = datetime.datetime.now().hour
time_task_hour_dropdown = ttk.Combobox(entrybox_frame_tasks, values=hour)
time_task_hour_dropdown.current(current_hour)
time_task_hour_dropdown.bind("<<ComboboxSelected>>", donothing)
time_task_hour_dropdown.grid(row=2,column=1)

minute = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
current_minute = datetime.datetime.now().minute
time_task_minute_dropdown = ttk.Combobox(entrybox_frame_tasks, values=minute)
time_task_minute_dropdown.current(current_minute)
time_task_minute_dropdown.bind("<<ComboboxSelected>>", donothing)
time_task_minute_dropdown.grid(row=2,column=2)

time_options = ['Specific Time','Anytime']
time_task_options_dropdown = ttk.Combobox(entrybox_frame_tasks, state="readonly", values=time_options)
time_task_options_dropdown.current(0)
time_task_options_dropdown.bind("<<ComboboxSelected>>", donothing)
time_task_options_dropdown.grid(row=2,column=3)

current_date = datetime.datetime.now().day

current_month = datetime.datetime.now().month

current_year = datetime.datetime.now().year

weekday_number = datetime.date(current_year,current_month,current_date).weekday()

week_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
week_task_dropdown = ttk.Combobox(entrybox_frame_tasks, state="readonly", values=week_days)
week_task_dropdown.current(weekday_number)
week_task_dropdown.bind("<<ComboboxSelected>>", donothing)
week_task_dropdown.grid(row=5,column=0)


dates = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
month = ['January','February','March','April','May','June','July','August','September','October','November','December']
year = ['2021','2022','2023','2024']

date_task_date_dropdown = ttk.Combobox(entrybox_frame_tasks, state="readonly", values=dates)
date_task_date_dropdown.current(current_date-1)
date_task_date_dropdown.bind("<<ComboboxSelected>>", donothing)
date_task_date_dropdown.grid(row=5,column=1)

date_task_month_dropdown = ttk.Combobox(entrybox_frame_tasks, state="readonly", values=month)
date_task_month_dropdown.current(current_month-1)
date_task_month_dropdown.bind("<<ComboboxSelected>>", donothing)
date_task_month_dropdown.grid(row=5,column=2)

date_task_year_dropdown = ttk.Combobox(entrybox_frame_tasks, state="readonly", values=year)
date_task_year_dropdown.current(current_year-2021)
date_task_year_dropdown.bind("<<ComboboxSelected>>", donothing)
date_task_year_dropdown.grid(row=5,column=3)

"""date_task_minute = Entry(entrybox_frame_tasks)
date_task_minute.grid(row=5,column=2)

date_task_second = Entry(entrybox_frame_tasks)
date_task_second.grid(row=5,column=3)"""
#button_anytime = tkinter.Button(root, text="Anytime", width=25, command=anytime)
#button_anytime.pack(side=tkinter.RIGHT)

button_add_task = Button(root, text="Add Task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = Button(root, text="Delete Task", width=48, command=delete_task)
button_delete_task.pack()

button_load_tasks = Button(root, text="Load Tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = Button(root, text="Save Tasks", width=48, command=save_tasks)
button_save_tasks.pack()

root.mainloop()