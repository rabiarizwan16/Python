from tkinter import *
root=Tk()

def calc():
    miles=float(input.get())
    km = miles * 1.609
    kilo_to.config(text=f"{km}")

root.title("miles to km converter")
root.geometry("600x600")

input=Entry(width=20)
input.grid(column=1,row=0)

mile=Label(text="Miles")
mile.grid(column=2,row=0)

kilo=Label(text="is equal to")
kilo.grid(column=0,row=1)

kilo_to=Label(text="0")
kilo_to.grid(column=1,row=1)
k_m=Label(text="Km")
k_m.grid(column=2,row=1)


button=Button(text="Calculate",command=calc)
button.grid(column=1,row=2)

root.mainloop()

