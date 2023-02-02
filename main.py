
import tkinter as tk
from tkinter import *
from calculation import Set_sequnce,Time_calculation
from Set_line import Get_Position

MAIN_BACKGROUND_COLOR = "#1A1A40"
CANVAS_BACKGROUND_COLOR = "#270082"
FONT_COLOR = "#FFFFFF"
FONT_PATTERN = "Arial 10 bold"
BORDER_SIZE= 5
POSTION_LIST = []
NUMBER_LIST = []
POINTER = 0
CURR_SEEK_TIME = []

main_window = tk.Tk()
main_window.geometry("765x600+20+20")
main_window.title("Scheduling Algorithms")
main_window.resizable(False,False)
main_window.config(background=MAIN_BACKGROUND_COLOR)

def Press_button():
    global POSTION_LIST
    global NUMBER_LIST
    global CURR_SEEK_TIME
    disk_numbers = disk_number_entry.get()
    disk_number_list = disk_numbers.split(',')
    disk_list = []
    for i in range(len(disk_number_list)):
        try:
            disk_list.append(int(disk_number_list[i]))
        except:
            print("error in input numbers")
            return 1
    
    # print(disk_list)
    try:
        starting_point = starting_point_number_entry.get()
        starting_point = int(starting_point)
    except:
        print("error in starting point")
        return 2
    # print(starting_point)

    try:
        starting_value = starting_value_number_entry.get()
        starting_value = int(starting_value)
    except:
        print("error in starting value")
        return 3
    # print(starting_value)

    try:
        ending_value = ending_value_number_entry.get()
        ending_value= int(ending_value)
    except:
        print("error in ending value..")
        return 4
    # print(ending_value)

    algorithum_value = var.get()
    # print(algorithum_value)

    array_min_value = min(disk_list)
    array_max_value = max(disk_list)

    if(starting_point<=array_min_value or starting_point>=array_max_value):
        print("wrong starting point")
        return 5
    elif(starting_value>=array_min_value):
        print("wrong starting value")
        return 6
    elif(ending_value<=array_max_value):
        print("wrong ending value")
        return 7
    elif(algorithum_value==0):
        print("algorithum not selected..")
        return 8
    
    if(algorithum_value==1):
        new_list = Set_sequnce.FCFS(disk_list,starting_point)
        final_point_list = Get_Position.get_postion(new_list,ending_value)
    elif(algorithum_value==2):
        new_list = Set_sequnce.SSTF(disk_list,starting_point)
        final_point_list = Get_Position.get_postion(new_list,ending_value)
    elif(algorithum_value==3):
        new_list = Set_sequnce.SCAN(disk_list,starting_point,ending_value)
        final_point_list = Get_Position.get_postion(new_list,ending_value)
    elif(algorithum_value==4):
        new_list = Set_sequnce.CSCAN(disk_list,starting_point,ending_value,starting_value)
        final_point_list = Get_Position.get_postion(new_list,ending_value)
    elif(algorithum_value==5):
        new_list = Set_sequnce.LOOK(disk_list,starting_point)
        final_point_list = Get_Position.get_postion(new_list,ending_value)
    elif(algorithum_value==6):
        new_list = Set_sequnce.CLOOK(disk_list,starting_point)
        final_point_list = Get_Position.get_postion(new_list,ending_value)

    control_button.place_forget()
    next_button.place(x=635,y=470)
    canvas.create_line(10,20,590,20,fill="#ffffff",width=2)
    canvas.create_text(10,15,text=f'{starting_value}',fill='#ffffff',font=FONT_PATTERN)
    canvas.create_text(590,15,text=f'{ending_value}',fill='#ffffff',font=FONT_PATTERN)
    POSTION_LIST = final_point_list
    NUMBER_LIST = new_list
    canvas.create_text(final_point_list[0][0],final_point_list[0][1],text=f'{new_list[0]}',fill='#ffffff')
    CURR_SEEK_TIME.append(NUMBER_LIST[0])
    # for i in range(len(final_point_list)-1):
    #     canvas.create_line(final_point_list[i][0],final_point_list[i][1],final_point_list[i+1][0],final_point_list[i+1][1],fill="#ffffff",width=2,arrow=tk.LAST)
    #     canvas.create_text(final_point_list[i][0]+15,final_point_list[i][1]-5,fill="#ffffff",text=f'{new_list[i]}')
    # canvas.create_text(final_point_list[-1][0],final_point_list[-1][1],text=f'{new_list[-1]}',fill='#ffffff')

