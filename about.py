from errno import ERANGE
import tkinter as tk
import math
import random

# ── COLOURS (identical to devlopers.py) ──────────────────────
BG_DEEP  = "#020810"
BG_CARD  = "#050d1a"
CYAN     = "#00f5ff"
CYAN_DIM = "#00b8c1"
GREEN    = "#00ff88"
BLUE     = "#0ea5e9"
PURPLE   = "#c0b3ff"
PINK     = "#ff4d6a"
YELLOW   = "#ffd700"
BORDER   = "#0e2a3a"
TEXT_WHT = "#e8f8ff"
TEXT_DIM = "#7ca0b8"

# ════════════════════════════════════════════════════════
#  ANIMATED LOGO  (reused from devlopers.py)
# ════════════════════════════════════════════════════════
class AttendXLogo(tk.Canvas):
    W, H = 220, 54
    TEXT = "ATTEND-X"
    FONT = ("Courier", 22, "bold")
    _STOPS = [
        (0, 245, 255),
        (0, 180, 255),
        (0, 245, 255),
        (0, 255, 160),
        (0, 245, 255),
    ]

    def __init__(self, parent):
        super().__init__(parent, width=self.W, height=self.H,
                         bg=BG_DEEP, highlightthickness=0)
        self._t       = 0.0
        self._flicker = 1.0
        self._scan_x  = -self.W
        self._scan_on = False
        self._next_scan()
        self._loop()

    def _next_scan(self):
        self.after(random.randint(2500, 6000), self._start_scan)

    def _start_scan(self):
        self._scan_on = True
        self._scan_x  = -30

    def _interp_color(self):
        stops = self._STOPS
        n     = len(stops) - 1
        pos   = (self._t * 0.4) % n
        i     = int(pos)
        frac  = pos - i
        r1, g1, b1 = stops[i]
        r2, g2, b2 = stops[(i + 1) % len(stops)]
        return (int(r1 + (r2-r1)*frac),
                int(g1 + (g2-g1)*frac),
                int(b1 + (b2-b1)*frac))

    def _dim(self, r, g, b, factor):
        f = max(0.0, min(1.0, factor))
        return f"#{int(r*f):02x}{int(g*f):02x}{int(b*f):02x}"

    def _loop(self):
        self.delete("all")
        self._t += 0.05
        pulse = 0.55 + 0.45 * (0.5 + 0.5 * math.sin(self._t * 1.2))
        if random.random() < 0.015:
            self._flicker = random.uniform(0.3, 0.7)
        else:
            self._flicker = min(1.0, self._flicker + 0.08)
        brightness = pulse * self._flicker
        r, g, b    = self._interp_color()
        cx, cy     = self.W // 2, self.H // 2
        layers = [(8, 0.08), (5, 0.18), (3, 0.35), (1, 0.65), (0, 1.00)]
        for offset, strength in layers:
            col = self._dim(r, g, b, strength * brightness)
            if offset == 0:
                self.create_text(cx, cy, text=self.TEXT,
                                 font=self.FONT, fill=col, anchor="center")
            else:
                for dx, dy in [(offset,0),(-offset,0),(0,offset),(0,-offset)]:
                    self.create_text(cx+dx, cy+dy, text=self.TEXT,
                                     font=self.FONT, fill=col, anchor="center")
        if self._scan_on:
            self._scan_x += 12
            col = self._dim(r, g, b, 0.55 * brightness)
            self.create_rectangle(self._scan_x, 0, self._scan_x+28, self.H,
                                  fill=col, outline="", stipple="gray25")
            if self._scan_x > self.W + 30:
                self._scan_on = False
                self._next_scan()
        line_col = self._dim(r, g, b, 0.4 * brightness)
        self.create_line(10, self.H-4, self.W-10, self.H-4,
                         fill=line_col, width=1)
        self.after(30, self._loop)


