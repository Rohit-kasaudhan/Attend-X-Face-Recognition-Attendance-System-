from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import cv2
import os
from face_recognition import Face_recognition
from train import Train
from attendance import Attendance
from devlopers import App
import tkinter
from about import About


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        # Image
        img = Image.open("images\ict.jpg")
        img = img.resize((425, 150), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=420, height=150)

        # Image1
        img1 = Image.open("images\download.jpg")
        img1 = img1.resize((420, 150), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=425, y=0, width=420, height=150)


        # Image2
        img2 = Image.open("images\ict.jpg")
        img2 = img2.resize((430, 150), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=855, y=0, width=430, height=150)


        # bg image
        img3 = Image.open("images\kiit.jpeg")
        img3 = img3.resize((1530, 640), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=150, width=1530, height=640)


        # middle title part
        title_lbl=Label(
            bg_img,
            text="FACE  RECOGNITION  ATTENDANCE  SYSTEM\t\t",
            font=("times new roman",35,"bold",),
            bg="white",
            fg="red",
            anchor="center")
    
        title_lbl.place(x=0,y=0,width=1530,height=45)


        # student button
        img4 = Image.open("images\std.jpg")
        img4 = img4.resize((150,120), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=150,height=120)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="lightgreen",fg="white")
        b1_1.place(x=200,y=200,width=150,height=30)




        # detect face button
        img5 = Image.open("images\\reco.jpg")
        img5 = img5.resize((150,120), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=420,y=100,width=150,height=120)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="lightgreen",fg="white")
        b1_1.place(x=420,y=200,width=150,height=30)




        # attendance button
        img6 = Image.open("images\\att.jpg")
        img6 = img6.resize((150,120), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=640,y=100,width=150,height=120)

        b1_1=Button(bg_img,text="Attendance Details",cursor="hand2",command=self.attendance_data,font=("times new roman",12,"bold"),bg="lightgreen",fg="white")
        b1_1.place(x=640,y=200,width=150,height=30)



        # About  button
        img7= Image.open("images\help.png")
        img7 = img7.resize((150,120), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.about_data)
        b1.place(x=860,y=100,width=150,height=120)

        b1_1=Button(bg_img,text="About",cursor="hand2",command=self.about_data,font=("times new roman",16,"bold"),bg="lightgreen",fg="white")
        b1_1.place(x=860,y=200,width=150,height=30)




         # train data
        img8= Image.open("images\\train.jpg")
        img8 = img8.resize((150,120), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=280,width=150,height=120)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",16,"bold"),bg="lightgreen",fg="white")
        b1_1.place(x=200,y=380,width=150,height=30)




         # photo
        img9= Image.open("images\photo.png")
        img9 = img9.resize((150,120), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=420,y=280,width=150,height=120)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",16,"bold"),bg="lightgreen",fg="white")
        b1_1.place(x=420,y=380,width=150,height=30)



        # developers
        img10= Image.open("images\dev.png")
        img10 = img10.resize((150,120), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developers_data)
        b1.place(x=640,y=280,width=150,height=120)

        b1_1=Button(bg_img,text="Developers",cursor="hand2",command=self.developers_data,font=("times new roman",16,"bold"),bg="lightgreen",fg="white")
        b1_1.place(x=640,y=380,width=150,height=30)



        #exit
        img11= Image.open("images\exit.jpg")
        img11 = img11.resize((150,120), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iexit)
        b1.place(x=860,y=280,width=150,height=120)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iexit,font=("times new roman",16,"bold"),bg="lightgreen",fg="white")
        b1_1.place(x=860,y=380,width=150,height=30)
    
    def open_img(self):
        os.startfile("data")

    #================Functions Button====================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)


    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developers_data(self):
        self.new_window = Toplevel(self.root)
        self.app = App(self.new_window)  



    def about_data(self):
        self.new_window = Toplevel(self.root)
        self.app = About(self.new_window)    

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit?",parent=self.root)
        if self.iexit >0:
            self.root.destroy()
        else:
            return



    




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
