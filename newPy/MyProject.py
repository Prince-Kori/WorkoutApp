from tkinter import *
from PIL import Image, ImageTk
import messagebox as msg
import mysql.connector as conn


def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()


def userDashboard():
    clearWindow()
    global userUsername
    frame = Frame(root, bg="#333333")
    root.title(f"Welcome {userUsername}")
    lbl = Label(frame, bg="#333333", fg="#0487E2", text=f"Dashboard {userUsername},", font=("celtic", 30, "bold"))
    btn = Button(frame, text="Workout programs", font=("celtic", 20), command=userProgramBtn)
    btn2 = Button(frame, text="See your progress", font=("celtic", 20), command=userSeeProgressBtn)
    btn3 = Button(frame, text="Enter your progress", font=("celtic", 20), command=userEnterProgress)
    lbl.grid(row=0, column=0, pady=40)
    btn.grid(row=1, column=0, pady=40)
    btn2.grid(row=2, column=0, pady=40)
    btn3.grid(row=3, column=0, pady=40)

    def goback():
        logWindow()

    backBtn = Button(root, text="Logout", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=100)


def userProgramBtn():
    viewProgram()


def userSeeProgressBtn():
    global userUsername
    root2 = Toplevel(root, bg="#333333")
    root2.geometry("1800x900")
    root2.title(f"View progress - {userUsername}")
    # import mysql.connector as conn
    con = conn.connect(host="localhost", user="root", password="admin", database="user_progress")
    cur = con.cursor()
    cur.execute(f"select * from {userUsername}")
    Label(root2, text="S.no", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=0)
    Label(root2, text="Title", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=1)
    Label(root2, text="Date", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=2)
    Label(root2, text="Description", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=3)
    Label(root2, text="Execution", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=4)
    Label(root2, text="Duration", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=5)
    rows = 1
    for users in cur:
        for j in range(len(users)):
            Label(root2, text=users[j], fg="white", bg="#333333", font=("celtic", 20)).grid(row=rows, column=j, padx=30)
        rows += 1
    con.commit()
    con.close()
    root2.mainloop()


def userEnterProgress():
    clearWindow()
    global userEntTtl, userEntDate, userEntDesc, userEntExec, userEntDura, userUsername
    root.title(f"Enter your progress - {userUsername}")
    frame = Frame(root, bg="#333333")

    # Creating widgets
    lbl = Label(frame, text="Enter your progress:", bg="#333333", fg="white", font=("celtic", 30))
    addlbl = Label(frame, text="Title", bg="#333333", fg="white", font=("celtic", 20))
    userEntTtl = Entry(frame, font=("celtic", 20))
    addlbl0 = Label(frame, text="Date", bg="#333333", fg="white", font=("celtic", 20))
    userEntDate = Entry(frame, font=("celtic", 20))
    addlbl1 = Label(frame, text="Description", bg="#333333", fg="white", font=("celtic", 20))
    userEntDesc = Text(frame, height=3, width=30, font=("celtic", 20))
    addlbl2 = Label(frame, text="Execution", bg="#333333", fg="white", font=("celtic", 20))
    userEntExec = Text(frame, height=3, width=30, font=("celtic", 20))
    addlbl3 = Label(frame, text="Duration", bg="#333333", fg="white", font=("celtic", 20))
    userEntDura = Entry(frame, font=("celtic", 20))
    btn1 = Button(frame, text="Add", bg="#0487E2", fg="white", font=("celtic", 20), width=10,
                  command=clickedUserEnterProgressBtn)

    # Placing widgets
    lbl.grid(row=0, column=0, columnspan=2, padx=20, pady=40)
    addlbl.grid(row=1, column=0, padx=20, pady=20)
    userEntTtl.grid(row=1, column=1)
    addlbl0.grid(row=2, column=0, padx=20, pady=20)
    userEntDate.grid(row=2, column=1)
    addlbl1.grid(row=3, column=0, padx=20, pady=40)
    userEntDesc.grid(row=3, column=1)
    addlbl2.grid(row=4, column=0, padx=20, pady=40)
    userEntExec.grid(row=4, column=1)
    addlbl3.grid(row=5, column=0, padx=20, pady=20)
    userEntDura.grid(row=5, column=1)
    btn1.grid(row=6, columnspan=2, pady=40)

    def goback():
        userDashboard()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=50)


