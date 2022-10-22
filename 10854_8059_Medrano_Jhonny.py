import sqlite3 #this will allow me to establish connection with the databse
import csv#SCORES
#import re
import os #Helps to open google windows
import codecs #This is used to open files inside the computer
import webbrowser #This is used to open the HTML file
from tkinter import * #This is used for the GUI
from tkinter import messagebox as ms
import tkinter.messagebox
from tkinter import messagebox
from tkinter import Tk, Button
import back

def validate(strings, chars):
    return True in [c in strings for c in chars]#This will validate inputs given by the use further on the program

conn = sqlite3.connect('students.db') #Establishes a connection to the database

c = conn.cursor()

#IF THE DATABASE IS NOT ALREADY CREATED, IT WILL CREATE IT WITH ALL THESE COLUMNS

c.execute("""CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    FirstName Text,
                    Surname Text,
                    DOB Integer,
                    Email Text,
                    Username Text,
                    Password Text)""")#This will only create a table if it isn't already

def get_selected_row(event):
    global selected_tuple #Globalised variable in order to access other functions
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    entry1.delete(0,END)
    entry1.insert(END,selected_tuple[1])
    entry2.delete(0,END)
    entry2.insert(END,selected_tuple[2])
    entry3.delete(0,END)
    entry3.insert(END,selected_tuple[3])
    entry4.delete(0,END)
    entry4.insert(END,selected_tuple[4])
    entry5.delete(0,END)
    entry5.insert(END,selected_tuple[5])
    entry6.delete(0,END)
    entry6.insert(END,selected_tuple[6])

def view_command(): #This is connected to the program "back" allows the admin to see all students in database.
    list1.delete(0,END)
    for row in back.view():
        list1.insert(END,row)

def search_command(): #Connected to backend, allows admin to search for a specific student or value
    list1.delete(0,END)
    for row in back.search(Name_text.get(),Surname_text.get(),DoB_text.get(),Email_text.get(),Username_text.get(),Password_text.get()): #Gets all results found to those specific values entered
        list1.insert(END,row)#Shows results in extended entry

def add_command():
    back.insert(Name_text.get(),Surname_text.get(),DoB_text.get(),Email_text.get(),Username_text.get(),Password_text.get())
    list1.delete(0,END)
    list1.insert(END,Name_text.get(),Surname_text.get(),DoB_text.get(),Email_text.get(),Username_text.get(),Password_text.get())

def delete_command():
    back.delete(selected_tuple[0])

def update_command():
    back.update(selected_tuple[0],Name_text.get(),Surname_text.get(),DoB_text.get(),Email_text.get(),Username_text.get(),Password_text.get())

def registration():
    
    window=Tk()  

    label1=Label(window,text="Students' Login Details")#Declares the name for label1
    label1.grid(row=0,column=2)#Declares the position of label1

    label2=Label(window,text="Name")#Declares the name for label2
    label2.grid(row=1,column=0)#Declares the position of label2

    label3=Label(window,text="Surname")#Declares the name for label3
    label3.grid(row=2,column=0)#Declares the position of label3

    label4=Label(window,text="DoB")#Declares the name for label4
    label4.grid(row=3,column=0)#Declares the position of label4

    label5=Label(window,text="Email")#Declares the name for label5
    label5.grid(row=4,column=0)#Declares the position of label5

    label6=Label(window,text="Username")#Declares the name for label6
    label6.grid(row=5,column=0)#Declares the position of label6

    label7=Label(window,text="Password")#Declares the name for label7
    label7.grid(row=6,column=0)#Declares the position of label7

    #GLOBALISED VARIABLES SO THEY CAN BE ACCESSED ANYTIME THEY ARE CALLED
    
    global entry1
    global Name_text
    Name_text=StringVar()
    entry1=Entry(window,textvariable=Name_text)
    entry1.grid(row=1,column=1)#Declares the position of entry1

    global entry2
    global Surname_text
    Surname_text=StringVar()
    entry2=Entry(window,textvariable=Surname_text)
    entry2.grid(row=2,column=1)#Declares the position of entry2

    global entry3
    global DoB_text
    DoB_text=StringVar()
    entry3=Entry(window,textvariable=DoB_text)
    entry3.grid(row=3,column=1)#Declares the position of entry3

    global entry4
    global Email_text
    Email_text=StringVar()
    entry4=Entry(window,textvariable=Email_text)
    entry4.grid(row=4,column=1)#Declares the position of entry4

    global entry5
    global Username_text
    Username_text=StringVar()
    entry5=Entry(window,textvariable=Username_text)
    entry5.grid(row=5,column=1)#Declares the position of entry5

    global entry6
    global Password_text
    Password_text=StringVar()
    entry6=Entry(window,textvariable=Password_text)
    entry6.grid(row=6,column=1)#Declares the position of entry6
    
    global list1
    list1=Listbox(window,height=20,width=59)
    list1.grid(row=1,column=3, rowspan=6, columnspan=2)#Declares the position of

    scrl=Scrollbar(window)
    scrl.grid(row=1,column=2, sticky='ns',rowspan=6)

    list1.configure(yscrollcommand=scrl.set)
    scrl.configure(command=list1.yview)#Binds the scrollbar to the list

    list1.bind('<<ListboxSelect>>',get_selected_row)

    b1=Button(window,text="View all",width=12, command=view_command)
    b1.grid(row=7, column=0)#Declares the position of B1

    b2=Button(window,text="Add entry",width=12,command=add_command)
    b2.grid(row=9, column=0)#Declares the position of B2

    b3=Button(window,text="Delete entry",width=12,command=delete_command)
    b3.grid(row=11, column=0)#Declares the position of B3

    b4=Button(window,text="Search",width=12,command=search_command)
    b4.grid(row=7, column=1)#Declares the position of B4

    b5=Button(window,text="Update",width=12,command=update_command)
    b5.grid(row=9, column=1)#Declares the position of B5

    b6=Button(window,text="Further Options",width=12,command=menu2)
    b6.grid(row=11, column=1)#Declares the position of B6
    
    window.attributes("-topmost", True)#Prioritises the GUI


    window.mainloop()

