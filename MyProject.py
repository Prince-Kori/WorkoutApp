from tkinter import *
from PIL import Image, ImageTk
import messagebox as msg


def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()


def userLoggedIn():
    pass


def logWindow():
    clearWindow()
    global logUser, logPass
    root.title("Login")

    # Frame here
    logWinFrame = Frame(root, bg="#333333")

    lbl = Label(logWinFrame, text="Username", fg="black", bg="white", font=("celtic", 20))
    logUser = Entry(logWinFrame, font=("celtic", 20))
    lbl2 = Label(logWinFrame, text="Password", fg="black", bg="white", font=("celtic", 20))
    logPass = Entry(logWinFrame, font=("celtic", 20))
    btn = Button(logWinFrame, text="Login", fg="white", bg="green", width=15, command=clickedLoginBtn,
                 font=("celtic", 20))
    lbl3 = Label(logWinFrame, text="Don't have an account?", font=("celtic", 20))
    btn2 = Button(logWinFrame, text="Signup", command=signWindow, font=("celtic", 20))
    lbl.grid(row=0, column=0, padx=10, pady=20)
    logUser.grid(row=0, column=1, padx=10, pady=10)
    lbl2.grid(row=1, column=0, padx=10, pady=10)
    logPass.grid(row=1, column=1, padx=10, pady=10)
    btn.grid(row=2, column=0, padx=10, pady=50, columnspan=2)
    lbl3.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
    btn2.grid(row=4, column=1, padx=10, pady=30, sticky='w')

    def goback():
        userLoginSignup()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    logWinFrame.pack(pady=10)


def clickedLoginBtn():
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


def signWindow():
    clearWindow()
    global signName, signUser, signPass, signCont, signConPass
    root.title("Sign up")

    frame = Frame(root, bg="#333333")

    # Creating widgets
    lbl = Label(frame, text="Full Name", fg="black", bg="white", font=("celtic", 20))
    signName = Entry(frame, font=("celtic", 20))
    lbl2 = Label(frame, text="Username", fg="black", bg="white", font=("celtic", 20))
    signUser = Entry(frame, font=("celtic", 20))
    lbl3 = Label(frame, text="Password", fg="black", bg="white", font=("celtic", 20))
    signPass = Entry(frame, font=("celtic", 20))
    lbl4 = Label(frame, text="Confirm password", fg="black", bg="white", font=("celtic", 20))
    signConPass = Entry(frame, font=("celtic", 20))
    lbl5 = Label(frame, text="Contact", fg="black", bg="white", font=("celtic", 20))
    signCont = Entry(frame, font=("celtic", 20))
    btn = Button(frame, text="Submit", fg="white", bg="green", command=clickedSignupBtn, font=("celtic", 20))
    lbl6 = Label(frame, text="Already have an account?", font=("celtic", 20))
    bt2 = Button(frame, text="Login", command=logWindow, font=("celtic", 20))

    # Placing widgets
    lbl.grid(row=0, column=0, padx=10, pady=10)
    signName.grid(row=0, column=1, padx=10, pady=10)
    lbl2.grid(row=1, column=0, padx=10, pady=10)
    signUser.grid(row=1, column=1, padx=10, pady=10)
    lbl3.grid(row=2, column=0, padx=10, pady=10)
    signPass.grid(row=2, column=1, padx=10, pady=10)
    lbl4.grid(row=3, column=0, padx=10, pady=10)
    signConPass.grid(row=3, column=1, padx=10, pady=10)
    lbl5.grid(row=4, column=0, padx=10, pady=10)
    signCont.grid(row=4, column=1, padx=10, pady=10)
    btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    lbl6.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    bt2.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def goback():
        userLoginSignup()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=120)


def adminLogWindow():
    clearWindow()
    global logUser, logPass
    root.title("Login")

    # Frame here
    logWinFrame = Frame(root, bg="#333333")

    lbl = Label(logWinFrame, text="Username", fg="black", bg="white", font=("celtic", 20))
    logUser = Entry(logWinFrame, font=("celtic", 20))
    lbl2 = Label(logWinFrame, text="Password", fg="black", bg="white", font=("celtic", 20))
    logPass = Entry(logWinFrame, font=("celtic", 20))
    btn = Button(logWinFrame, text="Login", fg="white", bg="green", width=15, command=clickedAdminLoginBtn,
                 font=("celtic", 20))

    lbl.grid(row=0, column=0, padx=10, pady=20)
    logUser.grid(row=0, column=1, padx=10, pady=10)
    lbl2.grid(row=1, column=0, padx=10, pady=10)
    logPass.grid(row=1, column=1, padx=10, pady=10)
    btn.grid(row=2, column=0, padx=10, pady=50, columnspan=2)

    def goback():
        mainWin()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    logWinFrame.pack(pady=100)