def clickedUserEnterProgressBtn():
    global userEntTtl, userEntDate, userEntDesc, userEntExec, userEntDura, userUsername
    userEntTtl1 = userEntTtl.get()
    userEntDate1 = userEntDate.get()
    userEntDesc1 = userEntDesc.get("1.0", "end-1c")
    userEntExec1 = userEntExec.get("1.0", "end-1c")
    userEntDura1 = userEntDura.get()

    if userEntTtl1 == "":
        msg.showinfo("Empty field", "Enter title")
    elif userEntDate1 == "":
        msg.showinfo("Empty field", "Enter date")
    elif userEntDesc1 == "":
        msg.showinfo("Empty field", "Enter description")
    elif userEntExec1 == "":
        msg.showinfo("Empty field", "Enter execution")
    elif userEntDura1 == "":
        msg.showinfo("Empty field", "Enter duration")
    else:
        # import mysql.connector as conn
        con = conn.connect(host="localhost", user="root", password="admin", database="user_progress")
        cur = con.cursor()
        query = f"INSERT INTO {userUsername}(title, date, description, execution, duration) VALUES (%s, %s, %s, %s, %s)"
        values = (userEntTtl1, userEntDate1, userEntDesc1, userEntExec1, userEntDura1)
        cur.execute(query, values)

        con.commit()
        con.close()
        msg.showinfo("Success", "Data stored successfully")
        userEntTtl.delete(0, END)
        userEntDate.delete(0, END)
        userEntDesc.delete("1.0", END)
        userEntExec.delete("1.0", END)
        userEntDura.delete(0, END)


def logWindow():
    clearWindow()
    global logUser, logPass
    root.title("Login")

    def showPassword():
        if chkVar.get():
            logPass.config(show="")
        else:
            logPass.config(show="*")

    # Frame here
    frame = Frame(root, bg="#333333")

    labl = Label(frame, text="Login", bg="#333333", fg="#0487E2", font=("celtic", 40, "bold"))
    lbl = Label(frame, text="Username", fg="white", bg="#333333", font=("celtic", 20))
    logUser = Entry(frame, font=("celtic", 20))
    lbl2 = Label(frame, text="Password", fg="white", bg="#333333", font=("celtic", 20))
    logPass = Entry(frame, font=("celtic", 20), show="*")
    chkVar = IntVar()
    chk = Checkbutton(frame, text="Show password", bg="#333333", fg="white", variable=chkVar, font=("celtic", 20),
                      command=showPassword,
                      activeforeground="white", activebackground="#333333")
    btn = Button(frame, text="Login", fg="white", bg="#0487E2", width=15, command=clickedLoginBtn,
                 font=("celtic", 20))
    lbl3 = Label(frame, text="Don't have an account?", fg="white", bg="#333333", font=("celtic", 15))
    btn2 = Button(frame, text="Signup", fg="#333333", bg="white", command=signWindow, font=("celtic", 15))

    labl.grid(row=0, column=0, columnspan=2)
    lbl.grid(row=1, column=0, padx=10, pady=20)
    logUser.grid(row=1, column=1, padx=10, pady=10)
    lbl2.grid(row=2, column=0, padx=10, pady=10)
    logPass.grid(row=2, column=1, padx=10, pady=10)
    chk.grid(row=3, column=1, columnspan=2)
    btn.grid(row=4, column=0, padx=10, pady=50, columnspan=2)
    lbl3.grid(row=5, column=0, padx=10, pady=10, columnspan=2)
    btn2.grid(row=6, column=0, padx=10, pady=30, columnspan=2)

    def goback():
        userLoginSignup()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=150)


