import tkinter as tk
from tkinter import *

MAIN_BACKGROUND_COLOR = "#1A1A40"
CANVAS_BACKGROUND_COLOR = "#270082"
FONT_COLOR = "#FFFFFF"
FONT_PATTERN = "Arial 10 bold"
BORDER_SIZE= 5


main_window = tk.Tk()
main_window.geometry("765x600+20+20")
main_window.title("CPU Algorithms")
main_window.resizable(False,False)
main_window.config(background=MAIN_BACKGROUND_COLOR)

canvas = Canvas(main_window,height=300,width=760)
canvas.place(x=0,y=0)
canvas.configure(background=CANVAS_BACKGROUND_COLOR)
counter = 0
def fcfs(tp,at,bt,time):
    p_name = ['p1','p2','p3','p4']
    a_time = at
    b_time = bt
    p_q = []
    s_q = []
    flag = True
    c_b_t = 0
    for i in range(time):
        if(i in a_time):
            for j in range(len(a_time)):
                if(i == a_time[j]):
                    p_q.append(p_name[j])
        if(len(p_q)!=0 and flag == True):
            flag =False
            name = p_q[0]
            c_b_t = b_time[p_name.index(p_q[0])]
            p_q.remove(p_q[0])
        if(c_b_t != 0):
            s_q.append(name)
            c_b_t = c_b_t - 1
            if(c_b_t == 0):
                flag = True
    #return p_q,s_q

def Press_button():
    global counter
    total_process = int(process_number_entry.get())
    a_time = at_entry.get()
    a_time = a_time.split(',')
    ar_time = []
    b_time = bt_entry.get()
    b_time = b_time.split(',')
    bs_time = []
    for i in range(len(a_time)):
        try:
            ar_time.append(int(a_time[i]))
        except:
            print("error in arrival time numbers")
            return 1
    for i in range(len(b_time)):
        try:
            bs_time.append(int(b_time[i]))
        except:
            print("error in bast time numbers")
            return 2
    fcfs(total_process,ar_time,bs_time,counter)
    counter = counter + 1
    #print(a,b)
    #print(total_process,ar_time,bs_time)

process_number_label = Label(main_window,text="Enter total Numbers of processes")
process_number_label.place(x=50,y=402)
process_number_label.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

process_number_entry = Entry(main_window)
process_number_entry.place(x=270,y=400)
process_number_entry.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN,bd=BORDER_SIZE)

at_label = Label(main_window,text="Enter Arrival time")
at_label.place(x=50,y=452)
at_label.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

at_entry = Entry(main_window)
at_entry.place(x=270,y=450)
at_entry.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN,bd=BORDER_SIZE)

bt_label = Label(main_window,text="Enter bust time")
bt_label.place(x=50,y=502)
bt_label.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

bt_entry = Entry(main_window)
bt_entry.place(x=270,y=500)
bt_entry.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN,bd=BORDER_SIZE)

control_button = Button(main_window,text="Run",width=10,height=3,command=Press_button)
control_button.place(x=550,y=435)
control_button.configure(background=MAIN_BACKGROUND_COLOR,font=FONT_PATTERN,foreground=FONT_COLOR)

main_window.mainloop()