def menu (): #SHOWS THE MENY TO STUDENTS ONCE THEY HAVE LOGGED IN

    
    def Create():
        
        Names = []
        Scores = []
        Scores.append(counter)#ADDS THE USERS POINTS TO THE ARRAY SCORES
        Name = ""
        while Name == "" or Name.isnumeric() == True:#ONLY ACCEPTS STRINGS
            Name = input("Enter your first name: ")
        Names.append(Name)#ADDS THE NAME OF THE USER TO THE ARRAY NAMES
        Score = open("Score.csv","a+")#CREATES CSV FILE IF IT DOESNT EXIST ALREADY
        with open("Score.csv","a", newline="") as file:#DOESN'T SKIP ANY ROWS.
            writer = csv.writer(file)
            writer.writerow((Names, Scores))#WRITES BOTH NAME AND SCORES IN DIFFERENT COLUMNS NEXT TO EACH OTHER
                
    def quiz():#DISPLAYS THE QUIZ ONCE THE USER CLICKS START QUIZ IN THE MENU
        root.destroy()

        global counter#SO IT CAN BE APPENDED INTO THE ARRAY

        counter = 0#COUNTER STARTS AT 0

        print("1.Demand Curve")
        print("2.Supply Curve")
        print("3.AD")
        print("4.AS")
        valid = False
        while not valid:
            q1 = input("Which curve slops upwards? ")
            if not validate(q1,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q1 == "2":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")

        print("\n")#LEAVES A NEW LINE
        print("1.Leather")
        print("2.Pork")
        print("3.Gravy")
        print("4.Fish")
        valid = False
        while not valid:
            q2 = input("Which of the following products are in joint supply with meat?")
            if not validate(q2,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print ("Answer is not valid")
            else:
                valid = True
        if q2 == "1":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")

        print("\n")#LEAVES A NEW LINE
        print("1.Elastic demand for exported goods")
        print("2.Elastic demand for imported goods")
        print("3.Inelastic demand for exported goods")
        print("4.Inelastic demand for imported goods")
        valid = False
        while not valid:
            q3 = input("Which of the follwoing would reduce the impact of a tarrif?")
            if not validate(q3,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q3 == "4":
            counter = counter + 1
        else:
            print("Incorrect")

        print("\n")#LEAVES A NEW LINE
        print("1.Derived supply")
        print("2.Structural Unemployment")
        print("3.Derived Demand")
        print("4.Seasonal Unemployment")
        valid = False
        while not valid:
            q4 = input("The demand for construction workers being dependent on the demand for new housing referred to as")
            if not validate(q4,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q4 == "3":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")
            
        print("\n")#LEAVES A NEW LINE
        print("1.Imports")
        print("2.Savings")
        print("3.Taxes")
        print("4.Exports")
        valid = False
        while not valid:
            q5 = input("An increase in which of the following will directly lead to an increase in AD")
            if not validate(q5,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q5 == "4":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")

        print("\n")#LEAVES A NEW LINE
        print("1.Fall in the availability of credit")
        print("2.Rise in corporation tax")
        print("3.Fall in the expected rate of return")
        print("4.Fall in the cost of borrowing")
        valid = False
        while not valid:
            q6 = input("Which of these factors is most likely to lead an increase in investment spending by firms?")
            if not validate(q6,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q6 == "4":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")
            
        print("\n")#LEAVES A NEW LINE
        print("1.Solicitor")
        print("2.Lawyer")
        print("3.Fast food restaurant employee")
        print("4.University Professor")
        valid = False
        while not valid:
            q7 = input("Which of these jobs is likely to have a more elastic supply?")
            if not validate(q7,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q7 == "3":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")
            
        print("\n")#LEAVES A NEW LINE
        print("1.Falling income tax receipts")
        print("2.A rise in company profits")
        print("3.Fewer people claiming Job Seekers Allowance")
        print("4.A rising rate of inflation")
        valid = False
        while not valid:
            q8 = input("Each of the following is a characteristic of a positive output gap except")
            if not validate(q8,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q8 == "1":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")
            
        print("\n")#LEAVES A NEW LINE
        print("1.GDP")
        print("2.Expected years of schooling")
        print("3.GNI per capita")
        print("4.Mean years of schooling")
        valid = False
        while not valid:
            q9 = input("Which of the following is not part of the HDI")
            if not validate(q9,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q9 == "1":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")

        print("\n")#LEAVES A NEW LINE
        print("1.A reduction in the base rate of interest in the economy")
        print("2.An increase in import volumes")
        print("3.An increase in export volumes")
        print("4.A reduction in inwards foreign investment")
        valid = False
        while not valid:
            q10 = input("Which one of the following is likely to cause appreciation of a country's currency?")
            if not validate(q10,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q10 == "3":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")
            
        print("\n")#LEAVES A NEW LINE
        print("1.An ageing population")
        print("2.A rise in employment")
        print("3.Reduced spending on public services")
        print("4.A rise in the income tax rate")
        valid = False
        while not valid:
            q11 = input("Which of the following is most likely to increase the size of the fiscal deficit?")
            if not validate(q11,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q11 == "1":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")
            
        print("\n")#LEAVES A NEW LINE
        print("1.AD is likely to rise")
        print("2.There would be downward pressure on real incomes")
        print("3.Import volumes may rise")
        print("4.UK goods and services will become less competitive")
        valid = False
        while not valid:
            q12 = input("Which one of the following is the likely consequence of a rise in the unemployment rate?")
            if not validate(q12,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q12 == "2":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")

        print("\n")#LEAVES A NEW LINE
        print("1.To meet the extra demand")
        print("2.To make profit")
        print("3.To benefit society")
        print("4.To use up unused resources")
        valid = False
        while not valid:
            q13 = input("What is the most likely reason for a firm to supply more when the price of a good increases?")
            if not validate(q13,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q13 == "2":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")

        print("\n")#LEAVES A NEW LINE
        print("1.£1")
        print("2.£19")
        print("3.-£1")
        print("4.£29")
        valid = False
        while not valid:
            q14 = input("If total costs rise from £300 to £319 and average costs fall from £30 to 29 how much is marginal cost?")
            if not validate(q14,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q14 == "2":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")

        print("\n")#LEAVES A NEW LINE
        print("1.A shift to the right in the AD curve")
        print("2.A shift to the left in the short run AS curve")
        print("3.A shift to the right in the long run AS curve")
        print("4.A shift to the right in the sort run aggregate supply curve")
        valid = False
        while not valid:
            q15 = input("A fall in the cost of imported raw mateirals is likely to lead to")
            if not validate(q15,"1234"):#MAKES SURE ONLY OPTIONS 1 TO 4 ARE ACCEPTED
                print("Answer is not valid")
            else:
                valid = True
        if q15 == "4.":
            counter = counter+1#INCREMENTS COUNTER IF ANSWER IS CORRECT
        else:
            print("Incorrect")
            print("\n")#LEAVES A NEW LINE


#THE COUNTER IS CHECKED BETWEEN THESE RANGES AND OUTPUTS FEEDBACK DEPENDING ON THEIR SCORE
        if 0 <= counter <=3:
            print("Don't worry you have plenty of time to revise and catch up, your score was",counter)
        elif 3< counter <=6:
            print("hehe, you're doing  well, keep it up, your score was",counter)
        elif 6 < counter <=9:
            print("Damn, keep working like this and you will get an A in that exam, your score was,",counter)
        elif 9 < counter <=12:
            print("Uhh, you were so close to getting full marks, your score was",counter)
        elif 12 < counter <=14:
            print("Alright Economics geek, we get it now, you're the best, you're score was",counter)
        elif counter == "15":
            print("Well, you my friend, got full marks, just go and take a day off")

        Create()#CALLS THE FUNCTION TO SAVE THE NAME AND THE SCORE TO CSV FILE
        menu()#DISPLAYS MENU AGAIN


#SHOWN IN MENU, USED TO OPEN REVISION WEBSITE            
    def Revision():
        new = 2
        url= "file:///E:/A%20level%20computing/Programming%20Project/check.html"#HTML NAME
        webbrowser.open(url,new=new)#REDIRECT TO THE HTML, MAKES SURE IT OPENS IT IN BROWSER


#SHOWS THE RESULTS WHEN THE USER CLICKS THE OPTION
    def results():
        with open("Score.csv","r",newline="") as file:
            List = list(csv.reader(file))
            for row in List:
                print(row)

#IF USER EXISTS IT WILL REDIRECT THEM BACK THE LOGIN MENU
    def last():
        root.destroy()#CLOSES MENU
        login()#OPENS LOGIN SYSTEM

#LAYOUT OF MENU
    root= Tk()
    root.geometry("250x250")
    root.title("Menu")
    root.configure(background='grey')

    b1=Button(root,text="Start Quiz",width=12,bg="grey",fg="white",command=quiz)
    b1.place(x=75,y=50)#Places button 1 in the given position

    b2=Button(root,text="Access Revision Website",width=20,bg="grey",fg="white",command=Revision)
    b2.place(x=50,y=100)

    b3=Button(root,text="View Class Scores", width=20,bg="grey",fg="white",command =results)
    b3.place(x=50,y=150)#Places button 1 in the given position

    b4=Button(root,text="Exit",width=12,bg="grey",fg="white",command=last)
    b4.place(x=75,y=200)#Places button 4 in the given position

    root.attributes("-topmost", True)#PRIORITISES THE MENU, PUTS IT ON TOP OF EVERY OTHER WINDOW
    
    root.mainloop()

def menu2():

    def results():
        with open("Score.csv","r",newline="") as file:
            List = list(csv.reader(file))
            for row in List:
                print(row)
    
    root= Tk()
    root.geometry("250x250")
    root.title("Furhter Options")
    root.configure(background='grey')

    b1=Button(root,text="Open Score Board",width=12,bg="grey",fg="white",command=results)
    b1.place(x=50,y=50)#Places button 1 in the given position

    b3=Button(root,text="Exit",width=12,bg="grey",fg="white",command=root.destroy)
    b3.place(x=50,y=150)#Places button 1 in the given position

    root.attributes("-topmost", True)#PRIORITISES THE MENU, PUTS IT ON TOP OF EVERY OTHER WINDOW
    
    root.mainloop()
    

def login():
    root =Tk()#Creates GUI
    root.geometry("500x600")#This establishes how big the window opened will be
    root.title("Economics Quiz.")#Title of the window that has been opened

#THIS IS THE POP UP THAT SHOWS WHEN THE USER WANTS TO EXIT, IT ASKS THEM TO CONFIRM
    def close():
        close = messagebox.askyesno("Economics Quiz","Confirm if you want to exit")
        if close == True: 
            root.destroy()#CLOSES THE TKINTER OF THE LOGIN WINDOW
            main()#CALLS THE MAIN SUBROUTINE, STARTS THE PROCESS AGAIN
        else:
            pass#KEEPS THE TKINTER WINDOW OPEN
        
#THIS IS TO VALIDATE THE TKINTER ENTRIES WITHIN THE WINDOW OF THE LOGIN SYSTEM
        
    def login1():
        #Establish Connection
        with sqlite3.connect('students.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM students WHERE username = ? and password = ?')
        c.execute(find_user,[(Username.get()),(Password.get())])
        result = c.fetchall()#CHECKS THE DATABASE 
        if result:
#THIS SHOWS ANOTHER POP UP TO MAKE SURE THE USER IS A STUDENT OR A TEACHER, ONLY IF THE USERNAME AND PASSWORD WERE FOUND
            if messagebox.askyesno("Question","Are you a student?") == True:
                root.destroy()#CLOSES THE TKINTER WINDOW
                menu()#DISPLAYS THE MENU AGAIN
            else:
                Username.get()
                root.destroy()#CLOSES 
                registration()
        else:
            ms.showerror('Oops!','Username Not Found or Password does not match.')

    def Wclose():
        root.destroy()
        main()
        
    Username=StringVar()
    Password=StringVar()
    
    root.configure(background='grey')

    label1=Label(root,text="Login System",relief = "solid",width=20,font=("arial",19,"bold"))
    label1.place(x=90,y=53)#Places Label 1 in the given position

    label2=Label(root,text="Username: ",width=10,font=("arial",10,"bold"))
    label2.place(x=90,y=130)#Places Label 2 in the given position

    label3=Label(root,text="Password: ",width=10,font=("arial",10,"bold"))
    label3.place(x=90,y=180)#Places Label 3 in the given position

    entry1=Entry(root,textvar=Username)
    entry1.place(x=185,y=130)#Places Entry 1 in the given position
    entry1.focus_force()

    entry2=Entry(root,show="*",textvar=Password)
    entry2.place(x=185,y=180)#Places Entry 2 in the given position

    b1=Button(root,text="Exit",width=12,bg="grey",fg="white",command=root.destroy)
    b1.place(x=200,y=350)#Places button 1 in the given position

    b2=Button(root,text="Log in",width=12,bg="grey",fg="white",command=login1)
    b2.place(x=200,y=300)


    root.attributes("-topmost", True)
    
    root.protocol('WM_DELETE_WINDOW', close)
    
    root.mainloop()

#THIS IS TO ENSURE THE USER HAS AN ACCOUNT OR NOT
def log_in():
    
    log_in = ""
    while log_in!= "Y" and log_in!="N":
        log_in = input("Do you have an account? Y/N: ").upper()#THIS FUNCTION PUTS EVERY INPUT IN CAPITAL LETTERS
    if log_in == "N":
        user_profile()#CALLS THE FUNCTION
        print("Please log in...")
        login()
        main()
    elif log_in == "Y":
        print("Please log in...")
        login()
        main()

#THIS IS WHAT IS IN CHARGE OF VALIDATING THE EMAIL
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
def check(Email):
    if(re.search(regex,Email)):  
        print("Valid Email")        
    else:  
        print("Invalid Email")

#THIS FUNCTION IS IN CHARGE OF COLLECTING THE USERS DETAILS
def user_profile():
        
    sign_up = ""
    while sign_up!= "Y" and sign_up!= "N":
        sign_up = input("Do you want to create an account? Y/N: ").upper()#THIS FUNCTION PUTS EVERY INPUT IN CAPITAL LETTERS
        while sign_up == "N":
            if sign_up == "N":
                print("You have to create an account to participate in the quiz.")
                sign_up = input("Do you want to create an account? Y/N: ").upper()#THIS FUNCTION PUTS EVERY INPUT IN CAPITAL LETTERS

    if sign_up == "Y":
    
        FirstName = ""
        while FirstName == "" or FirstName.isnumeric() == True:#ONLY STRINGS ARE ACCEPTED
            FirstName = input("Enter your first name: ")

        Surname = ""
        while Surname == "" or Surname.isnumeric() == True:#ONLY STRINGS ARE ACCEPTED
            Surname = input("Enter your surname: ")


        DOB = ""
        print("Dont leave any space between day, month and year")
        while DOB.isnumeric() == False:
            DOB = input("What is your Date of Birth? ")
            
        global Email
        Email = ""
        print("Please enter a valid email.")
        while Email == "":
            Email = input("Enter your email: ")
            check(Email)#CHECKS THE EMAIL

#THE USERNAME HAS TO BE VALIDATED AND CHECKED TO SEE IF IT HAS BEEN TAKEN OR NOT

        Username = ""
        while Username == "":
            Username = input("Create a username: ")
            i=0
            c.execute('SELECT Username FROM students')
            result=c.fetchall()
            for i in range(len(result)):
                if result[i][0] == Username:
                    print("Your username is taken")                
                while result[i][0] == Username:
                    Username = ""
                    while Username == "":   
                        Username = input("Create a username: ")
                        if result[i][0] == Username:
                            print("Your username is taken")

            
        Password = ""
        print("Password should be longer than 6 characters but less than 10")
        while len(Password) <6 or len(Password)>10:#CHECKS THE LENGTH OF THE PASSWORD
            Password = input("Create a password: ")

#THIS ASSIGNS THE VARIABLE TO THE VARIABLE, THEN THIS TELLS THE PROGRAM TO ASSIGN THE VALUES INTO THE DATABASE
        FirstName = FirstName
        Surname = Surname
        DOB = DOB
        Email = Email
        Username = Username
        Password = Password
        c.execute ("INSERT INTO students (FirstName, Surname, DOB, Email, Username, Password) VALUES (?,?,?,?,?,?)",
                   (FirstName, Surname, DOB, Email, Username, Password))
        conn.commit()
        
    else:
        exit()
        
def main():
    log_in()
    user_profile()

main()#CALLS THE FUNCTIONS SO THE PROGRAM STARTS