def clickedLoginBtn():
    global logUser, logPass, userUsername

    userUsername = logUser.get()
    pass1 = logPass.get()

    if logUser.get() == "":
        msg.showinfo("Field empty", "Enter your username")
    elif logPass.get() == "":
        msg.showinfo("Field empty", "Enter your password")
    else:
        # import mysql.connector as conn
        con = conn.connect(host="localhost", user="root", password="admin", database="user_db")
        cur = con.cursor()

        query = "select * from user_data where username = %s and password = %s"
        cur.execute(query, (userUsername, pass1))

        if cur.fetchone():
            print("Login successful")
            msg.showinfo("Success", "Login successful")
            userDashboard()
        else:
            print("Login failed")
            msg.showerror("Error", "Entered wrong username or password ")
        con.close()


def clickedSignupBtn():
    global signName, signUser, signPass, signCont, signConPass, userUsername

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
    elif signPass.get() != signConPass.get():
        msg.showinfo("Confirm password", "Please make sure your passwords match.")
    else:
        # import mysql.connector as conn

        con = conn.connect(host="localhost", user="root", password="admin", database="user_db")
        cur = con.cursor()
        query = "insert into user_data (name, username, password, contact) values (%s, %s, %s, %s)"
        values = (name1, user12, pass1, cont1)
        cur.execute(query, values)
        con.commit()
        con.close()

        con = conn.connect(host="localhost", user="root", password="admin", database="user_progress")
        cur = con.cursor()
        cur.execute(
            f"create table {user12}(id int auto_increment primary key, title varchar(50), date varchar(50), description varchar(200), execution varchar(200), duration varchar(20))")
        con.commit()
        con.close()

        print("User added successfully")
        msg.showinfo("Success", "Signed up successfully")
        logWindow()


def signWindow():
    clearWindow()
    global signName, signUser, signPass, signCont, signConPass
    root.title("Sign up")

    frame = Frame(root, bg="#333333")

    # Creating widgets
    labl = Label(frame, text="Signup", bg="#333333", fg="#0487E2", font=("celtic", 40, "bold"))
    lbl = Label(frame, text="Full Name", fg="white", bg="#333333", font=("celtic", 20))
    signName = Entry(frame, font=("celtic", 20))
    lbl2 = Label(frame, text="Username", fg="white", bg="#333333", font=("celtic", 20))
    signUser = Entry(frame, font=("celtic", 20))
    lbl3 = Label(frame, text="Password", fg="white", bg="#333333", font=("celtic", 20))
    signPass = Entry(frame, font=("celtic", 20))
    lbl4 = Label(frame, text="Confirm password", fg="white", bg="#333333", font=("celtic", 20))
    signConPass = Entry(frame, font=("celtic", 20))
    lbl5 = Label(frame, text="Contact", fg="white", bg="#333333", font=("celtic", 20))
    signCont = Entry(frame, font=("celtic", 20))
    btn = Button(frame, text="Submit", fg="white", bg="#0487E2", command=clickedSignupBtn, font=("celtic", 20))
    lbl6 = Label(frame, text="Already have an account?", fg="white", bg="#333333", font=("celtic", 15))
    bt2 = Button(frame, text="Login", command=logWindow, font=("celtic", 15))

    # Placing widgets
    labl.grid(row=0, column=0, columnspan=2)
    lbl.grid(row=1, column=0, padx=10, pady=10)
    signName.grid(row=1, column=1, padx=10, pady=10)
    lbl2.grid(row=2, column=0, padx=10, pady=10)
    signUser.grid(row=2, column=1, padx=10, pady=10)
    lbl3.grid(row=3, column=0, padx=10, pady=10)
    signPass.grid(row=3, column=1, padx=10, pady=10)
    lbl4.grid(row=4, column=0, padx=10, pady=10)
    signConPass.grid(row=4, column=1, padx=10, pady=10)
    lbl5.grid(row=5, column=0, padx=10, pady=10)
    signCont.grid(row=5, column=1, padx=10, pady=10)
    btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
    lbl6.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
    bt2.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def goback():
        userLoginSignup()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=120)


