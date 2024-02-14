from tkinter import *
from PIL import Image, ImageTk
import messagebox as msg


def loggedIn():
    pass


def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()


def logWin():
    clearWindow()
    global logUser, logPass
    root.title("Login")
    lbl = Label(root, text="Username", fg="black", bg="white")
    logUser = Entry(root)
    lbl2 = Label(root, text="Password", fg="black", bg="white")
    logPass = Entry(root)
    btn = Button(root, text="Login", fg="white", bg="green", command=clickedLogBtn)
    lbl3 = Label(root, text="Don't have an account?")
    btn2 = Button(root, text="Signup", command=signWin)
    lbl.place(x=10, y=10)
    logUser.place(x=100, y=10)
    lbl2.place(x=10, y=40)
    logPass.place(x=100, y=40)
    btn.place(x=100, y=70)
    lbl3.place(x=10, y=100)
    btn2.place(x=145, y=100)


def clickedLogBtn():
    global logUser, logPass

    user11 = logUser.get()
    pass1 = logPass.get()

    if logUser.get() == "":
        msg.showinfo("Field empty", "Enter your username")
    elif logPass.get() == "":
        msg.showinfo("Field empty", "Enter your password")
    else:
        import mysql.connector as conn
        con = conn.connect(host="localhost", user="root", password="admin", database="user_db")
        cur = con.cursor()

        query = "select * from user_data where username = %s and password = %s"
        cur.execute(query, (user11, pass1))

        if cur.fetchone():
            print("Login successful")
            msg.showinfo("Success", "Login successful")
        else:
            print("Login failed")
            msg.showerror("Error", "Entered wrong username or password ")
        con.close()


def clickedSignupBtn():
    global signName, signUser, signPass, signCont, signConPass

    name1 = signName.get()
    user12 = signUser.get()
    pass1 = signPass.get()
    cont1 = signCont.get()

    if signName.get() == "":
        msg.showinfo("Field empty", "Fill your name")
    elif signUser.get() == "":
        msg.showinfo("Field empty", "Fill your username")
    elif signPass.get() == "":
        msg.showinfo("Field empty", "Fill your password")
    elif signConPass.get() == "":
        msg.showinfo("Field empty", "Confirm your password")
    elif signCont.get() == "":
        msg.showinfo("Field empty", "Fill your contact")
    else:
        import mysql.connector as conn

        con = conn.connect(host="localhost", user="root", password="admin", database="user_db")
        cur = con.cursor()

        query = "insert into user_data (name, username, password, contact) values (%s, %s, %s, %s)"
        values = (name1, user12, pass1, cont1)
        cur.execute(query, values)

        con.commit()
        con.close()

        print("User added successfully")
        msg.showinfo("Success", "Signed up successfully")


def signWin():
    clearWindow()
    global signName, signUser, signPass, signCont, signConPass
    root.title("Sign up")
    lbl = Label(root, text="Full Name", fg="black", bg="white")
    lbl.place(x=10, y=10)
    signName = Entry(root)
    signName.place(x=100, y=10)
    lbl2 = Label(root, text="Username", fg="black", bg="white")
    lbl2.place(x=10, y=40)
    signUser = Entry(root)
    signUser.place(x=100, y=40)
    lbl3 = Label(root, text="Password", fg="black", bg="white")
    lbl3.place(x=10, y=70)
    signPass = Entry(root)
    signPass.place(x=100, y=70)
    lbl4 = Label(root, text="Confirm password", fg="black", bg="white")
    lbl4.place(x=10, y=100)
    signConPass = Entry(root)
    signConPass.place(x=140, y=100)
    lbl5 = Label(root, text="Contact", fg="black", bg="white")
    lbl5.place(x=10, y=130)
    signCont = Entry(root)
    signCont.place(x=100, y=130)
    btn = Button(root, text="Submit", fg="white", bg="green", command=clickedSignupBtn)
    btn.place(x=100, y=160)
    lbl6 = Label(root, text="Already have an account?")
    lbl6.place(x=10, y=190)
    bt2 = Button(root, text="Login", command=logWin)
    bt2.place(x=155, y=190)


def admin1():
    pass


def user1():
    clearWindow()
    image = Image.open("images/login image.jpg")
    image = image.resize((200, 200))
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo, anchor=W)
    label.image = photo
    label.place(x=80, y=90)

    log = Button(root, text="Login", fg="white", bg="#00d2ff", activebackground="#73e6ff", activeforeground="white",
                 command=logWin, font=("Arial", 20, "bold"))
    log.place(x=360, y=115)
    sign = Button(root, text="Sign up", fg="white", bg="#00d2ff", activebackground="#73e6ff", activeforeground="white",
                  command=signWin, font=("Arial", 20, "bold"))
    sign.place(x=348, y=200)


root = Tk()
root.geometry("600x400")
root.title("Welcome")
root.resizable(False, False)

adminBtn = Button(root, text="Admin", command=admin1, font=("arial", 20))
userBtn = Button(root, text="User", command=user1, font=("arial", 20))
adminBtn.place(x=130, y=160)
userBtn.place(x=360, y=160)

root.mainloop()