# ════════════════════════════════════════════════════════
#  PARTICLE BACKGROUND  (reused from devlopers.py)
# ════════════════════════════════════════════════════════
class Particles:
    def __init__(self, cv, w, h):
        self.cv  = cv
        self.w   = w
        self.h   = h
        self.pts = [self._new() for _ in range(55)]
        self._run()

    def _new(self):
        return {
            "x":  random.uniform(0, self.w),
            "y":  random.uniform(0, self.h),
            "vx": random.uniform(-.3, .3),
            "vy": random.uniform(-.3, .3),
            "r":  random.uniform(1, 2),
            "c":  random.choice([CYAN_DIM, GREEN]),
        }

    def _run(self):
        self.cv.delete("pt")
        for p in self.pts:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            if not (0 <= p["x"] <= self.w and 0 <= p["y"] <= self.h):
                p.update(self._new())
            r = p["r"]
            self.cv.create_oval(p["x"]-r, p["y"]-r, p["x"]+r, p["y"]+r,
                                fill=p["c"], outline="", tags="pt")
        for i, a in enumerate(self.pts):
            for b in self.pts[i+1:]:
                d = math.hypot(a["x"]-b["x"], a["y"]-b["y"])
                if d < 110:
                    self.cv.create_line(a["x"], a["y"], b["x"], b["y"],
                                        fill=CYAN_DIM, width=.4, tags="pt")
        self.cv.tag_lower("pt")
        self.cv.after(40, self._run)


# ════════════════════════════════════════════════════════
#  DIVIDER WIDGET
# ════════════════════════════════════════════════════════
def make_divider(parent, padx=60, pady=(0, 20)):
    div = tk.Canvas(parent, height=4, bg=BG_DEEP, highlightthickness=0)
    div.pack(fill="x", padx=padx, pady=pady)
    def _draw(e=None):
        div.delete("all")
        dw  = div.winfo_width() or 1280
        mid = dw // 2
        div.create_line(0,     2, mid-8, 2, fill=CYAN_DIM, width=1)
        div.create_line(mid+8, 2, dw,   2, fill=CYAN_DIM, width=1)
        div.create_polygon(mid, 0, mid+6, 2, mid, 4, mid-6, 2,
                           fill=CYAN, outline="")
    div.bind("<Configure>", _draw)
    div.after(50, _draw)


# ════════════════════════════════════════════════════════
#  SECTION HEADER
# ════════════════════════════════════════════════════════
def section_header(parent, icon, title, color=CYAN):
    f = tk.Frame(parent, bg=BG_DEEP)
    f.pack(fill="x", padx=60, pady=(30, 6))
    tk.Label(f, text=f"{icon}  {title}",
             font=("Courier", 18, "bold"),
             fg=color, bg=BG_DEEP).pack(anchor="w")
    tk.Canvas(f, height=2, bg=BG_DEEP,
              highlightthickness=0).pack(fill="x", pady=(4, 0))
    line = tk.Canvas(f, height=2, bg=BG_DEEP, highlightthickness=0)
    line.pack(fill="x", pady=(4, 0))
    def _draw(e=None):
        line.delete("all")
        w = line.winfo_width() or 1200
        line.create_line(0, 1, w, 1, fill=color, width=1)
    line.bind("<Configure>", _draw)
    line.after(50, _draw)