def adminLogWindow():
    clearWindow()
    global logUser, logPass
    root.title("Admin login")

    def showPassword():
        if chkVar.get():
            logPass.config(show="")
        else:
            logPass.config(show="*")

    # Frame here
    frame = Frame(root, bg="#333333")

    labl = Label(frame, text="Login", bg="#333333", fg="#0487E2", font=("celtic", 40, "bold"))
    lbl = Label(frame, text="Username", fg="white", bg="#333333", font=("celtic", 20))
    logUser = Entry(frame, font=("celtic", 20))
    lbl2 = Label(frame, text="Password", fg="white", bg="#333333", font=("celtic", 20))
    logPass = Entry(frame, font=("celtic", 20), show="*")
    chkVar = IntVar()
    chk = Checkbutton(frame, text="Show password", bg="#333333", fg="white", variable=chkVar, font=("celtic", 20),
                      command=showPassword,
                      activeforeground="white", activebackground="#333333")
    btn = Button(frame, text="Login", fg="white", bg="#0487E2", width=15, command=clickedAdminLoginBtn,
                 font=("celtic", 20))

    labl.grid(row=0, column=0, columnspan=2)
    lbl.grid(row=1, column=0, padx=10, pady=20)
    logUser.grid(row=1, column=1, padx=10, pady=10)
    lbl2.grid(row=2, column=0, padx=10, pady=10)
    logPass.grid(row=2, column=1, padx=10, pady=10)
    chk.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
    btn.grid(row=4, column=0, padx=10, pady=50, columnspan=2)

    def goback():
        mainWin()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=150)


def clickedAdminLoginBtn():
    global logUser, logPass

    user1 = logUser.get()
    pass1 = logPass.get()

    if logUser.get() == "":
        msg.showinfo("Field empty", "Enter your username")
    elif logPass.get() == "":
        msg.showinfo("Field empty", "Enter your password")
    else:
        # import mysql.connector as conn
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
    root.title("Admin dashboard")
    frame = Frame(root, bg="#333333")

    lbl = Label(frame, text="Admin dashboard", bg="#333333", fg="#0487E2", font=("celtic", 30, "bold"))
    btn = Button(frame, text="Program options", command=adminOperations, font=("celtic", 20))
    btn2 = Button(frame, text="View members", command=viewMemberBtn, font=("celtic", 20))
    btn3 = Button(frame, text="View member analytics", command=viewUserAnalyticBtn, font=("celtic", 20))
    lbl.grid(row=0, column=0, pady=30)
    btn.grid(row=1, column=0, padx=10, pady=40)
    btn2.grid(row=2, column=0, padx=10, pady=40)
    btn3.grid(row=3, column=0, padx=10, pady=40)

    def goback():
        adminLogWindow()

    backBtn = Button(root, text="<-Log out", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=100)


def viewMemberBtn():
    root2 = Toplevel(root, bg="#333333")
    root2.geometry("1800x900")
    root2.title("Members")

    # import mysql.connector as conn
    con = conn.connect(host="localhost", user="root", password="admin", database="user_db")
    cur = con.cursor()
    cur.execute("select * from user_data")
    Label(root2, text="S.no", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=0)
    Label(root2, text="Name", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=1)
    Label(root2, text="Username", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=2)
    Label(root2, text="Password", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=3)
    Label(root2, text="Contact", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=4)
    rows = 1
    for users in cur:
        for j in range(len(users)):
            Label(root2, text=users[j], fg="white", bg="#333333", font=("celtic", 20)).grid(row=rows, column=j, padx=30)
        rows += 1
    con.commit()
    con.close()
    root2.mainloop()


def adminOperations():
    clearWindow()

    root.title("Admin dashboard")
    frame = Frame(root, bg="#333333")
    btn = Button(frame, text="View program", command=adminViewBtn, font=("celtic", 20), width=13)
    btn2 = Button(frame, text="Add program", command=adminAddBtn, font=("celtic", 20), width=13)
    btn3 = Button(frame, text="Update program", command=adminUpdateBtn, font=("celtic", 20), width=13)
    btn4 = Button(frame, text="Delete program", command=adminDeleteBtn, font=("celtic", 20), width=13)
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
    viewProgram()


