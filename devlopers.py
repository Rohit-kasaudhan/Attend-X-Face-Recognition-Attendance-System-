import tkinter as tk
import webbrowser
import math
import random

# ── COLOURS ──────────────────────────────────────────────
BG_DEEP  = "#020810"
BG_CARD  = "#050d1a"
CYAN     = "#00f5ff"
CYAN_DIM = "#00b8c1"
GREEN    = "#00ff88"
BLUE     = "#0ea5e9"
PURPLE   = "#c0b3ff"
PINK     = "#ff4d6a"
BORDER   = "#0e2a3a"
TEXT_WHT = "#e8f8ff"

# ════════════════════════════════════════════════════════
#  TEAM DATA
#  Set "photo" to the full path of the member's image.
#  Example:  "photo": r"C:\Users\You\Pictures\rohit.png"
# ════════════════════════════════════════════════════════
TEAM = [
    {"initial":"M1","name":"Rohit Kasaudhan",
     "photo": "images//rohit.jpeg",
     "linkedin":"https://linkedin.com",
     "github":  "https://github.com",
     "email":   "member1@email.com"},

    {"initial":"M2","name":"Sumit Shah",
     "photo": "images\sumit.png",
     "linkedin":"https://www.linkedin.com/in/contactsumitshah",
     "github":  "https://github.com/sumitshah83326",
     "email":   "sumitshah83840@gmail.com"},

    {"initial":"M3","name":"Swastika Gupta",
     "photo": "images\swastika.jpeg",
     "linkedin":"www.linkedin.com/in/swastika-gupta-a2453a316",
     "github":  "https://github.com/swastika-1",
     "email":   "swastikagupta185@gmail.com"},

    {"initial":"M4","name":"Prince Shah",
     "photo": "images\prince.png",
     "linkedin":"https://www.linkedin.com/in/prince-shah-4ab1303b5/",
     "github":  "https://github.com/princenprusty",
     "email":   "princenpnepal@gmail.com"},

    {"initial":"M5","name":"Krish Rouniyar",
     "photo": "images\kri.png",
     "linkedin":"https://www.linkedin.com/in/krish693",
     "github":  "https://github.com/krish693",
     "email":   "krishrauniyar43@gmail.com"},

    {"initial":"M6","name":"Abhisek Rouniyar",
     "photo": "images//abhisek.png",
     "linkedin": "https://www.linkedin.com/in/abhishekguptarouniyar",
     "github":  "github.com/abhishekrouniyar",
     "email":   "abhishekrouniyar2003@gmail.com"},
]


