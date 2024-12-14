from tkinter import *

def click(event):
    global value,textbox
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if value.get().isdigit():
            res=int(value.get())
        else:
            res=eval(textbox.get())
        value.set(res)
        textbox.update()
    elif text == "AC":
         value.set("")
         textbox.update()
    else:
        value.set(value.get()+text)
        textbox.update()

root=Tk()
root.title("Calculator")
root.geometry("600x800")
img=PhotoImage(file="calc.png")
root.iconphoto(False,img)


value=StringVar()
value.set("")
textbox = Entry(root,textvariable=value,justify="right" ,width=16,font="Aerial 30 bold")
textbox.grid(row=0,pady=20,padx=40)


f1=Frame(root)
b=Button(f1,text="AC",font=("Aerial",28,"bold"),padx=5,pady=18)
b.grid(row=1,column=0)
b.bind("<Button>",click)

b=Button(f1,text="%",font=("Aerial",28,"bold"),padx=15,pady=18)
b.grid(row=1,column=1)
b.bind("<Button>",click)

b=Button(f1,text=")",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=1,column=2)
b.bind("<Button>",click)

b=Button(f1,text="(",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=1,column=3)
b.bind("<Button>",click)
f1.grid(row=1)

f2=Frame(root,bg="grey")
b=Button(f2,text="7",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=2,column=0 )
b.bind("<Button>",click)

b=Button(f2,text="8",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=2,column=1)
b.bind("<Button>",click)

b=Button(f2,text="9",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=2,column=2)
b.bind("<Button>",click)

b=Button(f2,text="/",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=2,column=3)
b.bind("<Button>",click)
f2.grid(row=2,pady=10,padx=10)

f3=Frame(root,bg="grey")
b=Button(f3,text="4",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=3,column=0 )
b.bind("<Button>",click)

b=Button(f3,text="5",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=3,column=1)
b.bind("<Button>",click)

b=Button(f3,text="6",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=3,column=2)
b.bind("<Button>",click)

b=Button(f3,text="*",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=3,column=3)
b.bind("<Button>",click)

f3.grid(row=3,pady=2,padx=10)
f4=Frame(root,bg="grey")
b=Button(f4,text="1",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=4,column=0 )
b.bind("<Button>",click)

b=Button(f4,text="2",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=4,column=1)
b.bind("<Button>",click)

b=Button(f4,text="3",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=4,column=2)
b.bind("<Button>",click)

b=Button(f4,text="-",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=4,column=3)
b.bind("<Button>",click)
f4.grid(row=4,pady=12,padx=10)

f5=Frame(root,bg="grey")
b=Button(f5,text="0",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=5,column=0 )
b.bind("<Button>",click)

b=Button(f5,text=".",font=("Aerial",28,"bold"),padx=20,pady=18)
b.grid(row=5,column=1)
b.bind("<Button>",click)

b=Button(f5,text="=",font=("Aerial",28,"bold"),padx=18,pady=18)
b.grid(row=5,column=2)
b.bind("<Button>",click)

b=Button(f5,text="+",font=("Aerial",28,"bold"),padx=16,pady=18)
b.grid(row=5,column=3)
b.bind("<Button>",click)

f5.grid(row=5,pady=12,padx=10)

root.mainloop()