def clickedAdminLoginBtn():
    global logUser, logPass

    user1 = logUser.get()
    pass1 = logPass.get()

    if logUser.get() == "":
        msg.showinfo("Field empty", "Enter your username")
    elif logPass.get() == "":
        msg.showinfo("Field empty", "Enter your password")
    else:
        import mysql.connector as conn
        con = conn.connect(host="localhost", user="root", password="admin", database="user_db")
        cur = con.cursor()

        query = "select * from admin_data where username = %s and password = %s"
        cur.execute(query, (user1, pass1))

        if cur.fetchone():
            print("Login successful")
            msg.showinfo("Success", "Login successful")
            adminDashboard()
        else:
            print("Login failed")
            msg.showerror("Error", "Entered wrong username or password ")

        con.close()


def adminDashboard():
    clearWindow()
    frame = Frame(root, bg="#333333")

    btn = Button(frame, text="Program", command=adminOperations, font=("celtic", 20))
    btn2 = Button(frame, text="View user analytics", command=viewUserAnalyticBtn, font=("celtic", 20))
    btn.grid(row=1, column=0, padx=10, pady=40)
    btn2.grid(row=2, column=0, padx=10, pady=40)

    def goback():
        adminLogWindow()

    backBtn = Button(root, text="<-Log out", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=100)


def adminOperations():
    clearWindow()

    frame = Frame(root, bg="#333333")
    btn = Button(frame, text="View program", command=adminViewBtn, font=("celtic", 20))
    btn2 = Button(frame, text="Add program", command=adminAddBtn, font=("celtic", 20))
    btn3 = Button(frame, text="Update program", command=adminUpdateBtn, font=("celtic", 20))
    btn4 = Button(frame, text="Delete program", command=adminDeleteBtn, font=("celtic", 20))
    btn.grid(row=0, column=0, padx=10, pady=40)
    btn2.grid(row=1, column=0, padx=10, pady=40)
    btn3.grid(row=2, column=0, padx=10, pady=40)
    btn4.grid(row=3, column=0, padx=10, pady=40)

    def goback():
        adminDashboard()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=100)


def adminViewBtn():
    pass
    # import mysql.connector as conn
    # con = conn.connect(host="localhost", user="root", password="admin", database="user_data")
    # cur = con.cursor()
    # cur.execute("select * from program_data")
    # con.commit()
    # con.close()


def adminAddBtn():
    clearWindow()
    frame = Frame(root, bg="#333333")

    # Creating widgets
    lbl = Label(frame, text="Enter program you want to add:", font=("celtic", 30))
    addlbl = Label(frame, text="Title", font=("celtic", 20))
    addEnt = Entry(frame, font=("celtic", 20))
    addlbl1 = Label(frame, text="Description", font=("celtic", 20))
    addtxt = Text(frame, height=3, width=30, font=("celtic", 20))
    addlbl2 = Label(frame, text="Execution", font=("celtic", 20))
    addtxt2 = Text(frame, height=3, width=30, font=("celtic", 20))
    addlbl3 = Label(frame, text="Duration", font=("celtic", 20))
    addEnt2 = Entry(frame, font=("celtic", 20))
    btn1 = Button(frame, text="Add", font=("celtic", 20), command=clickedAdminAddbtn)

    # Placing widgets
    lbl.grid(row=0, column=0, columnspan=2, padx=20, pady=40)
    addlbl.grid(row=1, column=0, padx=20, pady=20)
    addEnt.grid(row=1, column=1)
    addlbl1.grid(row=2, column=0, padx=20, pady=40)
    addtxt.grid(row=2, column=1)
    addlbl2.grid(row=3, column=0, padx=20, pady=40)
    addtxt2.grid(row=3, column=1)
    addlbl3.grid(row=4, column=0, padx=20, pady=20)
    addEnt2.grid(row=4, column=1)
    btn1.grid(row=5, columnspan=2, pady=40)

    def goback():
        adminOperations()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=50)


