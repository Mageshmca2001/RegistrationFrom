from tkinter import *
root=Tk()
root.title("Registration")
root.geometry("800x670")
root.resizable(True,True)

def register():
  name_info=namevalue.get()
  Department_info=Phonevalue.get()
  Degree_info=Degreevalue.get()
  Phone_info=Phonevalue.get()
  EmailID_info=EmailIDvalue.get()
  Gender_info=Gendervalue.get()
  Age_info=Agevalue.get()

  file=open(name_info + ".txt","w")
  file.write(name_info+"\n")
  file.write(Department_info+"\n")
  file.write(Degree_info+"\n")
  file.write(Phone_info+"\n")
  file.write(EmailID_info+"\n")
  file.write(Gender_info+"\n")
  file.write(Age_info+"\n")
  file.close()


  nameEntry.delete(0,END)
  DepartmentEntry.delete(0,END)
  DegreeEntry.delete(0,END)
  PhoneEntry.delete(0,END)
  EmailIDEntry.delete(0,END)
  GenderEntry.delete(0,END)
  AgeEntry.delete(0,END)
  



  Label(text="Registration success",fg="green",font=("calibri",11)).place(x=290,y=530)
  print("registered")

Label(root,text="Registration Form ",font="arial 25").pack(pady=50)

Label(text="Name",font=23).place(x=100,y=150)
Label(text="Department",font=23).place(x=100,y=200)
Label(text="Degree",font=23).place(x=100,y=250)
Label(text="phone",font=23).place(x=100,y=300)
Label(text="EmailID",font=23).place(x=100,y=350)
Label(text="Gender",font=23).place(x=100,y=400)
Label(text="Age",font=23).place(x=100,y=450)

#entry
namevalue=StringVar()
Departmentvalue=StringVar()
Degreevalue=StringVar()
Phonevalue=StringVar()
EmailIDvalue=StringVar()
Gendervalue=StringVar()
Agevalue=StringVar()

nameEntry=Entry(root,textvariable=namevalue,width=30,bd=2,font=20)
DepartmentEntry=Entry(root,textvariable=Departmentvalue,width=30,bd=2,font=20)
DegreeEntry=Entry(root,textvariable=Degreevalue,width=20,bd=2,font=20)
PhoneEntry=Entry(root,textvariable=Phonevalue,width=40,bd=2,font=20)
EmailIDEntry=Entry(root,textvariable=EmailIDvalue,width=30,bd=2,font=20)
GenderEntry=Entry(root,textvariable=Gendervalue,width=30,bd=2,font=20)
AgeEntry=Entry(root,textvariable=Agevalue,width=30,bd=2,font=20)


nameEntry.place(x=200,y=150)
DepartmentEntry.place(x=200,y=200)
DegreeEntry.place(x=200,y=250)
PhoneEntry.place(x=200,y=300)
EmailIDEntry.place(x=200,y=350)
GenderEntry.place(x=200,y=400)
AgeEntry.place(x=200,y=450)

#check button
checkvalue=IntVar
checkbtn=Checkbutton(text="remember kamal?",variable=checkvalue)
checkbtn.place(x=200,y=500)


Button(text="Register",font=20,width=11,height=2,command=register).place(x=300,y=530)




root.mainloop()
