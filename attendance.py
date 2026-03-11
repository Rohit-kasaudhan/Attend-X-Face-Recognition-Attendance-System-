from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #=================variables==============
        self.var_atten_studentID=StringVar()
        self.var_atten_Roll_no=StringVar()
        self.var_atten_student_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance_status=StringVar()



         # Image
        img = Image.open("images\paplu.png")
        img = img.resize((640, 200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=640, height=200)

        #img2
        img1 = Image.open("images\\ttl.jpg")
        img1 = img1.resize((640, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=640, y=0, width=640, height=200)

        # bg image
        img3 = Image.open("images\kiit.jpeg")
        img3 = img3.resize((1530, 640), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=640)


                # middle title part
        title_lbl=Label(
             bg_img,
            text="\tATTENDANCE MANAGEMENT SYSTEM\t",
            font=("times new roman",35,"bold",),
            bg="white",
            fg="green",
            anchor="w")
    
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=40,width=1500,height=550)


                #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",fg="red",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=4,width=600,height=390)

        img4 = Image.open("images\\atten.jpg")
        img4 = img4.resize((590, 100), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl = Label(Left_frame, image=self.photoimg4)
        f_lbl.place(x=5, y=0, width=590, height=100)
        #leftinside frame (frame k andar wala frame)
        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=110,width=586,height=260)

        #student id
        studentID_label=Label(left_inside_frame,text="Student ID",font=("times new roman",10,"bold"))
        studentID_label.grid(row=0,column=0,padx=10,pady=7,sticky=W)

        studentID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_studentID,font=("times new roman",10,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=7,sticky=W)


        #student name
        student_name_label=Label(left_inside_frame,text="Name",font=("times new roman",10,"bold"))
        student_name_label.grid(row=1,column=0,padx=10,pady=14,sticky=W)

        student_name_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_student_name,font=("times new roman",10,"bold"))
        student_name_entry.grid(row=1,column=1,padx=10,pady=14,sticky=W)

        #Roll NO:
        Roll_no_label=Label(left_inside_frame,text="Roll No:",font=("times new roman",10,"bold"))
        Roll_no_label.grid(row=0,column=2,padx=30,pady=7,sticky=W)

        Roll_no_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_Roll_no,font=("times new roman",10,"bold"))
        Roll_no_entry.grid(row=0,column=3,padx=1,pady=7,sticky=W)
        #department
        dep_label=Label(left_inside_frame,text="Department",font=("times new roman",10,"bold"))
        dep_label.grid(row=1,column=2,padx=30,pady=14,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",10,"bold"))
        dep_entry.grid(row=1,column=3,padx=1,pady=14,sticky=W)

        #time
        time_label=Label(left_inside_frame,text="Time",font=("times new roman",10,"bold"))
        time_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",10,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #date
        date_label=Label(left_inside_frame,text="Date",font=("times new roman",10,"bold"))
        date_label.grid(row=2,column=2,padx=30,pady=10,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",10,"bold"))
        date_entry.grid(row=2,column=3,padx=1,pady=10,sticky=W)

        #attendance status
        attendance_status_label = Label(left_inside_frame,text="Attendance Status",font=("times new roman",10,"bold") )
        attendance_status_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)

        attendance_status_combo = ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance_status,font=("times new roman",10,"bold"),state="readonly", width=17 )
        attendance_status_combo["values"] = ("Status", "Present", "Absent")
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=3, column=1, padx=10, pady=10,sticky=W)



        #bbuttonframe
        btn_frame=Frame(left_inside_frame)
        btn_frame.place(x=5,y=190,width=600,height=27)

        import_csv_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width="20",font=("times new roman",10,"bold"),bg="blue",fg="white")
        import_csv_btn.grid(row=0,column=0)

        export_csv_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width="18",font=("times new roman",10,"bold"),bg="blue",fg="white")
        export_csv_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width="18",command=self.update_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width="20",command=self.reset_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #right label frame
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",fg="red",font=("times new roman",12,"bold"))
        RIGHT_frame.place(x=620,y=4,width=640,height=390)

        #table frame
        table_frame=Frame(RIGHT_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=10,width=610,height=350)

        #==========Scroll bar table===============
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=(
            "studentID","Roll_no","student_name","dep","time","date","attendance_status"
        )
            ,xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("studentID",text="Student ID")
        self.AttendanceReportTable.heading("Roll_no",text="Roll No:")
        self.AttendanceReportTable.heading("student_name",text="Name")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance_status",text="Attendance Status")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("studentID",width=100)
        self.AttendanceReportTable.column("Roll_no",width=100)
        self.AttendanceReportTable.column("student_name",width=120)
        self.AttendanceReportTable.column("dep",width=120)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance_status",width=120)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #==============fetch data===================

    def fetchData(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                self.AttendanceReportTable.insert("",END,values=i)

    # import csv
    def importCsv(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            if not fln:
                return
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)

    # export csv
    def exportCsv(self):
       try:
           if len(mydata)<1:
              messagebox.showerror("No Data","No Data found to export",parent=self.root)
              return False
           fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
           if not fln:
               return
           with open(fln,mode="w",newline="")as myfile:
             exp_write=csv.writer(myfile,delimiter=",")
             for i in mydata:
                exp_write.writerow(i)
             messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
       except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content['values']
         self.var_atten_studentID.set(rows[0])
         self.var_atten_Roll_no.set(rows[1])
         self.var_atten_student_name.set(rows[2])
         self.var_atten_dep.set(rows[3])
         self.var_atten_time.set(rows[4])
         self.var_atten_date.set(rows[5])
         self.var_atten_attendance_status.set(rows[6])

    def reset_data(self):
         self.var_atten_studentID.set("")
         self.var_atten_Roll_no.set("")
         self.var_atten_student_name.set("")
         self.var_atten_dep.set("")
         self.var_atten_time.set("")
         self.var_atten_date.set("")
         self.var_atten_attendance_status.set("")

        #=========update function===========
    def update_data(self):
        if self.var_atten_dep.get() == "" or self.var_atten_student_name.get() == "" or self.var_atten_studentID.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return

        try:
            Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
            if not Update:
                return

            target_id = str(self.var_atten_studentID.get())
            target_date = str(self.var_atten_date.get())

            updated = False
            for i, row in enumerate(mydata):
            # Match by studentID (col 0) AND date (col 5) to update the right entry
                if len(row) >= 7 and str(row[0]) == target_id and str(row[5]) == target_date:
                    mydata[i] = [
                        self.var_atten_studentID.get(),
                        self.var_atten_Roll_no.get(),
                        self.var_atten_student_name.get(),
                        self.var_atten_dep.get(),
                        self.var_atten_time.get(),
                        self.var_atten_date.get(),
                        self.var_atten_attendance_status.get()
                    ]
                    updated = True
                    break

            if not updated:
               messagebox.showerror("Error", "Record not found in loaded data. Please re-import CSV.", parent=self.root)
               return

        # Write the updated mydata back to the CSV file
            import csv
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save Updated CSV",
                defaultextension=".csv",
                filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                parent=self.root
            )
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    exp_write = csv.writer(myfile)
                    for row in mydata:
                        exp_write.writerow(row)
                messagebox.showinfo("Success", "Attendance updated and saved successfully!", parent=self.root)

        # Refresh the treeview
            self.fetchData(mydata)

        except Exception as es:
          messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
         

















if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