# ════════════════════════════════════════════════════════
#  ATTEND-X  GLOWING LOGO  (canvas-based, animated)
# ════════════════════════════════════════════════════════
class AttendXLogo(tk.Canvas):
    """
    Animated neon logo in the top-left corner.
    Effects:
      • Multi-layer glow (4 shadow passes) that pulses in brightness
      • Colour cycle: cyan → electric-blue → cyan → green → cyan
      • Flicker: occasional random brightness drop (like a neon sign)
      • Scanline bar that sweeps across the text periodically
    """
    W, H   = 220, 54
    TEXT   = "ATTEND-X"
    FONT   = ("Courier", 22, "bold")

    # colour stops for the cycle  (R, G, B)
    _STOPS = [
        (0, 245, 255),   # cyan
        (0, 180, 255),   # electric blue
        (0, 245, 255),   # cyan
        (0, 255, 160),   # aqua-green
        (0, 245, 255),   # cyan
    ]

    def __init__(self, parent):
        super().__init__(parent, width=self.W, height=self.H,
                         bg=BG_DEEP, highlightthickness=0)
        self._t        = 0.0      # animation clock
        self._flicker  = 1.0     # brightness multiplier
        self._scan_x   = -self.W  # scanline position
        self._scan_on  = False
        self._next_scan()
        self._loop()

    # ── schedule next scan sweep ────────────────────────
    def _next_scan(self):
        delay = random.randint(2500, 6000)
        self.after(delay, self._start_scan)

    def _start_scan(self):
        self._scan_on = True
        self._scan_x  = -30

    # ── interpolate between two colour stops ────────────
    def _interp_color(self):
        stops = self._STOPS
        n     = len(stops) - 1
        pos   = (self._t * 0.4) % n        # full cycle over n steps
        i     = int(pos)
        frac  = pos - i
        r1,g1,b1 = stops[i]
        r2,g2,b2 = stops[(i+1) % len(stops)]
        r = int(r1 + (r2-r1)*frac)
        g = int(g1 + (g2-g1)*frac)
        b = int(b1 + (b2-b1)*frac)
        return r, g, b

    def _dim(self, r, g, b, factor):
        factor = max(0.0, min(1.0, factor))
        return f"#{int(r*factor):02x}{int(g*factor):02x}{int(b*factor):02x}"

    # ── main animation loop ─────────────────────────────
    def _loop(self):
        self.delete("all")
        self._t += 0.05

        # pulse: brightness oscillates 0.55 → 1.0
        pulse = 0.55 + 0.45 * (0.5 + 0.5 * math.sin(self._t * 1.2))

        # random flicker (rare)
        if random.random() < 0.015:
            self._flicker = random.uniform(0.3, 0.7)
        else:
            self._flicker = min(1.0, self._flicker + 0.08)

        brightness = pulse * self._flicker
        r, g, b    = self._interp_color()
        cx, cy     = self.W // 2, self.H // 2

        # glow layers  (outermost → innermost, increasing brightness)
        layers = [
            (8,  0.08),
            (5,  0.18),
            (3,  0.35),
            (1,  0.65),
            (0,  1.00),   # core text
        ]
        for offset, strength in layers:
            col = self._dim(r, g, b, strength * brightness)
            if offset == 0:
                # crisp core text
                self.create_text(cx, cy, text=self.TEXT,
                                 font=self.FONT, fill=col, anchor="center")
            else:
                # blurred shadow copies  (offset in 4 directions)
                for dx, dy in [(offset,0),(-offset,0),(0,offset),(0,-offset)]:
                    self.create_text(cx+dx, cy+dy, text=self.TEXT,
                                     font=self.FONT, fill=col, anchor="center")

        # scanline sweep
        if self._scan_on:
            self._scan_x += 12
            sx = self._scan_x
            scan_col = self._dim(r, g, b, 0.55 * brightness)
            self.create_rectangle(sx, 0, sx+28, self.H,
                                  fill=scan_col, outline="", stipple="gray25")
            if self._scan_x > self.W + 30:
                self._scan_on = False
                self._next_scan()

        # bottom accent line (thin, same colour)
        line_col = self._dim(r, g, b, 0.4 * brightness)
        self.create_line(10, self.H-4, self.W-10, self.H-4,
                         fill=line_col, width=1)

        self.after(30, self._loop)


# ════════════════════════════════════════════════════════
#  GLOW BUTTON
# ════════════════════════════════════════════════════════
class GlowBtn(tk.Canvas):
    def __init__(self, parent, text, color, cmd, w=100, h=30):
        super().__init__(parent, width=w, height=h,
                         bg=BG_CARD, highlightthickness=0, cursor="hand2")
        self.text  = text
        self.color = color
        self.cmd   = cmd
        self.W     = w
        self.H     = h
        self._hov  = False
        self._draw()
        self.bind("<Enter>",    lambda _: self._set(True))
        self.bind("<Leave>",    lambda _: self._set(False))
        self.bind("<Button-1>", lambda _: cmd())

    def _set(self, on):
        self._hov = on
        self._draw()

    def _draw(self):
        self.delete("all")
        fill = "#0a1e2e" if self._hov else BG_CARD
        lw   = 2        if self._hov else 1
        self.create_rectangle(1, 1, self.W-1, self.H-1,
                              outline=self.color, width=lw, fill=fill)
        self.create_text(self.W//2, self.H//2, text=self.text,
                         fill=self.color, font=("Courier", 10, "bold"))