# ════════════════════════════════════════════════════════
#  FEATURE CARD
# ════════════════════════════════════════════════════════
class FeatureCard(tk.Frame):
    def __init__(self, parent, icon, title, desc, color=CYAN):
        super().__init__(parent, bg=BG_CARD,
                         highlightbackground=BORDER,
                         highlightthickness=1)
        self._color = color
        self._hov   = False

        # icon circle
        ico_f = tk.Frame(self, bg=BG_CARD)
        ico_f.pack(pady=(18, 6))
        tk.Label(ico_f, text=icon, font=("Segoe UI Emoji", 26),
                 fg=color, bg=BG_CARD).pack()

        tk.Label(self, text=title, font=("Courier", 12, "bold"),
                 fg=color, bg=BG_CARD, wraplength=200).pack(pady=(0, 8))

        tk.Label(self, text=desc, font=("Courier", 9),
                 fg=TEXT_DIM, bg=BG_CARD,
                 wraplength=210, justify="center").pack(padx=14, pady=(0, 18))

        self._bind_all(self)

    def _bind_all(self, w):
        w.bind("<Enter>", self._enter, add="+")
        w.bind("<Leave>", self._leave, add="+")
        for c in w.winfo_children():
            self._bind_all(c)

    def _enter(self, _=None):
        if self._hov: return
        self._hov = True
        self.config(highlightbackground=self._color, highlightthickness=2)

    def _leave(self, _=None):
        self._hov = False
        self.config(highlightbackground=BORDER, highlightthickness=1)


# ════════════════════════════════════════════════════════
#  PIPELINE STEP  (for flow diagram)
# ════════════════════════════════════════════════════════
class PipelineStep(tk.Frame):
    def __init__(self, parent, num, icon, label, sublabel, color, last=False):
        super().__init__(parent, bg=BG_DEEP)

        col_f = tk.Frame(self, bg=BG_DEEP)
        col_f.pack(side="left", fill="y")

        # Number badge
        badge = tk.Canvas(col_f, width=44, height=44,
                          bg=BG_DEEP, highlightthickness=0)
        badge.pack(pady=(4, 0))
        badge.create_oval(2, 2, 42, 42, outline=color, width=2, fill=BG_CARD)
        badge.create_text(23, 23, text=str(num),
                          font=("Courier", 13, "bold"), fill=color)

        # vertical connector line
        if not last:
            line_cv = tk.Canvas(col_f, width=44, height=54,
                                bg=BG_DEEP, highlightthickness=0)
            line_cv.pack()
            line_cv.create_line(22, 0, 22, 54, fill=BORDER, width=2, dash=(4, 3))

        # content
        right = tk.Frame(self, bg=BG_DEEP)
        right.pack(side="left", fill="x", expand=True, padx=14, pady=6)

        tk.Label(right, text=f"{icon}  {label}",
                 font=("Courier", 12, "bold"),
                 fg=color, bg=BG_DEEP, anchor="w").pack(fill="x")
        tk.Label(right, text=sublabel,
                 font=("Courier", 9),
                 fg=TEXT_DIM, bg=BG_DEEP, anchor="w",
                 wraplength=780, justify="left").pack(fill="x", pady=(2, 0))


# ════════════════════════════════════════════════════════
#  TECH BADGE ROW
# ════════════════════════════════════════════════════════
class TechBadge(tk.Frame):
    def __init__(self, parent, icon, name, detail, color):
        super().__init__(parent, bg=BG_CARD,
                         highlightbackground=BORDER,
                         highlightthickness=1)
        inner = tk.Frame(self, bg=BG_CARD)
        inner.pack(padx=16, pady=12)
        tk.Label(inner, text=icon, font=("Segoe UI Emoji", 18),
                 fg=color, bg=BG_CARD).pack(side="left", padx=(0, 10))
        txt = tk.Frame(inner, bg=BG_CARD)
        txt.pack(side="left")
        tk.Label(txt, text=name, font=("Courier", 11, "bold"),
                 fg=color, bg=BG_CARD, anchor="w").pack(fill="x")
        tk.Label(txt, text=detail, font=("Courier", 8),
                 fg=TEXT_DIM, bg=BG_CARD, anchor="w").pack(fill="x")


# ════════════════════════════════════════════════════════
#  STAT CARD  (big number + label)
# ════════════════════════════════════════════════════════
class StatCard(tk.Frame):
    def __init__(self, parent, value, label, color=CYAN):
        super().__init__(parent, bg=BG_CARD,
                         highlightbackground=BORDER,
                         highlightthickness=1,
                         width=170, height=100)
        self.pack_propagate(False)
        tk.Label(self, text=value, font=("Courier", 24, "bold"),
                 fg=color, bg=BG_CARD).pack(pady=(18, 2))
        tk.Label(self, text=label, font=("Courier", 8),
                 fg=TEXT_DIM, bg=BG_CARD).pack()