def viewProgram():
    root2 = Toplevel(root, bg="#333333")
    root2.geometry("1800x900")
    root2.title("Programs list")
    # import mysql.connector as conn
    con = conn.connect(host="localhost", user="root", password="admin", database="user_db")
    cur = con.cursor()
    cur.execute("select * from program_data")
    Label(root2, text="S.no", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=0)
    Label(root2, text="Title", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=1)
    Label(root2, text="Description", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=2)
    Label(root2, text="Execution", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=3)
    Label(root2, text="Duration", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=4)
    rows = 1
    for users in cur:
        for j in range(len(users)):
            Label(root2, text=users[j], fg="white", bg="#333333", font=("celtic", 18)).grid(row=rows, column=j, padx=30)
        rows += 1
    con.commit()
    con.close()
    root2.mainloop()


def adminAddBtn():
    clearWindow()
    global addEnt, addtxt, addtxt2, addEnt2
    root.title("Add a program")
    frame = Frame(root, bg="#333333")

    # Creating widgets
    lbl = Label(frame, text="Enter program you want to add:", bg="#333333", fg="white", font=("celtic", 30))
    addlbl = Label(frame, text="Title", bg="#333333", fg="white", font=("celtic", 20))
    addEnt = Entry(frame, font=("celtic", 20))
    addlbl1 = Label(frame, text="Description", bg="#333333", fg="white", font=("celtic", 20))
    addtxt = Text(frame, height=3, width=30, font=("celtic", 20))
    addlbl2 = Label(frame, text="Execution", bg="#333333", fg="white", font=("celtic", 20))
    addtxt2 = Text(frame, height=3, width=30, font=("celtic", 20))
    addlbl3 = Label(frame, text="Duration", bg="#333333", fg="white", font=("celtic", 20))
    addEnt2 = Entry(frame, font=("celtic", 20))
    btn1 = Button(frame, text="Add", bg="#0487E2", fg="white", font=("celtic", 20), width=10,
                  command=clickedAdminAddbtn)

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
    global addEnt, addtxt, addtxt2, addEnt2

    addEnt_1 = addEnt.get()
    addtxt_1 = addtxt.get("1.0", "end-1c")  # Retrieves text without the trailing newline character
    addtxt2_1 = addtxt2.get("1.0", "end-1c")  # Same here
    addEnt2_1 = addEnt2.get()

    if addEnt_1 == "":
        msg.showinfo("Empty field", "Enter title")
    elif addtxt_1 == "":
        msg.showinfo("Empty field", "Enter description")
    elif addtxt2_1 == "":
        msg.showinfo("Empty field", "Enter execution")
    elif addEnt2_1 == "":
        msg.showinfo("Empty field", "Enter duration")
    else:
        # import mysql.connector as conn
        con = conn.connect(host="localhost", user="root", password="admin", database="user_db")
        cur = con.cursor()
        query = "INSERT INTO program_data (title, description, execution, duration) VALUES (%s, %s, %s, %s)"
        values = (addEnt_1, addtxt_1, addtxt2_1, addEnt2_1)
        cur.execute(query, values)

        con.commit()
        con.close()
        msg.showinfo("Success", "Data stored successfully")
        addEnt.delete(0, END)
        addtxt.delete(1.0, END)
        addtxt2.delete(1.0, END)
        addEnt2.delete(0, END)


def adminUpdateBtn():
    clearWindow()
    global program_id_entry, title_entry, description_text, execution_text, duration_entry
    root.title("Update Program")
    frame = Frame(root, bg="#333333")

    # Creating widgets
    program_label = Label(frame, text="Enter program ID you want to update:", bg="#333333", fg="white",
                          font=("celtic", 30))
    program_id_label = Label(frame, text="S.no", bg="#333333", fg="white", font=("celtic", 20))
    program_id_entry = Entry(frame, font=("celtic", 20))
    title_label = Label(frame, text="Title", bg="#333333", fg="white", font=("celtic", 20))
    title_entry = Entry(frame, font=("celtic", 20))
    description_label = Label(frame, text="Description", bg="#333333", fg="white", font=("celtic", 20))
    description_text = Text(frame, height=3, width=30, font=("celtic", 20))
    execution_label = Label(frame, text="Execution", bg="#333333", fg="white", font=("celtic", 20))
    execution_text = Text(frame, height=3, width=30, font=("celtic", 20))
    duration_label = Label(frame, text="Duration", bg="#333333", fg="white", font=("celtic", 20))
    duration_entry = Entry(frame, font=("celtic", 20))
    update_button = Button(frame, text="Update", bg="#0487E2", fg="white", font=("celtic", 20), width=10,
                           command=clickedAdminUpdateButton)

    # Placing widgets
    program_label.grid(row=0, column=0, columnspan=2, padx=20, pady=40)
    program_id_label.grid(row=1, column=0, padx=20, pady=40)
    program_id_entry.grid(row=1, column=1)
    title_label.grid(row=2, column=0, padx=20, pady=20)
    title_entry.grid(row=2, column=1)
    description_label.grid(row=3, column=0, padx=20, pady=40)
    description_text.grid(row=3, column=1)
    execution_label.grid(row=4, column=0, padx=20, pady=40)
    execution_text.grid(row=4, column=1)
    duration_label.grid(row=5, column=0, padx=20, pady=20)
    duration_entry.grid(row=5, column=1)
    update_button.grid(row=6, columnspan=2, pady=40)

    def go_back():
        adminOperations()

    back_button = Button(root, text="<-back", command=go_back, font=("celtic", 15))
    back_button.place(x=10, y=10)
    frame.pack(pady=50)