# ════════════════════════════════════════════════════════
#  AVATAR  – static pulsing glow circle
# ════════════════════════════════════════════════════════
class Avatar(tk.Canvas):
    R    = 65
    GLOW = 3

    def __init__(self, parent, data):
        size = (self.R + 20) * 2
        super().__init__(parent, width=size, height=size,
                         bg=BG_CARD, highlightthickness=0)
        self.cx      = self.cy = size // 2
        self.initial = data["initial"]
        self._img    = None
        self._pulse  = 0.0
        self._load(data.get("photo"))
        self._animate()

    def _load(self, path):
        if not path:
            return
        try:
            from PIL import Image, ImageTk, ImageDraw
            d   = self.R * 2
            img = Image.open(path).convert("RGBA")
            w, h  = img.size
            side  = min(w, h)
            left  = (w - side) // 2
            top   = (h - side) // 2
            img   = img.crop((left, top, left+side, top+side))
            img   = img.resize((d, d), Image.LANCZOS)
            mask  = Image.new("L", (d, d), 0)
            ImageDraw.Draw(mask).ellipse((0, 0, d, d), fill=255)
            img.putalpha(mask)
            self._img = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"[Avatar] {e}")

    def _dim_cyan(self, alpha):
        t = alpha / 255
        r = int(0*t   + 5*(1-t))
        g = int(245*t + 13*(1-t))
        b = int(255*t + 26*(1-t))
        return f"#{r:02x}{g:02x}{b:02x}"

    def _animate(self):
        self.delete("all")
        cx, cy, r = self.cx, self.cy, self.R
        pulse_offset = 4 * math.sin(self._pulse)

        for i in range(self.GLOW, 0, -1):
            pr  = r + 8 + i*4 + pulse_offset
            col = self._dim_cyan(int(80 / i))
            self.create_oval(cx-pr, cy-pr, cx+pr, cy+pr,
                             outline=col, width=1)

        self.create_oval(cx-r-2, cy-r-2, cx+r+2, cy+r+2,
                         outline=CYAN, width=2)

        if self._img:
            self.create_image(cx, cy, image=self._img)
        else:
            self.create_oval(cx-r, cy-r, cx+r, cy+r,
                             fill="#0a1628", outline="")
            self.create_text(cx, cy, text=self.initial,
                             font=("Courier", 28, "bold"), fill=CYAN)

        self._pulse += 0.06
        self.after(40, self._animate)


# ════════════════════════════════════════════════════════
#  DEVELOPER CARD
# ════════════════════════════════════════════════════════
class DevCard(tk.Frame):
    def __init__(self, parent, data):
        super().__init__(parent, bg=BG_CARD,
                         highlightbackground=BORDER, highlightthickness=1)
        self._hov = False

        Avatar(self, data).pack(pady=(20, 8))

        self.lbl = tk.Label(self, text=data["name"],
                             font=("Courier", 13, "bold"),
                             fg=TEXT_WHT, bg=BG_CARD)
        self.lbl.pack(pady=(0, 14))

        bf = tk.Frame(self, bg=BG_CARD)
        bf.pack(pady=(0, 22))
        GlowBtn(bf, "LinkedIn", BLUE,
                lambda u=data["linkedin"]: webbrowser.open(u)
                ).pack(side="left", padx=5)
        GlowBtn(bf, "GitHub",   PURPLE,
                lambda u=data["github"]:   webbrowser.open(u)
                ).pack(side="left", padx=5)
        GlowBtn(bf, "Email",    PINK,
                lambda e=data["email"]: webbrowser.open(f"mailto:{e}")
                ).pack(side="left", padx=5)

        self._bind_all(self)

    def _bind_all(self, w):
        w.bind("<Enter>", self._enter, add="+")
        w.bind("<Leave>", self._leave, add="+")
        for child in w.winfo_children():
            self._bind_all(child)

    def _enter(self, _=None):
        if self._hov: return
        self._hov = True
        self.config(highlightbackground=CYAN, highlightthickness=2)
        self.lbl.config(fg=CYAN)

    def _leave(self, _=None):
        self._hov = False
        self.config(highlightbackground=BORDER, highlightthickness=1)
        self.lbl.config(fg=TEXT_WHT)


