# 🎓Attend-X ( Face Recognition Attendance System )

A desktop-based **automated attendance management system** built with Python, OpenCV, and Tkinter. It uses **LBPH (Local Binary Pattern Histogram)** face recognition to identify students in real time via webcam and automatically marks their attendance — exporting the results to both CSV and Excel.

---

## 📸 Features

- 🔐 **Secure Login & Registration** — User authentication backed by MySQL
- 👨‍🎓 **Student Management** — Add, update, delete student records with photo capture
- 🤖 **Face Detection & Training** — Capture face samples and train the LBPH classifier
- 📷 **Real-Time Face Recognition** — Webcam-based recognition with confidence threshold
- ✅ **Automatic Attendance Marking** — Marks Present/Absent with duplicate-prevention logic (2-minute cooldown)
- 📊 **Attendance Reports** — Auto-generates a styled Excel report after every session
- 📁 **CSV Import/Export** — View, update, and export attendance data
- 📋 **Student Excel Export** — Full student master list exported to `.xlsx`
- 👨‍💻 **Developers & About Pages** — Project info and team credits

---

## 🗂️ Project Structure

```
Face-Recognition-Attendance-System/
│
├── run.py                        # Entry point — launches the login window
├── login.py                      # Login & registration UI
├── main.py                       # Main dashboard with navigation buttons
├── student.py                    # Student registration, CRUD, face capture
├── train.py                      # Train the LBPH face recognizer
├── face_recognition.py           # Real-time face recognition & attendance marking
├── attendance.py                 # View, import, export, update attendance CSV
├── generate_attendance_excel.py  # Generate styled attendance Excel report
├── export_students_excel.py      # Export student master list to Excel
├── about.py                      # About page
├── devlopers.py                  # Developers page
│
├── haarcascade_frontalface_default.xml  # Haar cascade for face detection
├── Attend.csv                    # Running attendance log (auto-generated)
├── classifier.xml                # Trained face classifier (generated after training)
│
├── data/                         # Captured face image samples (auto-created)
├── attendance_reports/           # Generated attendance Excel files
├── student_reports/              # Generated student Excel files
├── images/                       # UI image assets
└── requirements.txt              # Python dependencies
```

---

## ⚙️ Requirements

- **Python 3.9.1** (recommended)
- **MySQL Server** running locally

### Python Dependencies

Install all dependencies with:

```bash
pip install -r requirements.txt
```

| Package | Version |
|---|---|
| opencv-contrib-python | 4.13.0.92 |
| Pillow | 8.1.0 |
| numpy | 2.0.2 |
| mysql-connector-python | 9.4.0 |
| openpyxl | 3.1.5 |

---

## 🛠️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/face-recognition-attendance.git
cd face-recognition-attendance
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL Database

Create the database and required tables in your MySQL server:

```sql
CREATE DATABASE face_recognizer;

USE face_recognizer;

CREATE TABLE student (
    studentID     INT PRIMARY KEY AUTO_INCREMENT,
    student_name  VARCHAR(100),
    Roll_no       VARCHAR(50),
    dep           VARCHAR(100),
    course        VARCHAR(100),
    year          VARCHAR(20),
    semester      VARCHAR(20),
    section       VARCHAR(20),
    gender        VARCHAR(20),
    dob           VARCHAR(30),
    email         VARCHAR(100),
    Phone_no      VARCHAR(20),
    address       TEXT,
    teacher_name  VARCHAR(100),
    Photo_Sample  VARCHAR(200)
);

CREATE TABLE users (
    id       INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email    VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);
```

### 4. Update Database Credentials

Open the following files and update the DB credentials to match your MySQL setup:

- `login.py` → `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`
- `face_recognition.py` → connection block inside `face_recog()`
- `generate_attendance_excel.py` → `DB_CONFIG`
- `export_students_excel.py` → `DB_CONFIG`

### 5. Add Images

Place your UI images inside an `images/` folder in the project root. The required image filenames are referenced in each module.

### 6. Run the Application

```bash
python run.py
```

---

## 🚀 Usage Workflow

1. **Login / Register** — Create an account or log in
2. **Add Students** — Go to *Student Details*, fill in info, and capture face samples
3. **Train the Model** — Go to *Train Data* and click **TRAIN DATA** to build the classifier
4. **Take Attendance** — Go to *Face Detector* and click **FACE DETECTOR** to start the webcam
5. **View Reports** — Go to *Attendance Details* to import and manage CSV data
6. **Export Excel** — Attendance Excel is auto-generated after each recognition session in `attendance_reports/`

---

## 📌 Notes

- The system prevents duplicate entries using a **2-minute cooldown** per student per session
- `classifier.xml` is created automatically after training and must exist before running face recognition
- The `data/` folder stores face samples in the format `face.<studentID>.<index>.jpg`
- Attendance Excel reports are saved to `attendance_reports/Attendance_YYYY-MM-DD.xlsx`

---


## 👨‍💻 Developers

Built as an academic project. See the **Developers** section inside the application for team details.

---

## 📄 License

This project is intended for educational purposes.
