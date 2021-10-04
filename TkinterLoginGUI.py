# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 15:06:36 2021

@author: mendesr
"""

from tkinter import *
from tkinter import messagebox
window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('250x250')

def user_Register_Window():
    new = Toplevel(window)
    new.geometry("250x250")
    new.title("Registration")
   
    userlbl = Label(new,text="New Username:").grid(row=1, column=0)
    passwlbl = Label(new, text="New Password:").grid(row=2, column=0)
#Initialize username and password input variable prior + dont forget textvariable = in the entry widget to connect the value to inputUsername
    userInput = StringVar()
    passwInput = StringVar()
        

    userInput_Entry = Entry(new, width=20,textvariable=userInput, cursor="xterm").grid(row=1, column=1)
    passwInput_Entry = Entry(new, width=20,textvariable=passwInput, cursor="xterm", show="*").grid(row=2, column=1)
    

    print(str(userInput.get()))
#Not 100% but lamda only calls the function when it needs to it works perfetly
    registrationBtn= Button(new, text="Create Account", command=lambda: user_Register_Account(userInput,passwInput)).grid(row=4, column=1)
    

def user_Register_Account(userInput,passwInput):
#Create txt file credentials and write in the password and user passed in when the function was called
    credentials = open("credentials.txt", "a")
    credentials.write(f"Username,{userInput.get()},Password,{passwInput.get()},\n")
    messagebox.showinfo("my message","Account created!")

    credentials.close()
    
    
    

    
    
def validate(loginUsername, loginPassword):
    username = loginUsername.get()
    password = loginPassword.get()
    
    with open("credentials.txt", "r") as credentials:
        for line in credentials:
            line = line.split(",")
            if line[1] == username and line[3] == password:
                window.withdraw()
                home = Toplevel(window)
                home.geometry("250x250")
                home.title("Home")
                home()
            else:
                messagebox.showerror("Error", "Incorrect username or password")


def user_Login(loginUsername,loginPassword):
    i = 1;
    if i == 1:
        print("Hi bro")
        print(loginUsername.get())
        print(loginPassword.get())
        
    else:
        print("no bro")

lbl = Label(window,font='Times 15' ,text="RADASA").grid(column=2, row=1)
Label(text = ' Username ',font='Times 15').grid(row=3,column=1,pady=5)
Label(text = ' Password ',font='Times 15').grid(row=4,column=1,pady=5)

loginUsername = StringVar()
loginPassword = StringVar()


userLogin_Entry = Entry(window, width=20,textvariable=loginUsername, cursor="xterm").grid(row=3,column=2,columnspan=10)
passwLogin_Entry = Entry(window, width=20,textvariable=loginPassword, cursor="xterm", show="*").grid(row=4,column=2,columnspan=10)
 


loginBTN = Button(window, text="LOGIN", command=lambda: validate(loginUsername, loginPassword)).grid(row=5,column=2)

registerBTN = Button(window, text="REGISTER",command=user_Register_Window).grid(row=5,column=3)









window.mainloop()





#