def clickedAdminAddbtn():
    pass
#     global addEnt,addtxt, addtxt2, addEnt2
#         addEnt_1 = addEnt.get()
#         addtxt_1 = addtxt.get(1.0, END)
#         addtxt2_1 = addtxt2.get(1.0, END)
#         addEnt2_1 = addEnt2.get()
#
#     if addEnt.get() == "":
#         msg.showinfo("Empty field", "Enter title")
#     elif addtxt.get(1.0, END) == "":
#         msg.showinfo("Empty field", "Enter description")
#
#     elif addtxt2.get(1.0, END) == "":
#         msg.showinfo("Empty field", "Enter execution")
#
#     elif addEnt2.get() == "":
#         msg.showinfo("Empty field", "Enter duration")
#
#     else:
#         import mysql.connector as conn
#         con = conn.connect(host="localhost", user="root", password="admin", database="user_data")
#         cur = con.cursor()
#         query = "insert into program data(title,description,execution,duration) values(%s, %s, %s, %s)"
#         values = (addEnt_1, addtxt_1, addtxt2_1, addEnt2_1)
#         cur.execute(query, values)
#
#         con.commit()
#         con.close()


def adminUpdateBtn():
    pass


def adminDeleteBtn():
    pass


def viewUserAnalyticBtn():
    pass


def userLoginSignup():
    clearWindow()
    userFrame = Frame(root, bg="#333333")
    userFrame.pack()
    image = Image.open("images/login image.jpg")
    image = image.resize((300, 300))
    photo = ImageTk.PhotoImage(image)
    label = Label(userFrame, image=photo, anchor=W)
    label.image = photo
    label.grid(row=0, column=0, columnspan=2, padx=20, pady=60)

    log = Button(userFrame, text="Login", width=15, fg="white", bg="#00d2ff", activebackground="#73e6ff",
                 activeforeground="white",
                 command=logWindow, font=("celtic", 20))
    sign = Button(userFrame, text="Sign up", width=15, fg="white", bg="#00d2ff", activebackground="#73e6ff",
                  activeforeground="white",
                  command=signWindow, font=("celtic", 20))

    log.grid(row=2, column=0, rowspan=2, padx=10, pady=10)
    sign.grid(row=2, column=1, rowspan=2, padx=10, pady=10)

    def goback():
        mainWin()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)


root = Tk()
root.geometry("1960x1080")
root.attributes('-fullscreen', True)

root.title("Welcome")
root.config(bg="#333333")


def mainWin():
    clearWindow()

    frame = Frame(root, bg="#333333")
    frame.pack()

    # Load images
    user_img = Image.open("images/user_image.png")
    user_img = user_img.resize((300, 300))  # Resize image
    user_img = ImageTk.PhotoImage(user_img)  # Convert to PhotoImage

    admin_img = Image.open("images/admin_image.png")
    admin_img = admin_img.resize((300, 300))  # Resize image
    admin_img = ImageTk.PhotoImage(admin_img)  # Convert to PhotoImage

    # Button with images
    lbl = Label(frame, text="Select user:", font=("celtic", 30))
    adminBtn = Button(frame, image=admin_img, text="Admin", command=adminLogWindow, font=("celtic", 20), compound="top")
    userBtn = Button(frame, image=user_img, text="User", command=userLoginSignup, font=("celtic", 20), compound="top")
    quitBtn = Button(frame, text="Quit", font=("celtic", 20))
    adminBtn.image = user_img  # Keep reference to the image
    userBtn.image = admin_img  # Keep reference to the image
    lbl.grid(row=0, columnspan=3, padx=100, pady=50)
    adminBtn.grid(row=1, column=1, padx=100, pady=100)
    userBtn.grid(row=1, column=2, padx=100, pady=100)
    quitBtn

mainWin()
# adminAddBtn()
root.mainloop()

# insert into program_data(title,description,execute,duration) values("Biceps","Barbell curl, Dumbell curl, Hammer curl","3 set of 10 reps, 3 set of 10 reps,  3 set of 10 reps","30min");
# create table program_data(id int auto_increment primary key,title varchar(50),description varchar(200),duration varchar(50));
