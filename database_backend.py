import mysql.connector

#backend using MYSQL
'''
def studentdata():
	con = mysql.connector.connect(host="localhost",user="rc",passwd="password123",database="student")
	cur=con.cursor()
	cur.execute("create table if not exists student(StdID integer primary key,Firstname varchar(50),Surname varchar(50), DOB varchar(30), Age varchar(10),Gender varchar(10),Address varchar(100),Mobile varchar(30));")
	con.commit()
	con.close()
'''

def addstudentrecord(StdID,Firstname,Surname,DOB,Age,Gender,Address,Mobile):
	con = mysql.connector.connect(host="localhost",user="rc",passwd="password123",database="student")
	cur = con.cursor()
	a="insert into student(StdID,Firstname,Surname,DOB,Age,Gender,Address,Mobile) values(%s,%s,%s,%s,%s,%s,%s,%s);"
	b=(StdID,Firstname,Surname,DOB,Age,Gender,Address,Mobile)
	cur.execute(a,b)
	con.commit()
	con.close()

def viewdata():
	con = mysql.connector.connect(host="localhost",user="rc",passwd="password123",database="student")
	cur = con.cursor()
	cur.execute("Select * from student")
	row=cur.fetchall()
	con.commit()
	con.close()
	return row

def deletedata(StdID):
	con = mysql.connector.connect(host="localhost",user="rc",passwd="password123",database="student")
	cur = con.cursor()
	a="delete from student where StdID="+StdID+";"
	cur.execute(a)
	con.commit()
	con.close()

def searchdata(StdID="",Firstname="",Surname="",DOB="",Age="",Gender="",Address="",Mobile=""):
	con = mysql.connector.connect(host="localhost",user="rc",passwd="password123",database="student")
	cur = con.cursor()
	a="Select * from student where StdID=%s OR Firstname=%s OR Surname=%s or DOB=%s or Age=%s or Gender=%s or Address=%s or Mobile=%s;"
	b=(StdID,Firstname,Surname,DOB,Age,Gender,Address,Mobile)
	cur.execute(a,b)
	row=cur.fetchall()
	con.commit()
	con.close()
	return row

def dataupdate(StdID,Firstname,Surname,DOB,Age,Gender,Address,Mobile):
	con = mysql.connector.connect(host="localhost",user="rc",passwd="password123",database="student")
	cur = con.cursor()
	a="update student set StdID= %s, Firstname=%s, Surname=%s, DOB=%s, Age=%s, Gender=%s, Address=%s, Mobile=%s;"
	b=(StdID,Firstname,Surname,DOB,Age,Gender,Address,Mobile)
	cur.execute(a,b)
	con.commit()
	con.close()
  
#studentdata()