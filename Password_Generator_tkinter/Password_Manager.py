from tkinter import *
from tkinter import messagebox
from  random  import randint,choice,shuffle
import pyperclip
import json

root=Tk()
root.title("Password Manager")
root.geometry("600x600")
root.config(padx=50,pady=58)

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

def add_info():
    website=nameentry.get()
    email=u_entry.get()
    password=pass_entry.get()
    new_data={
        website:
                  {
                      "email":email,
                       "password":password,
                  }
    }

    if (len(website)==0 or len(password)==0):
        messagebox.askokcancel(title="Oops",
          message="Please don't leave any field empty!")

    #is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail:{email}\nPassword: {password}\nIs it ok to save?")
    else:
            try:
                f=open("data.json", "r")
                data = json.load(f)
        # reading the old data
            except:
                f = open("data.json", "w")
                json.dump(new_data, f, indent=4)
            else:
        #updating the old data
                 data.update(new_data)
        #saving update data
                 f = open("data.json", "w")
                 json.dump(data,f,indent=4)
        #use json.load(data) to read json file
        #use json.update(data) to append soething in json file
            finally:
                  nameentry.delete(0, END)
                  pass_entry.delete(0, END)

def search():
    website=nameentry.get()

    try:
        f1=open("data.json")
        data=json.load(f1)
    except:
        messagebox.showinfo(title="Error",
          message="No Data File Found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=f"{website}",message=f"Email: {email}\nPassword: {password}")
        else:
          messagebox.showinfo(title="Error",message=f"No Details for {website} exist.")

canvas=Canvas(width=200,height=200,highlightthickness=0)
tomato_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=tomato_img)
#timer_text=canvas.create_text(103,120,text="00:00",fill="white",font=("",30,"bold"))
canvas.grid(column=1,row=0)

name=Label(root,text="Website:- ")
user=Label(root,text="Email/Username:- ")
password=Label(root,text="Password :-")
name.grid(column=0,row=1)
user.grid(column=0,row=2)
password.grid(column=0,row=3)



nameentry=Entry(width=21)

nameentry.grid(row=1,column=1)
nameentry.focus()
u_entry=Entry(width=35)
pass_entry=Entry(width=21)
u_entry.grid(row=2,column=1,columnspan=2)
u_entry.insert(0, "angela@gmail.com")
pass_entry.grid(row=3,column=1)




b3=Button(text="Search",width=13,command=search)
b3.grid(column=2,row=1)
b1=Button(text="Generate Password",command=generate_password)
b1.grid(column=2,row=3)
b1=Button(text="Add",width=36,command=add_info)
b1.grid(column=1,row=4,columnspan=2)
root.mainloop()