# ════════════════════════════════════════════════════════
#  MAIN ABOUT APP
# ════════════════════════════════════════════════════════
class About:
    def __init__(self, root):
        self.root = root
        root.title("Attend-X")
        root.configure(bg=BG_DEEP)
        root.geometry("1400x860+0+0")

        # ── particle background ──
        self.bg_cv = tk.Canvas(root, bg=BG_DEEP, highlightthickness=0)
        self.bg_cv.place(relx=0, rely=0, relwidth=1, relheight=1)
        root.update_idletasks()
        Particles(self.bg_cv, root.winfo_width(), root.winfo_height())

        # ── scrollable content over the particles ──
        wrap = tk.Frame(root, bg=BG_DEEP)
        wrap.place(relx=0, rely=0, relwidth=1, relheight=1)

        # outer canvas + scrollbar
        self._cv = tk.Canvas(wrap, bg=BG_DEEP, highlightthickness=0)
        sb = tk.Scrollbar(wrap, orient="vertical", command=self._cv.yview,
                          bg=BG_DEEP, troughcolor=BG_DEEP)
        self._cv.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self._cv.pack(side="left", fill="both", expand=True)

        self._inner = tk.Frame(self._cv, bg=BG_DEEP)
        self._wid   = self._cv.create_window((0, 0), window=self._inner, anchor="nw")

        self._cv.bind("<Configure>",
                      lambda e: self._cv.itemconfig(self._wid, width=e.width))
        self._inner.bind("<Configure>",
                         lambda e: self._cv.configure(
                             scrollregion=self._cv.bbox("all")))
        self._cv.bind_all("<MouseWheel>",
                          lambda e: self._cv.yview_scroll(
                              -1 * (e.delta // 120), "units"))

        # ── build all sections ──
        self._header()
        self._hero()
        self._stats()
        self._features()
        self._flow()
        self._tech_stack()
        self._performance()
        self._limitations()
        self._future()
        self._footer()

    # ─────────────────────────────────────────────────────
    #  HEADER  (logo + title)
    # ─────────────────────────────────────────────────────
    def _header(self):
        hdr = tk.Frame(self._inner, bg=BG_DEEP)
        hdr.pack(fill="x")

        AttendXLogo(hdr).place(x=10, y=6)

        tk.Label(hdr, text="Smart Attendance Face Recognition System",
                 font=("Courier", 22, "bold"),
                 fg=CYAN, bg=BG_DEEP).pack(pady=(28, 6))

        # tk.Label(hdr,
        #          text="Face Recognition · Attendance Automation · AI-Powered",
        #          font=("Courier", 11),
        #          fg=TEXT_DIM, bg=BG_DEEP).pack(pady=(0, 10))

        # make_divider(hdr)

    # ─────────────────────────────────────────────────────
    #  HERO  (one-liner + short description)
    # ─────────────────────────────────────────────────────
    def _hero(self):
        f = tk.Frame(self._inner, bg=BG_CARD,
                     highlightbackground=BORDER, highlightthickness=1)
        f.pack(fill="x", padx=60, pady=(10, 0))

        tk.Label(f,
                 text="  ❝  No more roll-calls. No more proxy.  Just look at the camera.  ❞",
                 font=("Courier", 13, "italic"),
                 fg=YELLOW, bg=BG_CARD,justify="center").pack(pady=(18, 6))

        desc = (
            "Attend-X is a desktop-based Smart Face Recognition Attendance System that automates student "
            "attendance using Python, OpenCV, and Tkinter. It uses real-time facial recognition to identify students and"
            "mark attendance automatically, removing the need for manual roll calls. The system stores student data in a"
            "MySQL database, logs attendance in CSV files, and provides an easy-to-use GUI for administrators and teachers."
        )
        tk.Label(f, text=desc, font=("Courier", 10),
                 fg=TEXT_WHT, bg=BG_CARD,  justify="left",anchor="w",
                 wraplength=1100).pack(pady=(0, 18))

    # ─────────────────────────────────────────────────────
    #  STATS BAR
    # ─────────────────────────────────────────────────────
    def _stats(self):
        section_header(self._inner, "🔄", "At a Glance", CYAN)

        row = tk.Frame(self._inner, bg=BG_DEEP)
        row.pack(padx=60, pady=(0, 10))

        stats = [
            (">90%",    "Recognition\nAccuracy",    GREEN),
            ("<1.5s",   "Avg Detection\nLatency",   CYAN),
            ("< 5%",    "False\nAcceptance Rate",   BLUE),
            ("100+",    "Images Captured\n/ Student", PURPLE),
            ("0",       "Extra Hardware\nNeeded",   YELLOW),
            ("2 Min ",   "Anti-Spam Guard\nPer Student", PINK),
        ]
        for val, lbl, col in stats:
            StatCard(row, val, lbl, col).pack(side="left", padx=10, pady=10)

    # ─────────────────────────────────────────────────────
    #  FEATURES  (3-column card grid)
    # ─────────────────────────────────────────────────────
    def _features(self):
        section_header(self._inner, "🔄","Core Features", CYAN)

        features = [
            ("🔐", "Secure Login",
             "Password-protected admin access. No unauthorised entry to student data or attendance logs.",
             BLUE),
            ("👨‍🎓", "Student Management",
             "Full CRUD — register, update, delete students. Searchable table with all records.",
             GREEN),
            ("📸", "Face Data Capture",
             "Live webcam captures 100+ grayscale images per student, auto-named and sorted by ID.",
             CYAN),
            ("🧠", "Training",
             "One-click LBPH classifier training. Processes the full dataset and saves classifier.xml.",
             PURPLE),
            ("🎯", "Real-Time Recognition",
             "Haar Cascade detects faces; LBPH identifies them. Results shown live on the webcam feed.",
             PINK),
            ("📋", "Smart Attendance Marking",
             "120-second cooldown + date deduplication ensures exactly one record per student per day.",
             YELLOW),
            ("📊", "Attendance Dashboard",
             "Import, view, edit, and export CSV attendance logs. Compatible with Excel and Sheets.",
             CYAN),
            ("🚪", "Unknown Face Alert",
             "Unrecognised faces flagged instantly with a red bounding box — no false attendance.",
             PINK),
            ("👨‍💻", "Developer",
             "Animated team profiles with LinkedIn, GitHub, and Email links for each contributor.",
             BLUE),
        ]

        grid = tk.Frame(self._inner, bg=BG_DEEP)
        grid.pack(padx=60, pady=(0, 10))

        for i, (icon, title, desc, color) in enumerate(features):
            r, c = divmod(i, 3)
            card = FeatureCard(grid, icon, title, desc, color)
            card.grid(row=r, column=c, padx=12, pady=12, sticky="nsew")
            grid.columnconfigure(c, weight=1)

    # ─────────────────────────────────────────────────────
    #  SYSTEM FLOW  (numbered pipeline)
    # ─────────────────────────────────────────────────────
    def _flow(self):
        section_header(self._inner, "🔄", "How Attend-X Works — System Flow", GREEN)

        container = tk.Frame(self._inner, bg=BG_DEEP)
        container.pack(fill="x", padx=80, pady=(0, 10))

        steps = [
            (1,  "🔐", "Admin Login",
             "Administrator launches run.py and authenticates via the secure login screen. "
             "Valid credentials open the main Attend-X dashboard.",
             CYAN, False),

            (2,  "👨‍🎓", "Student Registration",
             "Admin navigates to Student Details, fills in the registration form (Name, Roll No, "
             "Department, DOB, Phone, Email) and saves the record to the MySQL database.",
             GREEN, False),

            (3,  "📸", "Face Dataset Capture",
             "Inside the Student Details module, clicking Take Photos activates the webcam. "
             "100+ grayscale JPEG frames are captured and saved to the data/ folder as "
             "face.{studentID}.{index}.jpg.",
             BLUE, False),

            (4,  "🧠", "Training",
             "The Train Data module reads every image from data, converts them to NumPy arrays, "
             "extracts student IDs from filenames, and trains OpenCV's LBPH FaceRecognizer. "
             "The finished model is serialised to classifier.xml.",
             PURPLE, False),

            (5,  "🎯", "Real-Time Recognition",
             "Face Detector loads haarcascade_frontalface_default.xml and classifier.xml, "
             "opens the webcam, and begins processing frames: BGR→Grayscale → Haar Cascade "
             "detection → LBPH prediction → confidence check (>77%) → MySQL lookup.",
             PINK, False),

            (6,  "✅", "Automatic Attendance Marking",
             "Recognised students have their Roll No, Name, Department, and ID overlaid "
             "on the live feed. mark_attendance() checks the 120-second cooldown and the "
             "existing CSV records before appending a new timestamped entry to Attend.csv.",
             YELLOW, False),

            (7,  "📊", "Review & Export Records",
             "Admin opens Attendance Details, imports Attend.csv into the Treeview table, "
             "optionally edits records, and exports the final CSV — ready for Excel, Google "
             "Sheets, or the institution's reporting system.",
             GREEN, True),
        ]

        for num, icon, label, sub, color, last in steps:
            PipelineStep(container, num, icon, label, sub, color, last).pack(
                fill="x", pady=2)

    # ─────────────────────────────────────────────────────
    #  TECH STACK
    # ─────────────────────────────────────────────────────
    def _tech_stack(self):
        section_header(self._inner,"🔄","Tech Stack", BLUE)

        tech = [
            ("🐍", "Python 3.9+",
             "Core language — clean, cross-platform, huge ecosystem.", CYAN),
            ("👁️", "OpenCV 4.13.0",
             "Haar Cascade face detection + LBPH recognition engine.", GREEN),
            ("🖥️", "Tkinter",
             "Built-in GUI toolkit — zero install dependency, full desktop UI.", BLUE),
            ("🔢", "NumPy",
             "Converts PIL images to uint8 arrays for the LBPH training pipeline.", PURPLE),
            ("🖼️", "Pillow (PIL)",
             "Image loading, grayscale conversion, and GUI photo rendering.", CYAN),
            ("🗄️", "MySQL 8.0",
             "Relational DB for persistent, queryable student records.", PINK),
            ("🔌", "mysql-connector-python",
             "Python ↔ MySQL bridge — DB-API 2.0 compliant.", YELLOW),
            ("📄", "CSV (stdlib)",
             "Portable, human-readable attendance log — opens in any spreadsheet app.", GREEN),
        ]

        grid = tk.Frame(self._inner, bg=BG_DEEP)
        grid.pack(padx=60, pady=(0, 10))

        for i, (icon, name, detail, color) in enumerate(tech):
            r, c = divmod(i, 4)
            TechBadge(grid, icon, name, detail, color).grid(
                row=r, column=c, padx=8, pady=8, sticky="nsew")
            grid.columnconfigure(c, weight=1)

    # ─────────────────────────────────────────────────────
    #  PERFORMANCE TABLE
    # ─────────────────────────────────────────────────────
    def _performance(self):
        section_header(self._inner,"🔄","Performance Benchmarks", YELLOW)

        rows_data = [
            ("Recognition Accuracy",          "> 90%",          "Controlled indoor lighting, frontal face"),
            ("Avg Recognition Latency",        "< 1.5 seconds",  "Per detected face region in frame"),
            ("Model Training Time",            "~45 seconds",    "30 students × 100 images each"),
            ("False Acceptance Rate",          "< 5%",           "With 77% confidence threshold"),
            ("Attendance CSV Write Time",       "< 10 ms",        "Per attendance record appended"),
            ("Duplicate-Prevention Cooldown",  "120 seconds",    "Per student per session"),
        ]

        tbl = tk.Frame(self._inner, bg=BG_DEEP)
        tbl.pack(fill="x", padx=60, pady=(0, 10))

        headers = ["Metric", "Value", "Notes"]
        col_w   = [320, 180, 560]
        h_colors = [CYAN, GREEN, BLUE]

        # header row
        for col, (h, w, c) in enumerate(zip(headers, col_w, h_colors)):
            cell = tk.Frame(tbl, bg=BG_CARD,
                            highlightbackground=BORDER, highlightthickness=1,
                            width=w, height=36)
            cell.pack_propagate(False)
            cell.grid(row=0, column=col, padx=1, pady=1, sticky="nsew")
            tk.Label(cell, text=h, font=("Courier", 10, "bold"),
                     fg=c, bg=BG_CARD).pack(expand=True)

        # data rows
        for r_idx, (metric, val, note) in enumerate(rows_data, start=1):
            bg = BG_CARD if r_idx % 2 == 0 else BG_DEEP
            for col, (text, w) in enumerate(zip([metric, val, note], col_w)):
                fg = [TEXT_WHT, YELLOW, TEXT_DIM][col]
                cell = tk.Frame(tbl, bg=bg,
                                highlightbackground=BORDER, highlightthickness=1,
                                width=w, height=32)
                cell.pack_propagate(False)
                cell.grid(row=r_idx, column=col, padx=1, pady=1, sticky="nsew")
                tk.Label(cell, text=text, font=("Courier", 9),
                         fg=fg, bg=bg).pack(expand=True, padx=6)

    # ─────────────────────────────────────────────────────
    #  KNOWN LIMITATIONS
    # ─────────────────────────────────────────────────────
    def _limitations(self):
        section_header(self._inner, "🔄","Known Limitations", GREEN)

        limits = [
            ("💡", "Lighting Sensitivity",
             "LBPH accuracy drops under harsh backlighting or very low ambient light. "
             "Consistent, diffuse indoor lighting gives the best results."),
            ("📷", "Camera Quality & Angle",
             "Recognition works best at frontal orientation (< 30° from front). "
             "Low-res cameras (below 720p) may degrade accuracy."),
            ("😷", "Occlusion Sensitivity",
             "Face masks, heavy glasses, or partially covered faces can confuse the LBPH model "
             "if training data was captured without those accessories."),
            ("💾", "Local-Only Storage",
             "All data lives on the deployment machine — no cloud sync, no remote access, "
             "single point of failure risk."),
            ("📈", "Linear Scaling",
             "LBPH recognition time grows linearly with registered students. "
             "Noticeable lag may appear in populations above several hundred."),
        ]

        f = tk.Frame(self._inner, bg=BG_DEEP)
        f.pack(fill="x", padx=60, pady=(0, 10))

        for icon, title, desc in limits:
            row = tk.Frame(f, bg=BG_CARD,
                           highlightbackground=BORDER, highlightthickness=1)
            row.pack(fill="x", pady=5)
            tk.Label(row, text=f" {icon}  {title}",
                     font=("Courier", 11, "bold"),
                     fg=PINK, bg=BG_CARD, anchor="w").pack(
                         fill="x", padx=16, pady=(10, 2))
            tk.Label(row, text=desc,
                     font=("Courier", 9),
                     fg=TEXT_DIM, bg=BG_CARD, anchor="w",
                     wraplength=1140, justify="left").pack(
                         fill="x", padx=28, pady=(0, 10))

    # ─────────────────────────────────────────────────────
    #  FUTURE ENHANCEMENTS
    # ─────────────────────────────────────────────────────
    def _future(self):
        section_header(self._inner,"🔄", "Future Roadmap", PURPLE)

        items = [
            ("🤖", "Deep Learning Recognition",
             "Replace LBPH with FaceNet / ArcFace for near-perfect accuracy under pose variation and occlusion.",
             PURPLE),
            ("☁️", "Cloud Database Integration",
             "Migrate MySQL to AWS RDS / Firebase for multi-campus access, remote monitoring, and disaster recovery.",
             BLUE),
            ("📱", "Mobile Monitoring App",
             "iOS / Android companion app for real-time attendance alerts, reports, and early-warning notifications.",
             GREEN),
            ("📊", "Analytics Dashboard",
             "Web-based live dashboard with class-wise rates, department trends, and automated absence alerts.",
             CYAN),
            ("📹", "Multi-Camera Support",
             "Distributed recognition across multiple webcam nodes for large lecture halls and exam centres.",
             YELLOW),
            ("😷", "Mask-Aware Recognition",
             "Models fine-tuned on occluded faces for reliable identification in health-conscious environments.",
             PINK),
        ]

        grid = tk.Frame(self._inner, bg=BG_DEEP)
        grid.pack(padx=60, pady=(0, 10))

        for i, (icon, title, desc, color) in enumerate(items):
            r, c = divmod(i, 3)
            card = tk.Frame(grid, bg=BG_CARD,
                            highlightbackground=BORDER, highlightthickness=1)
            card.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
            grid.columnconfigure(c, weight=1)

            # top accent bar
            accent = tk.Canvas(card, height=3, bg=BG_CARD, highlightthickness=0)
            accent.pack(fill="x")
            def _draw_accent(e, cv=accent, col=color):
                cv.delete("all")
                cv.create_line(0, 1, cv.winfo_width(), 1, fill=col, width=3)
            accent.bind("<Configure>", _draw_accent)
            accent.after(60, lambda cv=accent, col=color:
                         cv.create_line(0, 1, cv.winfo_width() or 400, 1,
                                        fill=col, width=3))

            tk.Label(card, text=f"{icon}  {title}",
                     font=("Courier", 11, "bold"),
                     fg=color, bg=BG_CARD, anchor="w").pack(
                         fill="x", padx=14, pady=(10, 4))
            tk.Label(card, text=desc,
                     font=("Courier", 9),
                     fg=TEXT_DIM, bg=BG_CARD, anchor="w",
                     wraplength=310, justify="left").pack(
                         fill="x", padx=14, pady=(0, 14))

    # ─────────────────────────────────────────────────────
    #  FOOTER
    # ─────────────────────────────────────────────────────
    def _footer(self):
        make_divider(self._inner, padx=60, pady=(30, 10))

        f = tk.Frame(self._inner, bg=BG_DEEP)
        f.pack(pady=(0, 30))

        tk.Label(f, text="Attend-X  —  Face Recognition Attendance System",
                 font=("Courier", 12, "bold"),
                 fg=CYAN, bg=BG_DEEP).pack()

        tk.Label(f,
                 text="Built with  Python · OpenCV · Tkinter · MySQL",
                 font=("Courier", 9),
                 fg=TEXT_DIM, bg=BG_DEEP).pack(pady=(4, 2))

        tk.Label(f,
                 text="Department of Computer Science & Engineering",
                 font=("Courier", 9),
                 fg=TEXT_DIM, bg=BG_DEEP).pack()

        # small animated pulse dot
        dot = tk.Canvas(f, width=12, height=12,
                        bg=BG_DEEP, highlightthickness=0)
        dot.pack(pady=10)
        self._pulse_dot(dot)

    def _pulse_dot(self, cv, t=0.0):
        cv.delete("all")
        r = 4 + 2 * math.sin(t)
        c = 6
        cv.create_oval(c-r, c-r, c+r, c+r, fill=CYAN, outline="")
        cv.after(40, lambda: self._pulse_dot(cv, t + 0.1))


# ════════════════════════════════════════════════════════
#  ENTRY POINT
# ════════════════════════════════════════════════════════
if __name__ == "__main__":
    root = tk.Tk()
    About(root)
    root.mainloop()
