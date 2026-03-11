from tkinter import *
from tkinter import messagebox
import mysql.connector

# ============================================================
DB_HOST     = "localhost"
DB_USER     = "root"
DB_PASSWORD = "Rohit@3809"
DB_NAME     = "face_recognizer"
# ============================================================

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST, user=DB_USER,
        password=DB_PASSWORD, database=DB_NAME
    )

def ensure_users_table():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id       INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100) NOT NULL,
                email    VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL
            )
        """)
        conn.commit()
        conn.close()
    except:
        pass

ensure_users_table()


# ════════════════════════════════════════════════════════════════
#  PROFESSIONAL LOGIN WINDOW
# ════════════════════════════════════════════════════════════════
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System — Login")
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg="#0a1628")

        # ── LEFT PANEL 60% ────────────────────────────────────────────
        left = Frame(self.root, bg="#0a1628")
        left.place(relx=0, rely=0, relwidth=0.60, relheight=1.0)

        # Decorative canvas for grid lines + circles
        canvas_deco = Canvas(left, bg="#0a1628", highlightthickness=0)
        canvas_deco.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)

        # Subtle grid
        for i in range(0, 1000, 60):
            canvas_deco.create_line(i, 0, i, 800, fill="#0d2240", width=1)
        for j in range(0, 800, 60):
            canvas_deco.create_line(0, j, 1000, j, fill="#0d2240", width=1)

        # Glowing ring accents
        canvas_deco.create_oval(60,  180, 700, 820, outline="#0e3060", width=2)
        canvas_deco.create_oval(140, 240, 640, 760, outline="#0e2a54", width=1)
        canvas_deco.create_oval(220, 300, 580, 700, outline="#0d2442", width=1)

        # Small dot accents
        for dx, dy in [(120,120),(820,90),(880,680),(50,660),(700,400)]:
            canvas_deco.create_oval(dx-4, dy-4, dx+4, dy+4, fill="#1e40af", outline="")

        # Institution logo pill
        logo_bg = Frame(left, bg="#1e3a5f", bd=0)
        logo_bg.place(relx=0.08, rely=0.07, width=180, height=38)
        Label(logo_bg, text="⬡  Attend-X",
              font=("Arial", 22, "bold"),
              bg="#1e3a5f", fg="#60a5fa"
              ).place(relx=0.5, rely=0.5, anchor=CENTER)

        # Main headline
        Label(left,
              text="THE FACE\nRECOGNITION\nATTENDANCE\nSYSTEM",
              font=("Georgia", 46, "bold"),
              bg="#0a1628", fg="white",
              justify=LEFT
              ).place(relx=0.08, rely=0.22)



       

        # ── RIGHT PANEL 40% ───────────────────────────────────────────
        right = Frame(self.root, bg="#f8fafc")
        right.place(relx=0.60, rely=0, relwidth=0.40, relheight=1.0)

        # Top blue bar
        Frame(right, bg="#3b82f6", height=5).place(relx=0, rely=0, relwidth=1.0)

        # Page title
        Label(right, text="Welcome Back",
              font=("Georgia", 30, "bold"),
              bg="#f8fafc", fg="#0a1628"
              ).place(relx=0.5, rely=0.11, anchor=CENTER)

        Label(right, text="Sign in to your dashboard",
              font=("Arial", 11),
              bg="#f8fafc", fg="#64748b"
              ).place(relx=0.5, rely=0.19, anchor=CENTER)

        Frame(right, bg="#e2e8f0", height=1
              ).place(relx=0.08, rely=0.25, relwidth=0.84)

        # ── Email ─────────────────────────────────────────────────────
        Label(right, text="EMAIL ADDRESS",
              font=("Arial", 9, "bold"),
              bg="#f8fafc", fg="#475569"
              ).place(relx=0.10, rely=0.295)

        ef = Frame(right, bg="white",
                   highlightbackground="#cbd5e1", highlightthickness=1)
        ef.place(relx=0.5, rely=0.357, anchor=CENTER, relwidth=0.80, height=48)

        Label(ef, text="✉", font=("Arial", 14),
              bg="white", fg="#94a3b8").place(x=13, rely=0.5, anchor=W)

        self.txt_email = Entry(ef, font=("Arial", 12),
                               bg="white", fg="#0f172a",
                               bd=0, relief=FLAT,
                               insertbackground="#3b82f6")
        self.txt_email.place(x=44, rely=0.5, anchor=W, relwidth=0.80, height=40)

        def ef_in(e):  ef.config(highlightbackground="#3b82f6", highlightthickness=2)
        def ef_out(e): ef.config(highlightbackground="#cbd5e1", highlightthickness=1)
        self.txt_email.bind("<FocusIn>",  ef_in)
        self.txt_email.bind("<FocusOut>", ef_out)

        # ── Password ──────────────────────────────────────────────────
        Label(right, text="PASSWORD",
              font=("Arial", 9, "bold"),
              bg="#f8fafc", fg="#475569"
              ).place(relx=0.10, rely=0.435)

        pf = Frame(right, bg="white",
                   highlightbackground="#cbd5e1", highlightthickness=1)
        pf.place(relx=0.5, rely=0.497, anchor=CENTER, relwidth=0.80, height=48)

        Label(pf, text="🔒", font=("Arial", 12),
              bg="white", fg="#94a3b8").place(x=13, rely=0.5, anchor=W)

        self.txt_pass = Entry(pf, font=("Arial", 12),
                              bg="white", fg="#0f172a",
                              show="●", bd=0, relief=FLAT,
                              insertbackground="#3b82f6")
        self.txt_pass.place(x=44, rely=0.5, anchor=W, relwidth=0.70, height=40)

        self.show_pass = False
        self.eye = Label(pf, text="👁", font=("Arial", 13),
                         bg="white", fg="#94a3b8", cursor="hand2")
        self.eye.place(relx=0.90, rely=0.5, anchor=CENTER)
        self.eye.bind("<Button-1>", self.toggle_password)

        def pf_in(e):  pf.config(highlightbackground="#3b82f6", highlightthickness=2)
        def pf_out(e): pf.config(highlightbackground="#cbd5e1", highlightthickness=1)
        self.txt_pass.bind("<FocusIn>",  pf_in)
        self.txt_pass.bind("<FocusOut>", pf_out)

        # ── SIGN IN button ────────────────────────────────────────────
        self.login_btn = Button(
            right, text="SIGN IN   →",
            command=self.login,
            font=("Arial", 12, "bold"),
            bg="#3b82f6", fg="white",
            activebackground="#2563eb",
            cursor="hand2", bd=0, relief=FLAT
        )
        self.login_btn.place(relx=0.5, rely=0.605,
                             anchor=CENTER, relwidth=0.80, height=52)

        self.login_btn.bind("<Enter>", lambda e: self.login_btn.config(bg="#2563eb"))
        self.login_btn.bind("<Leave>", lambda e: self.login_btn.config(bg="#3b82f6"))

        # ── OR divider ────────────────────────────────────────────────
        Frame(right, bg="#e2e8f0", height=1
              ).place(relx=0.08, rely=0.700, relwidth=0.84)
        Label(right, text="  OR  ",
              font=("Arial", 9, "bold"),
              bg="#f8fafc", fg="#94a3b8"
              ).place(relx=0.5, rely=0.690, anchor=CENTER)

        # ── Register row ──────────────────────────────────────────────
        row = Frame(right, bg="#f8fafc")
        row.place(relx=0.5, rely=0.755, anchor=CENTER)

        Label(row, text="Don't have an account?  ",
              font=("Arial", 11), bg="#f8fafc", fg="#64748b"
              ).pack(side=LEFT)

        reg = Label(row, text="Create Account",
                    font=("Arial", 11, "bold"),
                    bg="#f8fafc", fg="#3b82f6", cursor="hand2")
        reg.pack(side=LEFT)
        reg.bind("<Button-1>", lambda e: self.open_register())
        reg.bind("<Enter>",    lambda e: reg.config(fg="#1d4ed8"))
        reg.bind("<Leave>",    lambda e: reg.config(fg="#3b82f6"))

        # ── Security notice ───────────────────────────────────────────
        sec = Frame(right, bg="#eff6ff", bd=0,
                    highlightbackground="#bfdbfe", highlightthickness=1)
        sec.place(relx=0.5, rely=0.840, anchor=CENTER, relwidth=0.80, height=44)
        Label(sec, text="🔐   Secured with encrypted authentication",
              font=("Arial", 10),
              bg="#eff6ff", fg="#1e40af"
              ).place(relx=0.5, rely=0.5, anchor=CENTER)

        # ── Footer ────────────────────────────────────────────────────
        Label(right,
              text="© 2026 KIIT Face Recognition System  •  All rights reserved",
              font=("Arial", 8),
              bg="#f8fafc", fg="#94a3b8"
              ).place(relx=0.5, rely=0.950, anchor=CENTER)

        # Bottom blue bar
        Frame(right, bg="#3b82f6", height=5
              ).place(relx=0, rely=1.0, relwidth=1.0, y=-5)

        self.root.bind("<Return>", lambda e: self.login())

    def toggle_password(self, e=None):
        self.show_pass = not self.show_pass
        self.txt_pass.config(show="" if self.show_pass else "●")
        self.eye.config(fg="#3b82f6" if self.show_pass else "#94a3b8")

    def login(self):
        email    = self.txt_email.get().strip()
        password = self.txt_pass.get().strip()

        if not email or not password:
            messagebox.showerror("Error", "Both fields are required!", parent=self.root)
            return

        self.login_btn.config(text="Verifying...", state=DISABLED, bg="#64748b")
        self.root.update()

        try:
            conn   = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE email=%s AND password=%s",
                (email, password)
            )
            row = cursor.fetchone()
            conn.close()

            if row is None:
                self.login_btn.config(text="SIGN IN   →", state=NORMAL, bg="#3b82f6")
                messagebox.showerror("Access Denied",
                                     "Invalid email or password.\nPlease try again.",
                                     parent=self.root)
            else:
                self.login_btn.config(text="✓  Access Granted", bg="#16a34a")
                self.root.update()
                self.root.after(900, self._open_main)

        except mysql.connector.Error as err:
            self.login_btn.config(text="SIGN IN   →", state=NORMAL, bg="#3b82f6")
            messagebox.showerror("Database Error", str(err), parent=self.root)

    def _open_main(self):
        self.root.destroy()
        from main import Face_Recognition_System
        new_root = Tk()
        Face_Recognition_System(new_root)
        new_root.mainloop()

    def open_register(self):
        Register(Toplevel(self.root))


# ════════════════════════════════════════════════════════════════
#  PROFESSIONAL REGISTER WINDOW
# ════════════════════════════════════════════════════════════════
class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account — Face Recognition System")
        self.root.geometry("560x700+480+45")
        self.root.resizable(False, False)
        self.root.configure(bg="#f8fafc")

        # Top accent
        Frame(self.root, bg="#3b82f6", height=5).pack(fill=X)

        # Dark header
        header = Frame(self.root, bg="#0a1628", height=100)
        header.pack(fill=X)
        header.pack_propagate(False)

        Label(header, text="Create Your Account",
              font=("Georgia", 21, "bold"),
              bg="#0a1628", fg="white"
              ).place(relx=0.5, rely=0.38, anchor=CENTER)

        Label(header, text="Join the Face Recognition Attendance System",
              font=("Arial", 10),
              bg="#0a1628", fg="#94a3b8"
              ).place(relx=0.5, rely=0.72, anchor=CENTER)

        # Form
        form = Frame(self.root, bg="#f8fafc")
        form.pack(fill=BOTH, expand=True, padx=45, pady=15)

        fields = [
            ("FULL NAME",        "txt_user",    False, "👤"),
            ("EMAIL ADDRESS",    "txt_email",   False, "✉"),
            ("PASSWORD",         "txt_pass",    True,  "🔒"),
            ("CONFIRM PASSWORD", "txt_confirm", True,  "🔒"),
        ]

        for label_text, attr, is_pass, icon in fields:
            Label(form, text=label_text,
                  font=("Arial", 9, "bold"),
                  bg="#f8fafc", fg="#475569"
                  ).pack(anchor=W, pady=(12, 3))

            ff = Frame(form, bg="white",
                       highlightbackground="#cbd5e1", highlightthickness=1)
            ff.pack(fill=X, ipady=3)

            Label(ff, text=icon, font=("Arial", 12),
                  bg="white", fg="#94a3b8").pack(side=LEFT, padx=(10, 0))

            ent = Entry(ff, font=("Arial", 12),
                        bg="white", fg="#0f172a",
                        show="●" if is_pass else "",
                        bd=0, relief=FLAT,
                        insertbackground="#3b82f6")
            ent.pack(side=LEFT, fill=X, expand=True, padx=(8, 10), pady=8)
            setattr(self, attr, ent)

            def _fi(e, f=ff): f.config(highlightbackground="#3b82f6", highlightthickness=2)
            def _fo(e, f=ff): f.config(highlightbackground="#cbd5e1", highlightthickness=1)
            ent.bind("<FocusIn>",  _fi)
            ent.bind("<FocusOut>", _fo)

        # Register button
        self.reg_btn = Button(
            form, text="CREATE ACCOUNT",
            command=self.register_data,
            font=("Arial", 12, "bold"),
            bg="#3b82f6", fg="white",
            activebackground="#2563eb",
            cursor="hand2", bd=0, relief=FLAT
        )
        self.reg_btn.pack(fill=X, pady=(20, 0), ipady=14)
        self.reg_btn.bind("<Enter>", lambda e: self.reg_btn.config(bg="#2563eb"))
        self.reg_btn.bind("<Leave>", lambda e: self.reg_btn.config(bg="#3b82f6"))

        # Footer
        Frame(self.root, bg="#e2e8f0", height=1).pack(fill=X, pady=(12, 0))
        Label(self.root,
              text="© 2026 KIIT Face Recognition System",
              font=("Arial", 8), bg="#f8fafc", fg="#94a3b8"
              ).pack(pady=5)
        Frame(self.root, bg="#3b82f6", height=4).pack(fill=X, side=BOTTOM)

    def register_data(self):
        username = self.txt_user.get().strip()
        email    = self.txt_email.get().strip()
        password = self.txt_pass.get().strip()
        confirm  = self.txt_confirm.get().strip()

        if not username or not email or not password or not confirm:
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return
        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match!", parent=self.root)
            return
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters!", parent=self.root)
            return

        try:
            conn   = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password)
            )
            conn.commit()
            conn.close()

            self.reg_btn.config(text="✓  Account Created!", bg="#16a34a")
            self.root.after(900, lambda: (
                messagebox.showinfo("Success",
                                    f"Welcome, {username}!\nYour account has been created.\nYou can now sign in.",
                                    parent=self.root),
                self.root.destroy()
            ))

        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "This email is already registered!", parent=self.root)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", str(err), parent=self.root)


# ════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    root = Tk()
    Login(root)
    root.mainloop()