# ════════════════════════════════════════════════════════
#  PARTICLE BACKGROUND
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
            self.cv.create_oval(p["x"]-r, p["y"]-r,
                                p["x"]+r, p["y"]+r,
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
#  MAIN APP
# ════════════════════════════════════════════════════════
class App:
    def __init__(self, root):
        self.root = root
        root.title("Developers Team")
        root.configure(bg=BG_DEEP)
        root.geometry("1400x820+0+0")

        # particle canvas
        self.bg = tk.Canvas(root, bg=BG_DEEP, highlightthickness=0)
        self.bg.place(relx=0, rely=0, relwidth=1, relheight=1)
        root.update_idletasks()
        Particles(self.bg, root.winfo_width(), root.winfo_height())

        # content frame
        wrap = tk.Frame(root, bg=BG_DEEP)
        wrap.place(relx=0, rely=0, relwidth=1, relheight=1)

        self._header(wrap)
        self._grid(wrap)

    # ── HEADER ─────────────────────────────────────────
    def _header(self, parent):
        hdr = tk.Frame(parent, bg=BG_DEEP)
        hdr.pack(fill="x")

        # ── ATTEND-X animated logo (top-left, absolute) ──
        logo = AttendXLogo(hdr)
        logo.place(x=10, y=6)

        # ── Main title ──
        tk.Label(hdr, text="Developers",
                 font=("Courier", 38, "bold"),
                 fg=CYAN, bg=BG_DEEP).pack(pady=(26, 10))

        # ── Divider ──
        div = tk.Canvas(hdr, height=4, bg=BG_DEEP, highlightthickness=0)
        div.pack(fill="x", padx=60, pady=(0, 20))
        div.update_idletasks()
        dw  = div.winfo_width() or 1280
        mid = dw // 2
        div.create_line(0,      2, mid-8, 2, fill=CYAN_DIM, width=1)
        div.create_line(mid+8,  2, dw,   2, fill=CYAN_DIM, width=1)
        div.create_polygon(mid, 0, mid+6, 2, mid, 4, mid-6, 2,
                           fill=CYAN, outline="")

    # ── 3 × 2 SCROLLABLE GRID ──────────────────────────
    def _grid(self, parent):
        outer = tk.Frame(parent, bg=BG_DEEP)
        outer.pack(fill="both", expand=True, padx=30, pady=0)

        cv = tk.Canvas(outer, bg=BG_DEEP, highlightthickness=0)
        sb = tk.Scrollbar(outer, orient="vertical", command=cv.yview,
                          bg=BG_DEEP, troughcolor=BG_DEEP)
        cv.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        cv.pack(side="left",  fill="both", expand=True)

        inner = tk.Frame(cv, bg=BG_DEEP)
        wid   = cv.create_window((0, 0), window=inner, anchor="nw")

        cv.bind("<Configure>",
                lambda e: cv.itemconfig(wid, width=e.width))
        inner.bind("<Configure>",
                   lambda e: cv.configure(scrollregion=cv.bbox("all")))
        cv.bind_all("<MouseWheel>",
                    lambda e: cv.yview_scroll(-1*(e.delta//120), "units"))

        for idx, dev in enumerate(TEAM):
            row, col = divmod(idx, 3)
            DevCard(inner, dev).grid(row=row, column=col,
                                     padx=18, pady=18, sticky="nsew")
            inner.columnconfigure(col, weight=1)


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
