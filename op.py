#SCHOOL MANAGEMENT SYSTEM
print ("************************WELCOME TO SCHOOL MANAGEMENT SYSTEM************************")
import mysql.connector as mys
mydb=mys.connect(host="localhost",user="root",passwd="user")
if mydb.is_connected():
    print("successfully connected")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists pyschool")
mycursor.execute("use pyschool")
mycursor.execute("create table if not exists pystudent(name varchar(50) not null,class varchar(25) not null,roll_no varchar(25) not null,gender char(1))")
mycursor.execute("create table if not exists pystaff(name varchar(50) not null,salary varchar(25) not null,subject varchar(25) not null,gender char(1))")
mydb.commit()
while(True):
    print("1.Enter data for new student")
    print("2.Enter data for new staff")
    print("3.search student")
    print("4.search staff")
    print("5.remove student record")
    print("6.remove staff record")
    print("7.Exit")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        name=str(input("enter name:"))
        classs=str(input("enter class:"))
        roll_no=str(input("enter roll number:"))
        gender=str(input("enter gender(M/F):"))
        mycursor.execute("insert into pystudent values('"+name+"','"+classs+"','"+roll_no+"','"+gender+"')")
        mydb.commit()
        print("##student record saved successfully##")
    elif(ch==2):
        sname=str(input("enter staff member name:"))
        gender=str(input("enter gender(M/F):"))
        dep=str(input("enter department or subject:"))
        sal=int(input("enter salary:"))
        mycursor.execute("insert into pystaff values('"+sname+"','"+str(sal)+"','"+dep+"','"+gender+"')")
        mydb.commit()
        print("##staff record saved successfully##")
    elif(ch==3):
       roll_no=str(input("enter student rollno:"))
       mycursor.execute("select * from pystudent where roll_no='"+roll_no+"'")
       for i in mycursor:
           name,classs,roll_no,gender=i
           print(f"Name-{name}")
           print(f"class-{classs}")
           print(f"roll number-{roll_no}")
           print(f"gender-{gender}")
    elif(ch==4):
       name=str(input("enter name:"))
       mycursor.execute("select * from pystaff where name='"+name+"'")
       for i in mycursor:
           name,gender,dep,sal=i
           print(f"Name-{name}")
           print(f"sal-{sal}")
           print(f"dep-{dep}")
           print(f"gender-{gender}")
    elif(ch==5):
       r_no=str(input("enter roll no"))
       mycursor.execute("delete from pystudent where roll_no='"+r_no+"'")
       mydb.commit()
       print("$$student record successfully deleted$$")
    elif(ch==6):
       name=str(input("enter name"))
       mycursor.execute("delete from pystudent where name='"+name+"'")
       mydb.commit()
       print("$$staff record successfully deleted$$")
    else:
       break
    print("------------------------------------------------------------")
























       
           
           
      
