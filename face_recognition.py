from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
from generate_attendance_excel import generate_excel



class Face_recognition:
    def __init__(self, root):
        self.last_marked = {}  # {studentID: datetime}
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="FACE RECOGNITION\t",font=("times new roman",35,"bold",), bg="white",fg="red",anchor="center")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open("images\po.jpg")
        img_top = img_top.resize((1300,650), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1300, height=650)


         



                # ================= Center Button =================
        b1_1 = Button(
            self.root,
            text="FACE DETECTOR",
            command=self.face_recog,
            font=("times new roman", 22, "bold"),
            bg="#0f3057",
            fg="#00f5ff",
            activebackground="#0967da",
            activeforeground="white",
            cursor="hand2",
            bd=4,                  # Visible border
            relief="raised",       # 3D effect
            highlightthickness=2,
            highlightbackground="#00bdec"
        )

        b1_1.place(relx=0.6, rely=0.5, anchor="w")

        # ================= Hover Effects =================
        def on_enter(e):
            b1_1['background'] = "#1455a0"
            b1_1['fg'] = "white"
            b1_1['relief'] = "solid"

        def on_leave(e):
            b1_1['background'] = "#0f3057"
            b1_1['fg'] = "#00f5ff"
            b1_1['relief'] = "raised"

        b1_1.bind("<Enter>", on_enter)
        b1_1.bind("<Leave>", on_leave)


        #==========================MARK ATTENDANCE+=============================
    def mark_attendance(self, r, n, d, s):
       now = datetime.now()
       today = now.strftime("%d/%m/%Y")
       time_str = now.strftime("%H:%M:%S")

    # Check if this student was marked in the last 2 minutes
       if s in self.last_marked:
          seconds_passed = (now - self.last_marked[s]).total_seconds()
          if seconds_passed < 120:  # 120 seconds = 2 minutes
              return  # Too soon, skip silently

       with open("Attend.csv", "r+", newline="\n") as f:
          myDataList = f.readlines()

        # Build a set of (Roll_no, date) already recorded
          already_marked = set()
          for line in myDataList:
              entry = line.strip().split(",")
              if len(entry) >= 6:
                 already_marked.add((entry[0], entry[5]))  # (Roll_no, date)

        # Only write if not already marked today
          if (r, today) not in already_marked:
              f.writelines(f"\n{s},{r},{n},{d},{time_str},{today},Present")

    # Update the last marked time for this student (whether new or returning)
       self.last_marked[s] = now






    def face_recog(self):

       faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
       clf = cv2.face.LBPHFaceRecognizer_create()
       clf.read("classifier.xml")

    #  Connect to DB ONCE
       conn = mysql.connector.connect(
         host="localhost",
         user="root",
         password="Rohit@3809",
         database="face_recognizer"
       )
       my_cursor = conn.cursor()

       video_cap = cv2.VideoCapture(0)

       while True:
           ret, img = video_cap.read()
           if not ret:
              break

           gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
           features = faceCascade.detectMultiScale(gray_image, 1.1, 10)

           for (x, y, w, h) in features:

               id, predict = clf.predict(gray_image[y:y+h, x:x+w])
               confidence = int((100 * (1 - predict / 300)))

            #  Single Query
               my_cursor.execute(
                  "SELECT student_name, Roll_no, dep, studentID FROM student WHERE studentID=%s",
                (id,)
               )
               row = my_cursor.fetchone()

               if confidence > 77 and row is not None:
                   r, n, d, s = row


                   cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
                   cv2.putText(img, f"Name:{r}", (x,y-55),
                            cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),2)
                   cv2.putText(img, f"Roll no:{n}", (x,y-35),
                            cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),2)
                   cv2.putText(img, f"Department:{d}", (x,y-15),
                            cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),2)
                   cv2.putText(img, f"studentID:{s}", (x,y+5),
                            cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),2)
                   self.mark_attendance(r,n,d,s)
               else:
                   cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 3)
                   cv2.putText(img,"Unknown Face",(x,y-5),
                            cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

           cv2.imshow("Face Recognition", img)

           if cv2.waitKey(1) == 13:
             break

       video_cap.release()
       cv2.destroyAllWindows()
       conn.close()

       # ── Generate full attendance Excel (Present + Absent) ──────────────
       try:
           saved_path = generate_excel()
           messagebox.showinfo(
               "Attendance Report Generated",
               f"Attendance Excel saved successfully!\n\nFile: {saved_path}\n\n"
               "✔ Students detected by camera → Present\n"
               "✖ Remaining students from database → Absent",
               parent=self.root
           )
       except Exception as ex:
           messagebox.showerror(
               "Excel Error",
               f"Could not generate attendance Excel:\n{str(ex)}",
               parent=self.root
           )




if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()