def Next_move():
    global POSTION_LIST
    global POINTER
    global CURR_SEEK_TIME
    if(len(NUMBER_LIST)!=POINTER+1):
        CURR_SEEK_TIME.append(NUMBER_LIST[POINTER+1])
        canvas.create_line(POSTION_LIST[POINTER][0],POSTION_LIST[POINTER][1],POSTION_LIST[POINTER+1][0],POSTION_LIST[POINTER+1][1],fill='#ffffff',width=2,arrow=tk.LAST)
        canvas.create_text(POSTION_LIST[POINTER+1][0],POSTION_LIST[POINTER+1][1],text=f'{NUMBER_LIST[POINTER+1]}',fill='#ffffff')
        POINTER = POINTER + 1
        seek_number_label.configure(text=f"Seek Time : {Time_calculation.SEEK_TIME(CURR_SEEK_TIME)}")
    else:
        next_button.place_forget()
        stop_button.place(x=635,y=470)
        CURR_SEEK_TIME = []

        
def Stop_press():
    global POINTER,POSTION_LIST,NUMBER_LIST
    canvas.delete('all')
    POINTER = 0
    POSTION_LIST = []
    NUMBER_LIST = []
    disk_number_entry.delete(0,END)
    starting_point_number_entry.delete(0,END)
    starting_value_number_entry.delete(0,END)
    ending_value_number_entry.delete(0,END)
    stop_button.place_forget()
    control_button.place(x=635,y=470)
    seek_number_label.configure(text=f"Seek Time : 0")



canvas = Canvas(main_window,height=600,width=600)
canvas.place(x=0,y=0)
canvas.configure(background=CANVAS_BACKGROUND_COLOR)

disk_number_label = Label(main_window,text="Enter Disk Numbers")
disk_number_label.place(x=610,y=10)
disk_number_label.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

disk_number_entry = Entry(main_window)
disk_number_entry.place(x=610,y=35)
disk_number_entry.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN,bd=BORDER_SIZE)

startingi_point_number_label = Label(main_window,text="Enter Starting Point")
startingi_point_number_label.place(x=610,y=80)
startingi_point_number_label.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

starting_point_number_entry = Entry(main_window)
starting_point_number_entry.place(x=610,y=105)
starting_point_number_entry.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN,bd=BORDER_SIZE)

starting_value_number_label = Label(main_window,text="Enter Starting Value")
starting_value_number_label.place(x=610,y=150)
starting_value_number_label.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

starting_value_number_entry = Entry(main_window)
starting_value_number_entry.place(x=610,y=175)
starting_value_number_entry.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN,bd=BORDER_SIZE)

ending_value_number_label = Label(main_window,text="Enter Ending Value")
ending_value_number_label.place(x=610,y=220)
ending_value_number_label.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

ending_value_number_entry = Entry(main_window)
ending_value_number_entry.place(x=610,y=245)
ending_value_number_entry.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN,bd=BORDER_SIZE)

var = IntVar()
fcfs_radio = Radiobutton(main_window,text="FCFS",variable=var,value=1,command=None)
fcfs_radio.place(x=610,y=280)
fcfs_radio.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

sstf_radio = Radiobutton(main_window,text="SSTF",variable=var,value=2,command=None)
sstf_radio.place(x=610,y=310)
sstf_radio.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

scan_radio = Radiobutton(main_window,text="SCAN",variable=var,value=3,command=None)
scan_radio.place(x=610,y=340)
scan_radio.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

cscan_radio = Radiobutton(main_window,text="CSCAN",variable=var,value=4,command=None)
cscan_radio.place(x=610,y=370)
cscan_radio.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

look_radio = Radiobutton(main_window,text="LOOK",variable=var,value=5,command=None)
look_radio.place(x=610,y=400)
look_radio.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

clook_radio = Radiobutton(main_window,text="CLOOK",variable=var,value=6,command=None)
clook_radio.place(x=610,y=430)
clook_radio.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)

control_button = Button(main_window,text="Run",width=10,height=3,command=Press_button)
control_button.place(x=635,y=470)
control_button.configure(background=MAIN_BACKGROUND_COLOR,font=FONT_PATTERN,foreground=FONT_COLOR)

next_button = Button(main_window,text="Next",width=10,height=3,command=Next_move)
next_button.place(x=635,y=470)
next_button.configure(background=MAIN_BACKGROUND_COLOR,font=FONT_PATTERN,foreground=FONT_COLOR)
next_button.place_forget()

stop_button = Button(main_window,text="Stop",width=10,height=3,command=Stop_press)
stop_button.place(x=635,y=470)
stop_button.configure(background=MAIN_BACKGROUND_COLOR,font=FONT_PATTERN,foreground=FONT_COLOR)
stop_button.place_forget()

seek_number_label = Label(main_window,text="Seek Time : 0")
seek_number_label.place(x=610,y=550)
seek_number_label.configure(background=MAIN_BACKGROUND_COLOR,foreground=FONT_COLOR,font=FONT_PATTERN)


main_window.mainloop()