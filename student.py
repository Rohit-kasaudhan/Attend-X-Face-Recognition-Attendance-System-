from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from export_students_excel import export_students





class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #===================variables===================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_studentID=StringVar()
        self.var_student_name=StringVar()
        self.var_section=StringVar()
        self.var_Roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_Phone_no=StringVar()
        self.var_address=StringVar()
        self.var_teacher_name=StringVar()



         # Image
        img = Image.open("images\\500805811_18354636976196964_2874614255997732042_n.jpg")
        img = img.resize((425, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=420, height=200)


        # Image1
        img1 = Image.open("images\\bg.jpeg")
        img1 = img1.resize((420, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=425, y=0, width=420, height=200)


        # Image2
        img2 = Image.open("images\\501301941_18354636910196964_6884374772658807174_n.jpg")
        img2 = img2.resize((430, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=855, y=0, width=430, height=200)



         # bg image
        img3 = Image.open("images\kiit.jpeg")
        img3 = img3.resize((1530, 640), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1530, height=640)


        # middle title part
        title_lbl=Label(
            bg_img,
            text="STUDENT MANAGEMENT SYSTEM\t",
            font=("times new roman",35,"bold",),
            bg="white",
            fg="red",
            anchor="center")
    
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=40,width=1500,height=550)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=440)

        img4 = Image.open("images\\atten.jpg")
        img4 = img4.resize((590, 100), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl = Label(Left_frame, image=self.photoimg4)
        f_lbl.place(x=5, y=0, width=590, height=100)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text=" Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=100,width=590,height=94)

        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=5,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=5,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course","BTech","Mtech","BE","CSIT")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5)


        #year
        year_label=Label(current_course_frame,text="   Year",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2024-25","2025-26","2026-27","2027-28")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5)



        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"))
        semester_label.grid(row=1,column=2,padx=5,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        semester_combo["values"]=("Select Semester","1st sem","2nd sem","3rd sem","4th sem","5th sem","6th sem","7th sem","8th sem" )
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=5)


        #current course
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text=" Class Student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=195,width=590,height=220)


        #student id
        studentID_label=Label(class_student_frame,text="Student ID",font=("times new roman",10,"bold"))
        studentID_label.grid(row=0,column=0,padx=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_studentID,width=20,font=("times new roman",10,"bold"))
        studentID_entry.grid(row=0,column=1,padx=5,sticky=W)


        #student name
        student_name_label=Label(class_student_frame,text="Student Name",font=("times new roman",10,"bold"))
        student_name_label.grid(row=0,column=2,padx=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_student_name,width=20,font=("times new roman",10,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,sticky=W)



        #section
        section_label=Label(class_student_frame,text="Section",font=("times new roman",10,"bold"))
        section_label.grid(row=1,column=0,padx=5,sticky=W)

        section_entry=ttk.Entry(class_student_frame,textvariable=self.var_section,width=20,font=("times new roman",10,"bold"))
        section_entry.grid(row=1,column=1,padx=5,sticky=W)


        #roll no
        Roll_no_label=Label(class_student_frame,text="Roll no:",font=("times new roman",10,"bold"))
        Roll_no_label.grid(row=1,column=2,padx=5,sticky=W)

        Roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_Roll_no,width=20,font=("times new roman",10,"bold"))
        Roll_no_entry.grid(row=1,column=3,padx=5,sticky=W)


        # Gender
        gender_label = Label(class_student_frame,text="Gender",font=("times new roman",10,"bold") )
        gender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman",10,"bold"),state="readonly", width=17 )
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)
       #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",10,"bold"))
       # gender_entry.grid(row=2,column=1,padx=5,sticky=W)


        #dob
        dob_label=Label(class_student_frame,text="Date Of Birth:",font=("times new roman",10,"bold"))
        dob_label.grid(row=2,column=2,padx=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",10,"bold"))
        dob_entry.grid(row=2,column=3,padx=5,sticky=W)


        #email
        email_label=Label(class_student_frame,text="Email",font=("times new roman",10,"bold"))
        email_label.grid(row=3,column=0,padx=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",10,"bold"))
        email_entry.grid(row=3,column=1,padx=5,sticky=W)


        #phoneno.
        Phone_no_label=Label(class_student_frame,text="Phone no:",font=("times new roman",10,"bold"))
        Phone_no_label.grid(row=3,column=2,padx=5,sticky=W)

        Phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_Phone_no,width=20,font=("times new roman",10,"bold"))
        Phone_no_entry.grid(row=3,column=3,padx=5,sticky=W)


        #address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",10,"bold"))
        address_label.grid(row=4,column=0,padx=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",10,"bold"))
        address_entry.grid(row=4,column=1,padx=5,sticky=W)


        #Teacher name
        teacher_name_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",10,"bold"))
        teacher_name_label.grid(row=4,column=2,padx=5,sticky=W)

        teacher_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher_name,width=20,font=("times new roman",10,"bold"))
        teacher_name_entry.grid(row=4,column=3,padx=5,sticky=W)


        # radio buttons
        self.var_radio1 = StringVar()

        radiobtn1 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="Take Photo Sample",
            value="Yes"
        )
        radiobtn1.grid(row=6, column=0, padx=10, pady=5)

        radiobtn2 = ttk.Radiobutton(
            class_student_frame,
            variable=self.var_radio1,
            text="Photo Sample Not Available",
            value="No"
        )
        radiobtn2.grid(row=6, column=1, padx=10, pady=5)


        #bbuttonframe
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="#967D69")
        btn_frame.place(x=5,y=150,width=580,height=45)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width="10",font=("times new roman",10,"bold"),bg="#FF7F50",fg="black")
        save_btn.grid(row=0,column=0)

        up_btn=Button(btn_frame,text="Update",command=self.update_data,width="10",font=("times new roman",11,"bold"),bg="#FCEFEF",fg="black")
        up_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width="10",font=("times new roman",11,"bold"),bg="#7FD8BE",fg="black")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width="10",font=("times new roman",11,"bold"),bg="#0B6285",fg="black")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Pic",width="10",font=("times new roman",11,"bold"),bg="#8f8b61",fg="black")
        take_photo_btn.grid(row=0,column=4)

        update_photo_btn=Button(btn_frame,text="Update Pic",width="10",font=("times new roman",10,"bold"),bg="#faedcd",fg="black")
        update_photo_btn.grid(row=0,column=5)





        #right label frame
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        RIGHT_frame.place(x=620,y=10,width=620,height=440)


        img5 = Image.open("images\\ttl.jpg")
        img5 = img5.resize((610, 100), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        f_lbl = Label(self.root, image=self.photoimg5)
        f_lbl.place(x=630, y=225, width=610, height=100)


        #search system
        search_frame=LabelFrame(RIGHT_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=100,width=610,height=60)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",10,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10, pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=17)
        search_combo["values"]=("Select","Roll_no","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width="10",font=("times new roamn",10,"bold"),bg="#faedcd",fg="black")
        search_btn.grid(row=0,column=3)

        showAll_btn=Button(search_frame,text="Show All",width="10",font=("times new roamn",10,"bold"),bg="#faedcd",fg="black")
        showAll_btn.grid(row=0,column=4)

        #table frame
        table_frame=Frame(RIGHT_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=160,width=610,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=(
            "dep","course","year","semester","studentID","student_name",
            "section","Roll_no","gender","dob","email","Phone_no","address",
            "teacher_name","take_photo")
            ,xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("studentID",text="Student ID")
        self.student_table.heading("student_name",text="Student Name")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("Roll_no",text="Roll no:")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date Of Birth:")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("Phone_no",text="Phone no:")
        self.student_table.heading("address",text="Address:")
        self.student_table.heading("teacher_name",text="Teacher Name:")
        self.student_table.heading("take_photo",text="Take Pic")

        
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=80)
        self.student_table.column("course",width=80)
        self.student_table.column("year",width=80)
        self.student_table.column("semester",width=80)
        self.student_table.column("studentID",width=80)
        self.student_table.column("student_name",width=80)
        self.student_table.column("section",width=80)
        self.student_table.column("Roll_no",width=80)
        self.student_table.column("gender",width=80)
        self.student_table.column("dob",width=80)
        self.student_table.column("email",width=150)
        self.student_table.column("Phone_no",width=120)
        self.student_table.column("address",width=180)
        self.student_table.column("teacher_name",width=150)
        self.student_table.column("take_photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    

    #=====================Function declaration===================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.var_studentID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",user="root",password="Rohit@3809",database="face_recognizer")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_studentID.get(),
                                                                                                            self.var_student_name.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_Roll_no.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_Phone_no.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher_name.get(),
                                                                                                            self.var_radio1.get()
                                                                                                             
                                                                                                             
                                                                                                              ))
               
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
               try:
                   export_students()
               except Exception:
                   pass
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    
    
    
    #===========fetch data===================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Rohit@3809",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select* from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    

    #===================get cursor================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_studentID.set(data[4]),
        self.var_student_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_Roll_no.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_Phone_no.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher_name.set(data[13]),
        self.var_radio1.set(data[14])


    #=========update function===========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.var_studentID.get()=="":
           messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Rohit@3809",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET dep=%s,course=%s,year=%s,semester=%s,student_name=%s,section=%s,Roll_no=%s,gender=%s,dob=%s,email=%s,Phone_no=%s,address=%s,teacher_name=%s,take_photo=%s WHERE studentID=%s" ,(
                                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                                self.var_student_name.get(),
                                                                                                                                                                                                                                self.var_section.get(),
                                                                                                                                                                                                                                self.var_Roll_no.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_Phone_no.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_teacher_name.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                self.var_studentID.get() 
                                                                                                                                                                                                                          ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
                try:
                    export_students()
                except Exception:
                    pass
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                    

    #=============delete function==============
    def delete_data(self):
        if self.var_studentID.get()=="":
            messagebox.showerror("Error","Student id is required! ",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Rohit@3809",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where studentID=%s"
                    val=(self.var_studentID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details!",parent=self.root)
                try:
                    export_students()
                except Exception:
                    pass
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #==========reset====================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_studentID.set("")
        self.var_student_name.set("")
        self.var_section.set("Select section")
        self.var_Roll_no.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_Phone_no.set("")
        self.var_address.set("")
        self.var_teacher_name.set("")
        self.var_radio1.set("")



        #=========genertae data set or take photo smaple============
    def generate_dataset(self):
                    if self.var_dep.get()=="Select Department" or self.var_student_name.get()=="" or self.var_studentID.get()=="":
                        messagebox.showerror("Error","All Fields are required",parent=self.root)
                    else:
                        try:
                            conn=mysql.connector.connect(host="localhost",user="root",password="Rohit@3809",database="face_recognizer")
                            my_cursor=conn.cursor()
                            my_cursor.execute("select * from student")
                            myresult=my_cursor.fetchall()
                            id=0
                            for x in myresult:
                                id=id+1
                            my_cursor.execute("UPDATE student SET dep=%s,course=%s,year=%s,semester=%s,student_name=%s,section=%s,Roll_no=%s,gender=%s,dob=%s,email=%s,Phone_no=%s,address=%s,teacher_name=%s,take_photo=%s WHERE studentID=%s",(
                                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                                     self.var_course.get(),
                                                                                                                                                                                                                                                     self.var_year.get(),
                                                                                                                                                                                                                                                     self.var_semester.get(),
                                                                                                                                                                                                                                                     self.var_student_name.get(),
                                                                                                                                                                                                                                                     self.var_section.get(),
                                                                                                                                                                                                                                                     self.var_Roll_no.get(),
                                                                                                                                                                                                                                                     self.var_gender.get(),
                                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                                    self.var_Phone_no.get(),
                                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                                    self.var_teacher_name.get(),
                                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                                    self.var_studentID.get()==id+1 

                            ))
                            conn.commit()
                            self.fetch_data()
                            self.reset_data()
                            conn.close()


                            #=================== LOad predefined data on face frontals from opencv=========
                            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                            def face_cropped(img):
                                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                faces=face_classifier.detectMultiScale(gray,1.3,5)
                                #scaling factor=1.3
                                #Minimum Neighbour=5


                                for(x,y,w,h) in faces:
                                    face_cropped=img[y:y+h,x:x+w]
                                    return face_cropped
                                
                            cap=cv2.VideoCapture(0)
                            img_id=0
                            while True:
                                ret,my_frame=cap.read()
                                if face_cropped(my_frame) is not None:
                                    img_id+=1
                                    face=cv2.resize(face_cropped(my_frame),(450,450))
                                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                    file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg "
                                    cv2.imwrite(file_name_path,face)
                                    cv2.putText(face,str(img_id),(50,50 ),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                    cv2.imshow("Cropped Face",face)

                                if cv2.waitKey(1)==13 or int(img_id)==100:
                                    break
                            cap.release()
                            cv2.destroyAllWindows()
                            messagebox.showinfo("Result","Generating data set completed!! ")
                        except Exception as es:
                            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                        



                
                             



        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
