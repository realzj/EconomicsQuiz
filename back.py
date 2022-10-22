import sqlite3

def connect():
    conn=sqlite3.connect("students.db")#CONNECTS TO THE DATABASE "STUDENTS"
    cur=conn.cursor()
    conn.commit()
    conn.close()
    
def insert(FirstName,Surname,DOB,Email,Username,Password):
    conn=sqlite3.connect("students.db")#CONNECTS TO THE DATABASE "STUDENTS"
    cur=conn.cursor()
    cur.execute("INSERT INTO students VALUES (NULL, ?,?,?,?,?,?)",(FirstName,Surname,DOB,Email,Username,Password))#ADDS A NEW STUDENT TO THE DATABASE
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("students.db")#CONNECTS TO THE DATABASE "STUDENTS"
    cur=conn.cursor()
    cur.execute("SELECT * FROM students")#SHOWS ALL STUDENTS 
    row=cur.fetchall()
    conn.close()
    return row

def search(FirstName="",Surname="",DOB="",Email="",Username="",Password=""):#SEARCHS FOR STUDENTS DETAILS, IF THE DATABASE IS TOO LARGE THIS WILL BE USEFUL
    conn=sqlite3.connect("students.db")#CONNECTS TO THE DATABASE "STUDENTS"
    cur=conn.cursor()
    cur.execute("SELECT * FROM students WHERE FirstName=? OR Surname=? OR DOB=?  OR  Email=?  OR  Username=?  OR  Password=?",(FirstName,Surname,DOB,Email,Username,Password))
    row=cur.fetchall()
    conn.close()
    return row

def delete(id):#CHECKS ID AND DELETED ACCORDING TO THAT SPECIFIC ID
    conn=sqlite3.connect("students.db")#CONNECTS TO THE DATABASE "STUDENTS"
    cur=conn.cursor()
    cur.execute("DELETE FROM students  where id=?",(id,))#FIND THE ID AND DELETES
    conn.commit()
    conn.close()

def update(id,FirstName,Surname,DOB,Email,Username,Password):#CHECKS ID AND UPDATES THE STUDENTS DETAILS ACCORDING TO THAT SPECIFIC ID
    conn=sqlite3.connect("students.db")#CONNECTS TO THE DATABASE "STUDENTS"
    cur=conn.cursor()
    cur.execute("UPDATE students SET FirstName=? ,Surname=? , DOB=? ,  Email=? , Username=? , Password=? where id=?",(FirstName,Surname,DOB,Email,Username,Password,id))#UPDATES ACCORDING TO ID
    conn.commit()
    conn.close()

connect()