def clickedAdminUpdateButton():
    global program_id_entry, title_entry, description_text, execution_text, duration_entry
    program_id = program_id_entry.get()
    title = title_entry.get()
    description = description_text.get("1.0", "end-1c")
    execution = execution_text.get("1.0", "end-1c")
    duration = duration_entry.get()

    if program_id == "":
        msg.showinfo("Empty field", "Enter serial number")
    elif title or description or execution or duration == "":
        msg.showinfo("Empty field", "Enter something to update")
    else:
        # Connect to database
        con = conn.connect(host="localhost", user="root", password="admin", database="user_db")
        cur = con.cursor()

        query = "UPDATE program_data SET title = %s, description = %s, execution = %s, duration = %s WHERE id = %s"
        values = (title, description, execution, duration, program_id)
        cur.execute(query, values)

        con.commit()
        con.close()
        msg.showinfo("Success", "Data updated successfully")
        program_id_entry.delete(0, END)
        title_entry.delete(0, END)
        description_text.delete(1.0, END)
        execution_text.delete(1.0, END)
        duration_entry.delete(0, END)


def adminDeleteBtn():
    clearWindow()
    global delEnt

    frame = Frame(root, bg="#333333")
    lbl = Label(frame, text="Enter serial no. that you want to delete:", bg="#333333", fg="white", font=("celtic", 30))
    delEnt = Entry(frame, font=("celtic", 20))
    btn = Button(frame, text="Delete", bg="#0487E2", fg="white", font=("celtic", 20), command=clickedAdminDeleteBtn)
    lbl.grid(row=1, column=1, pady=40)
    delEnt.grid(row=2, column=1, pady=40)
    btn.grid(row=3, column=1, pady=40)

    def goback():
        adminOperations()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=150)


def clickedAdminDeleteBtn():
    global delEnt

    delEnta = int(delEnt.get())
    con = conn.connect(host="localhost", user="root", password="admin", database="user_db")
    cur = con.cursor()
    query = "delete from program_data where id = %s"
    cur.execute(query, (delEnta,))

    con.commit()
    con.close()
    msg.showinfo("Deleted", "Deleted successfully")
    delEnt.delete(0, END)


def viewUserAnalyticBtn():
    clearWindow()
    global userEntAna

    frame = Frame(root, bg="#333333")
    lbl = Label(frame, text="Enter username", bg="#333333", fg="white", font=("celtic", 30))
    userEntAna = Entry(frame, font=("celtic", 20))
    btn = Button(frame, text="Get analytics", bg="#0487E2", fg="white", font=("celtic", 20),
                 command=clickedViewUserAnalyticBtn)
    lbl.grid(row=1, column=1, pady=40)
    userEntAna.grid(row=2, column=1, pady=40)
    btn.grid(row=3, column=1, pady=40)

    def goback():
        adminOperations()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=150)


