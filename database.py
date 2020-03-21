#Frontend of the App
#try
from Tkinter import *
import tkMessageBox
import  database_backend 

#import Student database

class Student:

	def __init__(self,root):
		self.root=root 
		self.root.title("Student Database Management system")
		self.root.geometry("1000x700")
		self.root.config(bg="Light Blue")

		StdID=StringVar()
		firstname=StringVar()
		surname=StringVar()
		dob=StringVar()
		age=StringVar()
		gender=StringVar()
		address=StringVar()
		mobile=StringVar()

		####################Functions#########################

		def iExit():
			iExit=tkMessageBox.askyesno("students databas Management systems","confirm if you want to exit")
			if iExit > 0:
				root.destroy()
			return 

		def cleardata():
			self.txtStdID.delete(0,END)
			self.txtFna.delete(0,END)
			self.txtSna.delete(0,END)
			self.txtDOB.delete(0,END)
			self.txtAge.delete(0,END)
			self.txtGender.delete(0,END)
			self.txtAdress.delete(0,END)
			self.txtMobile.delete(0,END)

		def adddata():
			if (len(StdID.get())!=0):
				database_backend.addstudentrecord(StdID.get(),firstname.get(),surname.get(),dob.get(),age.get(),gender.get(),address.get(),mobile.get())
				studentlist.delete(0,END)
				studentlist.insert(END,StdID.get(),firstname.get(),surname.get(),dob.get(),age.get(),gender.get(),address.get(),mobile.get())
			tkMessageBox.showinfo("Operation", "Entry Added")

		def displaydata():
			studentlist.delete(0,END)
			for row in database_backend.viewdata():
				studentlist.insert(END,row,str(""))

		def studentrec(event):
			global sd
			searchstduent=studentlist.curselection()[0]
			sd=studentlist.get(searchstduent)
			#clearing and then pasting
			self.txtStdID.delete(0,END)
			self.txtStdID.insert(END,sd[1])
			self.txtFna.delete(0,END)
			self.txtFna.insert(END,sd[2])
			self.txtSna.delete(0,END)
			self.txtSna.insert(END,sd[3])
			self.txtDOB.delete(0,END)
			self.txtDOB.insert(END,sd[4])
			self.txtAge.delete(0,END)
			self.txtAge.insert(END,sd[5])
			self.txtGender.delete(0,END)
			self.txtGender.insert(END,sd[6])
			self.txtAdress.delete(0,END)
			self.txtAdress.insert(END,sd[7])
			self.txtMobile.delete(0,END)
			self.txtMobile.insert(END,sd[8])
			
		def deletedata():
			if (len(StdID.get())!=0):
				database_backend.deletedata(StdID.get())
				cleardata()
				displaydata()
			tkMessageBox.showinfo("Operation", "Entry deleted")

		def searchdata():
			studentlist.delete(0,END)
			for row in database_backend.searchdata(StdID.get(),firstname.get(),surname.get(),dob.get(),age.get(),gender.get(),address.get(),mobile.get()):
					studentlist.insert(END,row,str(""))

		def updatedata():
			if (len(StdID.get())!=0):
				database_backend.deletedata(StdID.get())
				database_backend.addstudentrecord(StdID.get(),firstname.get(),surname.get(),dob.get(),age.get(),gender.get(),address.get(),mobile.get())
			tkMessageBox.showinfo("Operation", "Entry Updated")	

		############Frame###################
		MainFrame=Frame(self.root, bg="Light Blue")
		MainFrame.grid()	


		#Creating Title frame inside the Main frame
		Titleframe=Frame(MainFrame,bd=2,padx=54,pady=8,bg="Ghost White",relief=RAISED)
		Titleframe.pack(side=TOP)

		self.lblTxt=Label(Titleframe,font=("Roboto",30,"bold"),text="Student Database Management System",bg="Ghost White")
		self.lblTxt.grid()

		Buttonframe=LabelFrame(MainFrame,bd=1,width=1350,height=70,padx=18,pady=10,bg="Ghost White",relief=RIDGE)
		Buttonframe.pack(side=BOTTOM)

		DataframeLEFT=LabelFrame(MainFrame,font=("Roboto",15,"bold"),text="Student Info",bd=1,width=1000,height=600,padx=15,pady=10,bg="Ghost White",relief=RIDGE)
		DataframeLEFT.pack(side=LEFT)

		DataframeRIGHT=LabelFrame(MainFrame,font=("Roboto",15,"bold"),text="Student Details",bd=1,width=450,height=300,padx=31,pady=3,bg="Ghost White",relief=RIDGE)
		DataframeRIGHT.pack(side=RIGHT)

		##########Labels and Entry ##############
		self.lblStdID=Label(DataframeLEFT,font=("Roboto",15),text="Student ID",padx=2,pady=2,bg="Ghost White")
		self.lblStdID.grid(row=0,column=0,sticky=W)
		self.txtStdID=Entry(DataframeLEFT,font=("Roboto",15),textvariable=StdID,width=39)
		self.txtStdID.grid(row=0,column=1)

		self.lblFna=Label(DataframeLEFT,font=("Roboto",15),text="First Name",padx=2,pady=2,bg="Ghost White")
		self.lblFna.grid(row=1,column=0,sticky=W)
		self.txtFna=Entry(DataframeLEFT,font=("Roboto",15),textvariable=firstname,width=39)
		self.txtFna.grid(row=1,column=1)

		self.lblSna=Label(DataframeLEFT,font=("Roboto",15,),text="Surname",padx=2,pady=2,bg="Ghost White")
		self.lblSna.grid(row=2,column=0,sticky=W)
		self.txtSna=Entry(DataframeLEFT,font=("Roboto",15),textvariable=surname,width=39)
		self.txtSna.grid(row=2,column=1)

		self.lblDOB=Label(DataframeLEFT,font=("Roboto",15),text="DOB",padx=2,pady=2,bg="Ghost White")
		self.lblDOB.grid(row=3,column=0,sticky=W)
		self.txtDOB=Entry(DataframeLEFT,font=("Roboto",15),textvariable=dob,width=39)
		self.txtDOB.grid(row=3,column=1)

		self.lblGender=Label(DataframeLEFT,font=("Roboto",15),text="Gender",padx=2,pady=2,bg="Ghost White")
		self.lblGender.grid(row=4,column=0,sticky=W)
		self.txtGender=Entry(DataframeLEFT,font=("Roboto",15),textvariable=gender,width=39)
		self.txtGender.grid(row=4,column=1)

		self.lblAge=Label(DataframeLEFT,font=("Roboto",15),text="Age",padx=2,pady=2,bg="Ghost White")
		self.lblAge.grid(row=5,column=0,sticky=W)
		self.txtAge=Entry(DataframeLEFT,font=("Roboto",15),textvariable=age,width=39)
		self.txtAge.grid(row=5,column=1)

		self.lblAdress=Label(DataframeLEFT,font=("Roboto",15),text="Address",padx=2,pady=2,bg="Ghost White")
		self.lblAdress.grid(row=6,column=0,sticky=W)
		self.txtAdress=Entry(DataframeLEFT,font=("Roboto",15),textvariable=address,width=39)
		self.txtAdress.grid(row=6,column=1)

		self.lblMobile=Label(DataframeLEFT,font=("Roboto",15,),text="Mobile",padx=2,pady=2,bg="Ghost White")
		self.lblMobile.grid(row=7,column=0,sticky=W)
		self.txtMobile=Entry(DataframeLEFT,font=("Roboto",15,),textvariable=mobile,width=39)
		self.txtMobile.grid(row=7,column=1)


		################## List Box and Scroll Bar  ######################

		scrollbar=Scrollbar(DataframeRIGHT)
		scrollbar.grid(row=0,column=1,sticky='ns')

		studentlist=Listbox(DataframeRIGHT,width=41,height=16,font=('Roboto',12), yscrollcommand=scrollbar.set)
		studentlist.bind('<<ListboxSelect>>',studentrec)
		studentlist.grid(row=0,column=0,padx=8)
		scrollbar.config(command= studentlist.yview)

		################### Buttons #########################

		self.btnadddate=Button(Buttonframe,text="add new",font=("Roboto",15,'bold'),height=1,width=10,bd=4,command=adddata)
		self.btnadddate.grid(row=0,column=0)

		self.btndisplaydata=Button(Buttonframe,text="Display",font=("Roboto",15,'bold'),height=1,width=10,bd=4,command=displaydata)
		self.btndisplaydata.grid(row=0,column=1)

		self.btncleardata=Button(Buttonframe,text="Clear",font=("Roboto",15,'bold'),height=1,width=10,bd=4,command=cleardata)
		self.btncleardata.grid(row=0,column=2)

		self.btndeletedata=Button(Buttonframe,text="Delete",font=("Roboto",15,'bold'),height=1,width=10,bd=4,command=deletedata)
		self.btndeletedata.grid(row=0,column=3)

		self.btnsearchdata=Button(Buttonframe,text="Search",font=("Roboto",15,'bold'),height=1,width=10,bd=4,command=searchdata)
		self.btnsearchdata.grid(row=0,column=4)

		self.btnupdatedata=Button(Buttonframe,text="Update",font=("Roboto",15,'bold'),height=1,width=10,bd=4,command=updatedata)
		self.btnupdatedata.grid(row=0,column=5)

		self.btnexit=Button(Buttonframe,text="Exit",font=("Roboto",15,'bold'),height=1,width=10,bd=4,command=iExit)
		self.btnexit.grid(row=0,column=6)

		



if __name__=='__main__':
	root=Tk()
	application=Student(root)
	root.mainloop()
