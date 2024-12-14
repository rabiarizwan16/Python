from tkinter import *
import math

reps=0
WORK_MIN=1
SHORT_BREAK_MIN=5
LONG_BREAK_MIN=20
timer=None
#--------TIMER RESET------------
def reset_timer():
    global timer
    root.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer",fg="#008B8B")
    global reps
    reps=0
#----------TIMER MECHANISM--------
def start_timer():
    global reps
    reps+=1


    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps==1 or reps==3 or reps==5 or reps==7:
        count_down(work_sec)
        label.config(text="Work", fg="#008B8B")

    elif reps==8:
        count_down(long_break_sec)
        label.config(text="Break", fg="#008B8B")
    elif reps==2 or reps==4 or reps==6:
        count_down(short_break_sec)
        label.config(text="Break", fg="red")

    ''' if reps%8==0:
        count_down(long_break_sec)
    elif reps%2==0:
        count_down(short_break_sec)
    else:
        count_down(work_sec)'''

#----------COUNTDOWN MACHANISM-------
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=math.floor(count%60)
    if count_sec<10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
         global timer
         timer = root.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=" "
        work_session=math.floor(reps/2)
        for i in range(work_session):
            mark+="\u2713"
        label1.config(text=mark)


root=Tk()
root.title("Pomodora")
root.geometry("600x600")

root.config(padx=150,pady=50,bg="#FCE6C9")
label=Label(text="Timer",fg="#008B8B",font=("" , 35 ,"bold"),bg="#FCE6C9")
label.grid(column=1,row=0)

canvas=Canvas(width=200,height=250,bg="#FCE6C9",highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(103,120,text="00:00",fill="white",font=("",30,"bold"))
canvas.grid(column=1,row=1)


b1=Button(text="Start",command=start_timer)
b1.grid(column=0,row=2)
b2=Button(text="Reset",command=reset_timer)
b2.grid(column=2,row=2)

label1 = Label(text="\u2713", fg="#008B8B", font=("", 20, "bold"), bg="#FCE6C9")
#label1.grid(column=1, row=3)


root.mainloop()