def clickedViewUserAnalyticBtn():
    global userEntAna
    root2 = Toplevel(root, bg="#333333")
    root2.geometry("1800x900")
    root2.title("Programs list")
    userEntAna1 = userEntAna.get()
    # import mysql.connector as conn
    con = conn.connect(host="localhost", user="root", password="admin", database="user_progress")
    cur = con.cursor()
    cur.execute(f"select * from {userEntAna1}")
    Label(root2, text="S.no", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=0)
    Label(root2, text="Title", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=1)
    Label(root2, text="Date", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=2)
    Label(root2, text="Description", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=3)
    Label(root2, text="Execution", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=4)
    Label(root2, text="Duration", fg="white", bg="#333333", font=("celtic", 20)).grid(row=0, column=5)
    rows = 1
    for users in cur:
        for j in range(len(users)):
            Label(root2, text=users[j], fg="white", bg="#333333", font=("celtic", 18)).grid(row=rows, column=j, padx=30)
        rows += 1
    con.commit()
    con.close()
    root2.mainloop()


def userLoginSignup():
    clearWindow()
    root.title("Welcome")

    frame = Frame(root, bg="#333333")
    image = Image.open("images/login image.jpg")
    image = image.resize((300, 300))
    photo = ImageTk.PhotoImage(image)
    label = Label(frame, image=photo, anchor=W)
    label.image = photo
    label.grid(row=0, column=0, columnspan=2, padx=20, pady=60)

    log = Button(frame, text="Login", width=15, fg="white", bg="#0487E2", activebackground="#73e6ff",
                 activeforeground="white",
                 command=logWindow, font=("celtic", 20))
    sign = Button(frame, text="Sign up", width=15, fg="white", bg="#0487E2", activebackground="#73e6ff",
                  activeforeground="white",
                  command=signWindow, font=("celtic", 20))

    log.grid(row=2, column=0, rowspan=2, padx=10, pady=10)
    sign.grid(row=2, column=1, rowspan=2, padx=10, pady=10)

    def goback():
        mainWin()

    backBtn = Button(root, text="<-back", command=goback, font=("celtic", 15))
    backBtn.place(x=10, y=10)
    frame.pack(pady=100)


def quitBtn1():
    root.destroy()


root = Tk()
# root.geometry("1960x1080")
root.attributes("-fullscreen", True)
root.title("Welcome")
root.config(bg="#333333")


def mainWin():
    clearWindow()

    root.title("Workout programs")

    frame = Frame(root, bg="#333333")

    # Load images
    user_img = Image.open("images/user_image.png")
    user_img = user_img.resize((300, 300))  # Resize image
    user_img = ImageTk.PhotoImage(user_img)  # Convert to PhotoImage

    admin_img = Image.open("images/admin_image.png")
    admin_img = admin_img.resize((300, 300))  # Resize image
    admin_img = ImageTk.PhotoImage(admin_img)  # Convert to PhotoImage

    # Button with images
    lbl = Label(frame, text="Select user:", bg="#333333", fg="white", font=("celtic", 30))
    adminBtn = Button(frame, image=admin_img, text="Admin", command=adminLogWindow, font=("celtic", 20), compound="top")
    userBtn = Button(frame, image=user_img, text="User", command=userLoginSignup, font=("celtic", 20), compound="top")
    adminBtn.image = user_img
    userBtn.image = admin_img
    lbl.grid(row=0, columnspan=3, padx=100, pady=50)
    adminBtn.grid(row=1, column=1, padx=100, pady=100)
    userBtn.grid(row=1, column=2, padx=100, pady=100)

    quitBtn = Button(frame, text="Quit", font=("celtic", 20), command=quitBtn1)
    quitBtn.grid(row=2, columnspan=3, padx=100, pady=50)
    frame.pack()


mainWin()
# adminLogWindow()
# adminDashboard()
# adminAddBtn()
# signWindow()
# adminOperations()
# logWindow()
# userLoggedIn()
# viewMemberBtn()
# adminDeleteBtn()
# userEnterProgress()
root.mainloop()

# insert into program_data(title,description,execute,duration) values("Biceps","Barbell curl, Dumbell curl, Hammer curl","3 set of 10 reps, 3 set of 10 reps,  3 set of 10 reps","30min");
# create table program_data(id int auto_increment primary key,title varchar(50),description varchar(200),duration varchar(50));
