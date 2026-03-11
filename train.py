from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        
        title_lbl=Label(
            self.root,
            text="TRAIN DATA SET\t",
            font=("times new roman",35,"bold",),
            bg="white",
            fg="red",
            anchor="center")
    
        title_lbl.place(x=0,y=0,width=1530,height=45)

        img_top = Image.open("images\\abbbb.jpeg")
        img_top = img_top.resize((1300,650), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=50, width=1300, height=650)


        #button
        
     #   b1_1=Button(self.root,text="TRAIN DATA",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
      #  b1_1.place(x=430,y=300,width=450,height=60)



                # ================= Center Button =================
        b1_1 = Button(
            self.root,
            text="TRAIN DATA",
            command=self.train_classifier,
            font=("times new roman", 22, "bold"),
            bg="#0f3057",
            fg="#00f5ff",
            activebackground="#145da0",
            activeforeground="white",
            cursor="hand2",
            bd=4,                  # Visible border
            relief="raised",       # 3D effect
            highlightthickness=2,
            highlightbackground="#00f5ff"
        )

        b1_1.place(relx=0.5, rely=0.5, anchor=CENTER)

        # ================= Hover Effects =================
        def on_enter(e):
            b1_1['background'] = "#145da0"
            b1_1['fg'] = "white"
            b1_1['relief'] = "solid"

        def on_leave(e):
            b1_1['background'] = "#0f3057"
            b1_1['fg'] = "#00f5ff"
            b1_1['relief'] = "raised"

        b1_1.bind("<Enter>", on_enter)
        b1_1.bind("<Leave>", on_leave)



    def train_classifier(self):
            
            data_dir=("data")
            path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

            faces=[]
            ids=[]

            for image in path:
                
                img=Image.open(image).convert('L')   #Gray scale image
                imageNp=np.array(img,'uint8')
                id=int(os.path.split(image)[1].split('.')[1])
  
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)==13
            ids=np.array(ids)

            #================ Train the classifier And save================
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training datasets completed!!")
                
                








if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()