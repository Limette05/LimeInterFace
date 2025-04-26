import random
import tkinter as tk
import tkinter.font as tkfont
import string
import pickle
import os
from tkinter import ttk

import win32.lib.win32con as win32con
import win32gui
import sv_ttk as sv
import webbrowser

# ToDo
# LimeClicker:
# Speicherstand-Funktion


########################################################################################
# Variablen
fB = "Bahnschrift SemiCondensed"
cookies = 0
durchgang = 10
adjektive = ["beste", "liebenswürdigste", "schönste", "größte","stärkste","coolste","reichste","betrunkenste",
             "herzallerliebste","netteste","hübscheste","aufmerksamste","angenehmste","glücklichste"]
nomen = ["Mensch", "Affe", "Freund", "Kumpel", "Programmierer","Dude","Gamer",
         "Hipster","Punk","Mitmensch","Scharfschütze","Mitspieler","Millionär","Angestellte"]
logged_in = False


########################################################################################
# Programme:

def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

########################################################################################


def login():
    class Login():
        def __init__(self):
            self.username = ""
            self.password = ""
            self.empty = {""}
            self.log_on = False
            self.reg_on = False
            self.lcloaded = False
            self.lcreset = False

            self.loop()

        def login(self):
            self.log_on = True
            self.login = tk.Tk()
            sv.use_dark_theme()
            self.login.geometry("350x180")
            self.login.title('Login')
            self.login.configure()
            self.login.resizable(width=False, height=False)
            center(self.login)

            self.f_smol = tkfont.Font(family=fB, size=10)
            self.f_smol_b = tkfont.Font(family=fB, size=10, weight="bold")
            self.f_small = tkfont.Font(family=fB, size=13)
            self.f_small_b = tkfont.Font(family=fB, size=13, weight="bold")
            self.f_button = tkfont.Font(family=fB, size=14, weight="bold")
            self.f_medium = tkfont.Font(family=fB, size=16)
            self.f_medium_b = tkfont.Font(family=fB, size=16, weight="bold")
            self.f_big = tkfont.Font(family=fB, size=20)
            self.f_big_b = tkfont.Font(family=fB, size=20, weight="bold")
            self.f_giant = tkfont.Font(family=fB, size=30, weight="bold")

            self.s = ttk.Style()
            self.s.configure("TButton", font=self.f_button)

            self.F_bottom = ttk.Frame(self.login, )
            self.F_bottom_left = ttk.Frame(self.F_bottom, )
            self.F_bottom_mid = ttk.Frame(self.F_bottom, )
            self.F_bottom_right = ttk.Frame(self.F_bottom, )
            self.F_top = ttk.Frame(self.login, )
            self.F_left = ttk.Frame(self.F_top, )
            self.F_right = ttk.Frame(self.F_top, )

            self.tip_text = tk.StringVar(self.login, "")

            self.L_name = ttk.Label(self.F_left, text="Username:", font=self.f_small)
            self.L_pw = ttk.Label(self.F_left, text="Passwort:", font=self.f_small)
            self.L_tip = ttk.Label(self.F_bottom, textvariable=self.tip_text,font=self.f_smol)

            self.E_name = ttk.Entry(self.F_right)
            self.E_pw = ttk.Entry(self.F_right, show="*")

            self.Btn_login = ttk.Button(self.F_bottom_left, text="Login",command=lambda: self.login_Btn(),
                                       width=11)
            self.remember_var = tk.BooleanVar(self.login)
            self.Check_remember = ttk.Checkbutton(self.F_bottom_right, text="Merken", variable=self.remember_var)
            self.show_var = tk.BooleanVar(self.login)
            self.Check_show = ttk.Checkbutton(self.F_bottom_mid, text="Anzeigen",
                                             command=lambda: self.show_pw(), variable=self.show_var)

            # pack manager
            self.F_top.pack(side="top", expand=True)
            self.F_left.pack(side="left", expand=True)
            self.F_right.pack(side="right", expand=True)
            self.F_bottom.pack(side="bottom", expand=True,fill="x")
            self.L_tip.pack(pady=5)
            self.F_bottom_left.pack(side="left",expand=True)
            self.F_bottom_mid.pack(side="left",expand=True)
            self.F_bottom_right.pack(side="left",expand=True)
            self.L_name.pack(padx=30,pady=10)
            self.L_pw.pack(padx=30,pady=10)

            self.Btn_login.pack(side="left",expand=True)
            self.Check_remember.pack(side="left",expand=True)
            self.Check_show.pack(side="left",expand=True)

            self.E_name.pack(side="top", pady=4, padx=30)
            self.E_pw.pack(side="top", pady=4, padx=30)

            self.login.bind("<Return>",lambda event: self.login_Btn())
            self.login.mainloop()

        def show_pw(self):
            self.E_pw.configure(show="")
            self.Check_show.configure(command=lambda: self.hide_pw())

        def hide_pw(self):
            self.E_pw.configure(show="*")
            self.Check_show.configure(command=lambda: self.show_pw())

        def show_pw2(self):
            if not self.E_pw2.get() == "Passwort bestätigen":
                self.E_pw2.configure(show="")
            if not self.E_pw.get() == "mind. 6 Zeichen":
                self.E_pw.configure(show="")
            self.Check_show.configure(command=lambda: self.hide_pw2())

        def hide_pw2(self):
            if not self.E_pw2.get() == "Passwort bestätigen":
                self.E_pw2.configure(show="*")
            if not self.E_pw.get() == "mind. 6 Zeichen":
                self.E_pw.configure(show="*")
            self.Check_show.configure(command=lambda: self.show_pw2())

        def register(self):
            self.reg_on = True
            self.register = tk.Tk()
            sv.use_dark_theme()
            self.register.geometry("320x200")
            self.register.title('Registrieren')
            self.register.configure()
            self.register.resizable(width=False, height=False)
            center(self.register)

            self.f_smol = tkfont.Font(family=fB, size=10)
            self.f_smol_b = tkfont.Font(family=fB, size=10, weight="bold")
            self.f_small = tkfont.Font(family=fB, size=13)
            self.f_small_b = tkfont.Font(family=fB, size=13, weight="bold")
            self.f_button = tkfont.Font(family=fB, size=14, weight="bold")
            self.f_medium = tkfont.Font(family=fB, size=16)
            self.f_medium_b = tkfont.Font(family=fB, size=16, weight="bold")
            self.f_big = tkfont.Font(family=fB, size=20)
            self.f_big_b = tkfont.Font(family=fB, size=20, weight="bold")
            self.f_giant = tkfont.Font(family=fB, size=30, weight="bold")

            self.s = ttk.Style()
            self.s.configure("TButton", font=self.f_button)

            self.F_bottom = ttk.Frame(self.register, )
            self.F_bottom_left = ttk.Frame(self.F_bottom, )
            self.F_bottom_mid = ttk.Frame(self.F_bottom, )
            self.F_bottom_right = ttk.Frame(self.F_bottom, )
            self.F_top = ttk.Frame(self.register, )
            self.F_left = ttk.Frame(self.F_top, )
            self.F_right = ttk.Frame(self.F_top, )

            self.tip_text = tk.StringVar(self.register, "")

            self.L_name = ttk.Label(self.F_left, text="Username:", font=self.f_small)
            self.L_pw = ttk.Label(self.F_left, text="Passwort:", font=self.f_small)
            self.L_pw2 = ttk.Label(self.F_left, text="Bestätigen:", font=self.f_small)
            self.L_tip = ttk.Label(self.F_bottom, textvariable=self.tip_text,
                                  font=self.f_smol)

            self.E_name = ttk.Entry(self.F_right,width=40)
            self.E_pw = ttk.Entry(self.F_right,width=40)
            self.E_pw2 = ttk.Entry(self.F_right,width=40)

            self.Btn_register = ttk.Button(self.F_bottom_left, text="Registrieren",command=lambda: self.register_Btn(),
                                       width=11)
            self.remember_var = tk.BooleanVar(self.register)
            self.Check_remember = ttk.Checkbutton(self.F_bottom_right, text="Merken", variable=self.remember_var)
            self.show_var = tk.BooleanVar(self.register)
            self.Check_show = ttk.Checkbutton(self.F_bottom_mid, text="Anzeigen",
                                             command=lambda: self.show_pw2(), variable=self.show_var)

            # pack manager
            self.F_top.pack(side="top", expand=True)
            self.F_left.pack(side="left", expand=True)
            self.F_right.pack(side="right", expand=True)
            self.F_bottom.pack(side="bottom", expand=True, fill="x")

            self.L_tip.pack(pady=5)

            self.F_bottom_left.pack(side="left", expand=True,pady=5)
            self.F_bottom_mid.pack(side="left", expand=True,pady=5)
            self.F_bottom_right.pack(side="left", expand=True,pady=5)

            self.L_name.pack(padx=30,pady=10)
            self.L_pw.pack(padx=30,pady=10)
            self.L_pw2.pack(padx=30,pady=10)

            self.Btn_register.pack(expand=True)
            self.Check_show.pack(expand=True)
            self.Check_remember.pack(expand=True)

            self.E_name.pack(side="top",pady=4,padx=30)
            self.E_name.insert(0, "mind. 4 Zeichen")
            self.E_name.bind('<FocusIn>', lambda event: self.in_name())
            self.E_name.bind('<FocusOut>', lambda event: self.out_name())
            self.E_pw.pack(side="top",pady=4,padx=30)
            self.E_pw.insert(0, "mind. 6 Zeichen")
            self.E_pw.bind('<FocusIn>', lambda event: self.in_pw1())
            self.E_pw.bind('<FocusOut>', lambda event: self.out_pw1())
            self.E_pw2.pack(side="top",pady=4,padx=30)
            self.E_pw2.insert(0, "Passwort bestätigen")
            self.E_pw2.bind('<FocusIn>', lambda event: self.in_pw2())
            self.E_pw2.bind('<FocusOut>', lambda event: self.out_pw2())

            self.register.bind("<Return>", lambda event: self.register_Btn())
            self.register.mainloop()

        def in_pw1(self):
            if self.E_pw.get() == "mind. 6 Zeichen":
                self.E_pw.delete(0, "end")
                self.E_pw.insert(0, "")
                if not self.show_var.get():
                    self.E_pw.configure(show="*")

        def out_pw1(self):
            if self.E_pw.get() == "":
                self.E_pw.insert(0, "mind. 6 Zeichen")
                self.E_pw.configure(show="")

        def in_pw2(self):
            if self.E_pw2.get() == "Passwort bestätigen":
                self.E_pw2.delete(0, "end")
                self.E_pw2.insert(0, "")
                if not self.show_var.get():
                    self.E_pw2.configure(show="*")

        def out_pw2(self):
            if self.E_pw2.get() == "":
                self.E_pw2.insert(0, "Passwort bestätigen")
                self.E_pw2.configure(show="")

        def in_name(self):
            if self.E_name.get() == "mind. 4 Zeichen":
                self.E_name.delete(0, "end")
                self.E_name.insert(0, "")
                self.E_name.configure()

        def out_name(self):
            if self.E_name.get() == "":
                self.E_name.insert(0, "mind. 4 Zeichen")
                self.E_name.configure()

#####################################################################
        def Root1(self):
            self.root = tk.Tk()
            sv.use_dark_theme()

            self.f_smol = tkfont.Font(family=fB, size=10)
            self.f_smol_b = tkfont.Font(family=fB, size=10, weight="bold")
            self.f_small = tkfont.Font(family=fB, size=13)
            self.f_small_b = tkfont.Font(family=fB, size=13, weight="bold")
            self.f_button = tkfont.Font(family=fB, size=14, weight="bold")
            self.f_medium = tkfont.Font(family=fB, size=16)
            self.f_medium_b = tkfont.Font(family=fB, size=16, weight="bold")
            self.f_big = tkfont.Font(family=fB, size=20)
            self.f_big_b = tkfont.Font(family=fB, size=20, weight="bold")
            self.f_giant = tkfont.Font(family=fB, size=30, weight="bold")

            self.s = ttk.Style()
            self.s.configure("TButton", font=self.f_button)

            self.Root()

        def Root2(self):
            self.root = tk.Toplevel()
            self.Root()

        def Root(self):
            self.root.geometry("700x400")
            center(self.root)
            self.root.title("LIF 1.6")
            self.root.resizable(width=False,height=False)

            self.s = ttk.Style()
            self.s.configure("TButton", font=self.f_button)

            self.root_in = ttk.Frame(self.root)
            self.up = ttk.Frame(self.root_in)
            self.top = ttk.Frame(self.root_in)
            self.top2 = ttk.Frame(self.root_in)
            self.topl = ttk.Frame(self.top2)
            self.topr = ttk.Frame(self.top2)
            self.midholder = ttk.Frame(self.root_in)
            self.mid = ttk.Frame(self.root_in)
            self.midl = ttk.Frame(self.mid)
            self.midr = ttk.Frame(self.mid)
            self.bot = ttk.Frame(self.root_in)
            self.bot2 = ttk.Frame(self.root_in)
            self.bot2l = ttk.Frame(self.root_in)
            self.bot2r = ttk.Frame(self.root_in)

            self.vollbild_text = tk.StringVar(self.root, "")
            self.countdown_text = tk.StringVar(self.root, durchgang)
            self.greetsl = tk.StringVar(self.root, f"{random.choice(adjektive)}")
            self.greetsr = tk.StringVar(self.root, f"{random.choice(nomen)}!")

            # Bilder:
            self.P_cookie = tk.PhotoImage(file="./assets/cookie.png")

            # Label:
            self.namecheck = pickle.load(open("assets/username.txt", "rb"))
            self.Head = ttk.Label(self.top,
                                  text=f"Willkommen {self.namecheck}, im ersten LimeInterFace, kurz LIF",
                                  font=self.f_big)
            self.greeting = ttk.Label(self.topl, text=("Du  bist  der "), font=self.f_medium)
            self.greetingsl = tk.Button(self.topr, textvariable=self.greetsl, borderwidth=0,
                                        activebackground="grey11",
                                        font=self.f_medium, command=lambda: self.wduschel())
            self.greetingsr = tk.Button(self.topr, textvariable=self.greetsr, borderwidth=0,
                                        activebackground="grey11",
                                        font=self.f_medium, command=lambda: self.wduscher())

            self.hobbyloscount = 0
            self.menuBtn = ttk.Button(self.midl, text="Menü", command=lambda: self.Appmenu(),
                                      width=15)

            self.B_exit = ttk.Button(self.midr, text=("Beenden"), command=lambda: self.beenden(),
                                     width=15)

            self.vbild = ttk.Label(self.bot, textvariable=self.vollbild_text, font=self.f_small_b)
            self.dev = ttk.Label(self.bot2l, text="LIF by @BossLimette :", font=self.f_small)
            self.log = tk.Button(self.bot2r, text="Changelog", borderwidth=0, activebackground="grey11",
                                 font=self.f_small, command=lambda: self.Changelog())

            self.root_in.pack(expand=True,fill="both")
            self.up.pack(pady=20)
            self.top.pack(fill="x")
            self.top2.pack(fill="x")
            self.topl.pack(expand=True, fill="x", side="left")
            self.topr.pack(expand=True, fill="x", side="right")
            self.midholder.pack(pady=30)
            self.mid.pack(expand=True, fill="both")
            self.midl.pack(expand=True, fill="both", side="left")
            self.midr.pack(expand=True, fill="both", side="right")
            self.bot.pack(expand=True, fill="both")
            self.bot2.pack(fill="x")
            self.bot2l.pack(expand=True, fill="x", side="left")
            self.bot2r.pack(expand=True, fill="x", side="right")

            self.Head.pack()
            self.greeting.pack(side="right")
            self.greetingsl.pack(side="left")
            self.greetingsr.pack(side="left")

            self.menuBtn.pack(padx=30, side="right")
            self.B_exit.pack(padx=30, side="left")

            self.vbild.pack(side="bottom", pady=5)

            self.dev.pack(side="right", pady=5)
            self.log.pack(side="left", pady=5)

            self.root.bind("<F11>", self.toggle_fullscreen)
            self.root.protocol("WM_DELETE_WINDOW", lambda: self.close())

            self.save_remember = open("assets/login.txt", "a")
            self.save_remember.close()
            self.remember_read = pickle.load(open("assets/login.txt", "rb"))

            self.root.mainloop()

#        def hobbylos(self):
#            self.hobbyloscount += 1
#            if self.hobbyloscount >= 100:
#                self.hobbylostext.set("Herzlichen Glückwunsch, du bist so hobbylos, dass du diesen Knopf 100 mal gedrückt hast!")
#            if self.hobbyloscount >= 1000:
#                self.hobbylostext.set("Du hast diesen Knopf... 1000 MAL gedrückt! WARUM?!")

        def wduschel(self):
            self.greeting.pack()
            self.greetl = random.choice(adjektive)
            self.greetsl.set(f"{self.greetl}")

        def wduscher(self):
            self.greeting.pack()
            self.greetr = random.choice(nomen)
            self.greetsr.set(f"{self.greetr}!")

        def beenden(self):
            self.empty = {""}
            self.remember_read = "0"
            self.save_remember = open("assets/login.txt", "a")
            self.save_remember.close()
            self.remember_read = pickle.load(open("assets/login.txt", "rb"))

            if self.remember_read == "1":
                self.pick = tk.Toplevel()
                self.pick.title("Beenden")
                self.pick.geometry("300x100")
                self.pick.resizable(width=False, height=False)
                self.pick.configure()
                center(self.pick)

                self.F_top = ttk.Frame(self.pick)
                self.F_bottom = ttk.Frame(self.pick)

                self.L_sure = ttk.Label(self.F_top, text="Nur schließen oder auch abmelden?",
                                        font=self.f_small).pack()
                self.Btn_beenden = ttk.Button(self.F_bottom, text="Schließen",
                                              command=lambda: self.schliessen(), width=10)
                self.Btn_abmelden = ttk.Button(self.F_bottom, text="Abmelden",
                                               command=lambda: self.abmelden(), width=10)

                self.F_top.pack(side="top", expand=True)
                self.F_bottom.pack(side="bottom", expand=True)
                self.Btn_beenden.pack(side="left", expand=True, padx=5)
                self.Btn_abmelden.pack(side="right", expand=True, padx=5)

                self.focus = 0
                self.pick.bind("<FocusIn>", self.exit_in)
                self.pick.bind("<FocusOut>", self.exit_out)

            else:
                self.close()

        def exit_in(self, event):
            self.focus += 1

        def exit_out(self, event):
            self.focus -= 1
            if self.focus == 0:
                self.pick.destroy()

        def close(self):
            self.root.destroy()
            if self.log_on == True:
                self.login.destroy()
            elif self.reg_on == True:
                self.register.destroy()

        def schliessen(self):
            self.pick.destroy()
            self.root.destroy()
            if self.log_on == True:
                self.login.destroy()
            elif self.reg_on == True:
                self.register.destroy()

        def abmelden(self):
            pickle.dump("0", open("assets/login.txt", "wb"))
            self.pick.destroy()
            self.root.destroy()
            if self.log_on == True:
                self.login.destroy()
            elif self.reg_on == True:
                self.register.destroy()

        def toggle_fullscreen(self, event):
            if (self.root.attributes('-fullscreen')):
                self.root.attributes('-fullscreen', False)
                self.vbild.pack_forget()
                self.vollbild_text.set("Vollbildmodus aus")
                self.vbild.pack(side="bottom", pady=5)
                self.bot.after(1500, lambda: self.vbild.pack_forget())

            else:
                self.root.attributes('-fullscreen', True)
                self.vbild.pack_forget()
                self.vollbild_text.set("Vollbildmodus an")
                self.vbild.pack(side="bottom", pady=5)
                self.bot.after(1500, lambda: self.vbild.pack_forget())

        def callback(self,url):
            webbrowser.open_new(url)

        def Changelog(self):
            self.main_menu = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(self.main_menu, win32con.SW_HIDE)

            self.changelog = tk.Toplevel()
            self.changelog.geometry("500x400")
            self.changelog.title('Changelog')
            self.changelog.resizable(width=False, height=False)
            center(self.changelog)

            self.tophead = ttk.Frame(self.changelog)
            self.head1 = ttk.Frame(self.changelog)
            self.underhead1 = ttk.Frame(self.changelog)
            self.text1 = ttk.Frame(self.changelog)
            self.bottom = ttk.Frame(self.changelog)

            self.Logs = ttk.Label(self.tophead, text="Changelog:", font=self.f_big)
            self.L_head1 = ttk.Label(self.head1, text="v1.6", font=self.f_medium_b)
            self.L_underhead1 = ttk.Label(self.underhead1, text="[ 25.07.2022, 01:12 CET ]", font=self.f_smol_b)
            self.L_text1 = ttk.Label(self.text1, font=self.f_small, text=("""
              Interaktives App-Menü

               LimeClicker optimiert
- Speicherstand kann noch kaputt gehen

                    Neues Design:
            - Sun Valley Theme von"""))
            self.L_htext1 = tk.Label(self.text1, font=self.f_small, text="@rdbende",bg="grey11",fg="limegreen")
            self.L_htext1.bind("<ButtonRelease-1>", lambda e: self.callback("https://github.com/rdbende"))

            self.L_sign = ttk.Label(self.bottom, text="LIF by Boss Limette", font=self.f_smol)

            self.tophead.pack()
            self.head1.pack()
            self.underhead1.pack()
            self.text1.pack()
            self.bottom.pack(side="bottom")

            self.Logs.pack()
            self.L_head1.pack()
            self.L_underhead1.pack()
            self.L_text1.pack(fill="x")
            self.L_htext1.pack(fill="x")
            self.L_sign.pack(side="bottom")

            self.changelog.protocol("WM_DELETE_WINDOW", lambda: self.exit_devlog())

        def exit_devlog(self):
            self.changelog.destroy()
            win32gui.ShowWindow(self.main_menu, win32con.SW_SHOW)


######################################################################################################
######################################################################################################


        def Appmenu(self):
            self.lc_cookies = 0

            self.lc_ac_min = 9
            self.lc_ac_cost = 10
            self.lc_ac_newcost = 10
            self.lc_ac_zaehler = 0
            self.lc_ac_count = 0

            self.lc_af_min = 99
            self.lc_af_faktor = 1.2
            self.lc_af_faktor_temp = 1
            self.lc_af_cost = 100
            self.lc_af_newcost = 100
            self.lc_af_zaehler = 0
            self.lc_af_count = 0

            self.lc_mc_min = 99
            self.lc_mc_faktor = 1.2
            self.lc_mc_faktor_temp = 1
            self.lc_mc_cost = 100
            self.lc_mc_newcost = 100
            self.lc_mc_zaehler = 0
            self.lc_mc_count = 0

            self.lc_autofaktor = 1

            self.lc_multiclick = 1


            self.main_menu = win32gui.GetForegroundWindow()
            if not self.lcreset:
                win32gui.ShowWindow(self.main_menu, win32con.SW_HIDE)
                self.lcreset = False
            self.lc_active = False
            self.lk_active = False
            self.lc_loaded = False
            self.pw_active = False
            self.lk_saved = False

            self.appmenu = tk.Toplevel()
            self.appmenu.geometry("960x540")
            self.appmenu.title('App Menü')
            self.appmenu.resizable(width=False, height=False)
            center(self.appmenu)

            self.titel = ttk.Label(self.appmenu, text="",font=self.f_small)
            self.menutext = ttk.Label(self.appmenu, text="Menü",font=self.f_small)

            self.left = ttk.Labelframe(self.appmenu, labelwidget=self.menutext,width=200,labelanchor="n")
            self.right = ttk.Labelframe(self.appmenu, labelwidget=self.titel,labelanchor="n")
            self.display = ttk.Frame(self.right)


            self.backBtn = ttk.Button(self.left, text="Zurück",command=lambda: self.exit_appmenu(),width=15)
            self.pwgenBtn = ttk.Button(self.left, text="PW-Generator",
                                       command=lambda: self.useBtn("Passwort-Generator",self.pwgen_f,self.pwgenBtn),width=15)
            self.lcBtn = ttk.Button(self.left, text="LimeClicker",
                                       command=lambda: self.useBtn("LimeClicker",self.lc_start,self.lcBtn),width=15)
            self.lkBtn = ttk.Button(self.left, text="LimeKarten",
                                       command=lambda: self.useBtn("LimeKarten",self.limekarten,self.lkBtn),width=15)


            self.left.pack(side="left",fill="y",pady=10,padx=10)
            self.right.pack(side="right",fill="both",pady=10,padx=10,expand=True)
            self.display.pack(expand=True,fill="both",padx=5,pady=5)
            self.backBtn.pack(fill="x",pady=5,padx=10)
            self.pwgenBtn.pack(fill="x",pady=5,padx=10)
            self.lcBtn.pack(fill="x",pady=5,padx=10)
            self.lkBtn.pack(fill="x",pady=5,padx=10)

            self.appmenu.protocol("WM_DELETE_WINDOW", lambda: self.exit_appmenu())

        def exit_appmenu(self):
            self.lc_closelc()
            self.appmenu.destroy()
            win32gui.ShowWindow(self.main_menu, win32con.SW_SHOW)

        def pw_checkpw(self):
            if self.pw_active:
                self.pwgenBtn.configure(state=tk.NORMAL)
                self.pw_active = False

        def lk_checklk(self):
            if self.lk_active:
                self.lkBtn.configure(state=tk.NORMAL)
                self.lk_active = False

        def lc_checklc(self):
            if self.lc_active:
                self.lcBtn.configure(state=tk.NORMAL)
                self.lc_active = False

        def lc_closelc(self):
            if self.lc_loaded:
                pickle.dump(round(self.lc_cookies), open("assets/cookies.txt", "wb"))
                pickle.dump(self.lc_ac_count, open("assets/autoclick.txt", "wb"))
                pickle.dump(self.lc_af_count, open("assets/autofaktor.txt", "wb"))
                pickle.dump(self.lc_mc_count, open("assets/multiclick.txt", "wb"))
                self.lcBtn.configure(state=tk.NORMAL)
                self.lc_loaded = False
            #if prestige > 1:
                #speicher prestige in config


        def useBtn(self,newtitel,newapp,appBtn):
            appBtn.configure(state=tk.DISABLED)
            self.pw_checkpw()
            self.lc_checklc()
            self.lk_checklk()
            self.titel.configure(text=newtitel)
            for widgets in self.display.winfo_children():
                widgets.destroy()
            newapp()

        def pwgen_f(self):
            self.pw_active = True
            self.pw_upper = string.ascii_uppercase
            self.pw_lower = string.ascii_lowercase
            self.pw_digits = string.digits
            self.pw_symbols = string.punctuation
            self.pw_contents = (self.pw_upper + self.pw_lower + self.pw_digits + self.pw_symbols)
            self.pw_ups = True
            self.pw_lows = True
            self.pw_numbs = True
            self.pw_symbs = True

            self.pw_laenge = range(2, 101)

            self.pw_option_var = tk.StringVar(self.appmenu)

            self.pw_create_widgets()

        def pw_get_length(self):
            try:
                value = int(self.pw_option_var.get())
                if value > 100:
                    value = 100
                elif value < 6:
                    value = 6
                return value
            except Exception as e:
                print(e)

        def pw_create_widgets(self):
            self.pw_F_overall = ttk.Frame(self.display)
            self.pw_F_left = ttk.Frame(self.pw_F_overall)
            self.pw_F_left_top = ttk.Frame(self.pw_F_left)
            self.pw_F_left_bottom = ttk.Frame(self.pw_F_left)
            self.pw_F_left_bottom2 = ttk.Frame(self.pw_F_left)
            self.pw_F_left_bottom3 = ttk.Frame(self.pw_F_left)
            self.pw_F_right = ttk.Frame(self.pw_F_overall)

            self.pw_text_upper = tk.StringVar(self.appmenu, "ABC: An")
            self.pw_text_lower = tk.StringVar(self.appmenu, "abc: An")
            self.pw_text_digits = tk.StringVar(self.appmenu, "123: An")
            self.pw_text_symbols = tk.StringVar(self.appmenu, "%<&: An")

            self.pw_Btn_upper = ttk.Button(self.pw_F_left_bottom, textvariable=self.pw_text_upper,command=lambda: self.pw_content(0),
                                       width=10)
            self.pw_Btn_lower = ttk.Button(self.pw_F_left_bottom, textvariable=self.pw_text_lower,
                                       command=lambda: self.pw_content(1),
                                       width=10)
            self.pw_Btn_digits = ttk.Button(self.pw_F_left_bottom2, textvariable=self.pw_text_digits,
                                       command=lambda: self.pw_content(2),
                                       width=10)
            self.pw_Btn_symbols = ttk.Button(self.pw_F_left_bottom2, textvariable=self.pw_text_symbols,
                                       command=lambda: self.pw_content(3),
                                       width=10)
            self.pw_Btn_gen = ttk.Button(self.pw_F_left_bottom3, text="Generieren",
                                      command=lambda: self.pw_generator(self.pw_get_length()),
                                      width=10)
            self.pw_Btn_copy = ttk.Button(self.pw_F_left_bottom3, text="Kopieren", command=lambda: self.pw_copy(),
                                       width=10)

            self.pw_label = ttk.Label(self.pw_F_left_top, text='Passwortlänge: ',font=self.f_small)
            self.pw_option_menu = ttk.Combobox(self.pw_F_left_top, textvariable=self.pw_option_var, values=(1, *self.pw_laenge))

            self.pw_textbox = tk.Text(self.pw_F_right, height=10, width=28, bg="grey28", fg="white")
            self.pw_textbox.configure(state=tk.DISABLED)


            self.pw_textbox.pack(side="left")
            self.pw_F_overall.pack(expand=True)
            self.pw_F_left.pack(side="left", padx=7, pady=7)
            self.pw_F_left_top.pack(side="top",expand=True,)
            self.pw_F_left_bottom.pack(expand=True,fill="both")
            self.pw_F_left_bottom2.pack(expand=True,fill="both")
            self.pw_F_left_bottom3.pack(side="bottom",expand=True,fill="both")
            self.pw_F_right.pack(side="right", padx=7, pady=7)

            self.pw_label.pack(side="left", padx=5,pady=5)

            self.pw_option_menu.pack(side="right", padx=5,pady=5)

            self.pw_Btn_upper.pack(side="left",expand=True,fill="both",padx=3,pady=3)
            self.pw_Btn_lower.pack(side="left",expand=True,fill="both",padx=3,pady=3)
            self.pw_Btn_digits.pack(side="left",expand=True,fill="both",padx=3,pady=3)
            self.pw_Btn_symbols.pack(side="left",expand=True,fill="both",padx=3,pady=3)
            self.pw_Btn_gen.pack(side="left",expand=True,fill="both",padx=3,pady=3)
            self.pw_Btn_copy.pack(side="left",expand=True,fill="both",padx=3,pady=3)

        def pw_generator(self, pw_length):
            self.pw_pwtemp = random.choices((self.pw_upper+self.pw_lower+self.pw_digits+self.pw_symbols),
                                            weights=None, cum_weights=None, k=pw_length)
            self.pw_passwort = "".join(self.pw_pwtemp)
            self.pw_textbox.configure(state=tk.NORMAL)
            self.pw_textbox.delete(1.0, 'end')
            self.pw_textbox.insert('end', self.pw_passwort)
            self.pw_textbox.configure(state=tk.DISABLED)

        def pw_content(self,pw_choice):
            if pw_choice == 0:
                if not self.pw_ups:
                    self.pw_upper = string.ascii_uppercase
                    self.pw_ups = True
                    self.pw_text_upper.set("ABC: An")
                else:
                    self.pw_upper = ''
                    self.pw_ups = False
                    self.pw_text_upper.set("ABC: Aus")
            if pw_choice == 1:
                if not self.pw_lows:
                    self.pw_lower = string.ascii_lowercase
                    self.pw_lows = True
                    self.pw_text_lower.set("abc: An")
                else:
                    self.pw_lower = ''
                    self.pw_lows = False
                    self.pw_text_lower.set("abc: Aus")
            if pw_choice == 2:
                if not self.pw_numbs:
                    self.pw_digits = string.digits
                    self.pw_numbs = True
                    self.pw_text_digits.set("123: An")
                else:
                    self.pw_digits = ''
                    self.pw_numbs = False
                    self.pw_text_digits.set("123: Aus")
            if pw_choice == 3:
                if not self.pw_symbs:
                    self.pw_symbols = string.punctuation
                    self.pw_symbs = True
                    self.pw_text_symbols.set("%<&: An")
                else:
                    self.pw_symbols = ''
                    self.pw_symbs = False
                    self.pw_text_symbols.set("%<&: Aus")

        def pw_copy(self):
            value = self.pw_passwort
            self.appmenu.clipboard_clear()
            self.appmenu.clipboard_append(value)

######################################################################################################
        def limekarten(self):
            self.lk_active = True
            self.lk_count = 1
            #
            self.maintainance = ttk.Label(self.display, text="Coming soon...").pack(expand=True)
            #
#            self.lk_spalte1 = ttk.Frame(self.display)
#            self.lk_spalte2 = ttk.Frame(self.display)
#            self.lk_spalte3 = ttk.Frame(self.display)
#            self.lk_spalte4 = ttk.Frame(self.display)

#            self.lk_spalte1.pack(side="left",expand=True)
#            self.lk_spalte2.pack(side="left",expand=True)
#            self.lk_spalte3.pack(side="left",expand=True)
#            self.lk_spalte4.pack(side="left",expand=True)

            # load
#        def newkarte(self):
#            self.lk_select = tk.Toplevel()
#            self.lk_select.geometry("250x100")
#            self.lk_select.resizable(width=False, height=False)
#            self.lk_select.title("Neuer Ordner")
#            center(self.lk_select)
#            self.lk_select_top = ttk.Frame(self.lk_select)
#            self.lk_select_top.pack(padx=9,pady=5,fill="x",expand=True)
#            self.lk_select_l = ttk.Frame(self.lk_select_top)
#            self.lk_select_l.pack(side="left",padx=10)
#            self.lk_select_r = ttk.Frame(self.lk_select_top)
#            self.lk_select_r.pack(side="left",padx=10)
#            self.lk_select_bot = ttk.Frame(self.lk_select)
#            self.lk_select_bot.pack(side="bottom",pady=5)
#            self.lk_selecttext = ttk.Label(self.lk_select_l, text="Name:").pack(side="right")
#            self.lk_selectname = ttk.Entry(self.lk_select_r)
#            self.lk_selectname.pack(side="left")
#            self.lk_selectBtn = ttk.Button(self.lk_select_bot,text="Erstellen",command=lambda: self.createCard()).pack()

#            self.focus = 0
#            self.lk_select.bind("<FocusIn>",self.lk_exit_in)
#            self.lk_select.bind("<FocusOut>",self.lk_exit_out)

        def createCard(self):
            self.lk_newname = str(self.lk_selectname.get())
            if self.lk_count >= 12:
                print("Maximale Ordneranzahl erreicht!")
                return
            if self.lk_newname not in self.empty:
                self.lk_count += 1
                self.lk_Bdict = {2:self.lk_Btn2,3:self.lk_Btn3,4:self.lk_Btn4,5:self.lk_Btn5,
                                 6:self.lk_Btn6,7:self.lk_Btn7,8:self.lk_Btn8,9:self.lk_Btn9,10:self.lk_Btn10,
                                 11:self.lk_Btn11,12:self.lk_Btn12}
                self.lk_Tdict = {2:self.lk_Btn2_t,3:self.lk_Btn3_t,4:self.lk_Btn4_t,5:self.lk_Btn5_t,
                                 6:self.lk_Btn6_t,7:self.lk_Btn7_t,8:self.lk_Btn8_t,9:self.lk_Btn9_t,10:self.lk_Btn10_t,
                                 11:self.lk_Btn11_t,12:self.lk_Btn12_t}
                self.lk_Bdict[self.lk_count].pack()
                self.lk_Tdict[self.lk_count].set(self.lk_newname)
                self.lk_select.destroy()


        def lk_exit_in(self, event):
            self.focus += 1

        def lk_exit_out(self, event):
            self.focus -= 1
            if self.focus == 0:
                self.lk_select.destroy()


################################################################################################

        def lc_start(self):
            if self.lc_loaded:
                return self.lc_screen()

            self.lc_save_cookies = open("assets/cookies.txt", "a")
            self.lc_save_cookies.close()
            self.lc_savecheck = open("assets/cookies.txt", "r")
            self.lc_savedcookies = self.lc_savecheck.read()
            if self.lc_savedcookies in self.empty:
                pickle.dump(self.lc_cookies, open("assets/cookies.txt", "wb"))
            self.lc_cookies = pickle.load(open("assets/cookies.txt", "rb"))

            # Autoclick save

            self.lc_save_autoclick = open("assets/autoclick.txt", "a")
            self.lc_save_autoclick.close()
            self.lc_saveread_autoclick = open("assets/autoclick.txt", "r")
            self.lc_saved_autoclick = self.lc_saveread_autoclick.read()
            if self.lc_saved_autoclick in self.empty:
                pickle.dump(self.lc_ac_count, open("assets/autoclick.txt", "wb"))
            self.lc_saved_ac = pickle.load(open("assets/autoclick.txt", "rb"))

            # multiclick save

            self.lc_save_multiclick = open("assets/multiclick.txt", "a")
            self.lc_save_multiclick.close()
            self.lc_saveread_multiclick = open("assets/multiclick.txt", "r")
            self.lc_saved_multiclick = self.lc_saveread_multiclick.read()
            if self.lc_saved_multiclick in self.empty:
                pickle.dump(self.lc_mc_count, open("assets/multiclick.txt", "wb"))
            self.lc_saved_mc = pickle.load(open("assets/multiclick.txt", "rb"))

            # Autofaktor save

            self.lc_save_autofaktor = open("assets/autofaktor.txt", "a")
            self.lc_save_autofaktor.close()
            self.lc_saveread_autofaktor = open("assets/autofaktor.txt", "r")
            self.lc_saved_autofaktor = self.lc_saveread_autofaktor.read()
            if self.lc_saved_autofaktor in self.empty:
                pickle.dump(self.lc_af_count, open("assets/autofaktor.txt", "wb"))
            self.lc_saved_af = pickle.load(open("assets/autofaktor.txt", "rb"))

            self.lc_screen()

            for i in range(self.lc_saved_mc): self.lc_multiclick_buy(0, self.lc_mc_faktor, 0, 0)
            for i in range(self.lc_saved_af): self.lc_autofaktor_buy(0, self.lc_af_faktor, 0, 0)
            for i in range(self.lc_saved_ac): self.appmenu.after(10, self.lc_autoclick_buy(0, 0, 0))


        def lc_screen(self):
            self.lc_active = True
            if not self.lc_loaded:

                self.lc_autoclicker_anzeige = tk.StringVar(self.appmenu, f"[-10🍋] AutoClick : {self.lc_ac_count}")

                self.lc_autofaktor_anzeige = tk.StringVar(self.appmenu, f"[-100🍋] AutoMulti : {self.lc_autofaktor}")

                self.lc_multiclick_anzeige = tk.StringVar(self.appmenu, f"[-100🍋] MultiClick : {self.lc_multiclick}")

                self.lc_cookiecount = tk.StringVar(self.appmenu, f"{self.lc_cookies}🍋")

                self.lc_loaded = True

            # Frame
            self.lc_app = ttk.Frame(self.display)
            self.lc_top = ttk.Frame(self.lc_app)
            self.lc_main = ttk.Frame(self.lc_app)
            self.lc_left = ttk.Frame(self.lc_main)
            self.lc_right = ttk.Frame(self.lc_main)
            self.lc_F_buttons = ttk.Frame(self.lc_right)

            # Bilder
            self.lc_P_cookie = tk.PhotoImage(file="./assets/cookie.png")

            # Label:

            self.lc_L_cookies = ttk.Label(self.lc_top, textvariable=self.lc_cookiecount,font=self.f_giant).pack(expand=True)

            # Button:
            self.lc_B_click = tk.Button(self.lc_left, image=self.lc_P_cookie, borderwidth=0, activebackground="grey11", command=lambda: self.lc_cookie_clicker())
            self.lc_B_autoclick_buy = ttk.Button(self.lc_F_buttons, textvariable=self.lc_autoclicker_anzeige,
                                        command=lambda: self.lc_autoclick_buy(self.lc_ac_min,self.lc_ac_cost,self.lc_ac_newcost)
                                        ,width=30)
            self.lc_B_autofaktor_buy = ttk.Button(self.lc_F_buttons, textvariable=self.lc_autofaktor_anzeige,
                                         command=lambda: self.lc_autofaktor_buy(self.lc_af_min,self.lc_af_faktor,self.lc_af_cost,
                                                                             self.lc_af_newcost), width=30)
            self.lc_B_multiclick_buy = ttk.Button(self.lc_F_buttons, textvariable=self.lc_multiclick_anzeige,
                                         command=lambda: self.lc_multiclick_buy(self.lc_mc_min,self.lc_mc_faktor,self.lc_mc_cost,
                                                                             self.lc_mc_newcost),width=30)
            self.lc_resetBtn = ttk.Button(self.lc_F_buttons, text="R E S E T", command=self.lc_reset).pack(pady=10)

            self.lc_app.pack(expand=True,fill="both")
            self.lc_top.pack(fill="x",side="top",pady=10)
            self.lc_main.pack(expand=True,fill="both",pady=10)
            self.lc_left.pack(expand=True,side="left")
            self.lc_right.pack(padx=30,side="right")
            self.lc_F_buttons.pack(side="right")
            self.lc_B_click.pack(expand=True)

            self.lc_F_buttons.pack(side="bottom",fill="x")
            self.lc_B_autoclick_buy.pack(pady=5)
            self.lc_B_autofaktor_buy.pack(pady=5)
            self.lc_B_multiclick_buy.pack(pady=5)

            self.lc_setcookies()

        def lc_reset(self):
            f = open("assets/multiclick.txt", "w")
            f.write("")
            f.close()
            f = open("assets/autoclick.txt", "w")
            f.write("")
            f.close()
            f = open("assets/autofaktor.txt", "w")
            f.write("")
            f.close()
            f = open("assets/cookies.txt", "w")
            f.write("")
            f.close()

            self.appmenu.destroy()
            self.lcreset = True
            self.Appmenu()

            self.useBtn("LimeClicker",
                        self.lc_start,
                        self.lcBtn)

        def lc_multiclick_buy(self, min, faktor, cost, newcost):
            if self.lc_cookies > min:
                self.lc_multiclick = faktor
                self.lc_mc_count += 1
                self.lc_cookies -= cost
                self.lc_setcookies()
                self.lc_mc_prices()

        def lc_mc_prices(self):
            self.lc_mc_zaehler += 1

            if self.lc_mc_zaehler > 0:
                if self.lc_mc_zaehler > 9:
                    if self.lc_mc_zaehler == 10:
                        self.lc_mc_faktor *= 1.2
                        self.lc_mc_faktor_temp *= 1.2
                        self.lc_mc_cost += 0
                        self.lc_mc_newcost += 0
                    elif self.lc_mc_zaehler > 19:
                        if self.lc_mc_zaehler == 20:
                            self.lc_mc_faktor *= 1.1
                            self.lc_mc_faktor_temp *= 1.1
                            self.lc_mc_cost += 0
                            self.lc_mc_newcost += 0
                        elif self.lc_mc_zaehler > 29:
                            if self.lc_mc_zaehler == 30:
                                self.lc_mc_faktor *= 1.09
                                self.lc_mc_faktor_temp *= 1.09
                                self.lc_mc_cost += 0
                                self.lc_mc_newcost += 0
                            elif self.lc_mc_zaehler > 49:
                                if self.lc_mc_zaehler == 50:
                                    self.lc_mc_faktor *= 1.06
                                    self.lc_mc_faktor_temp *= 1.06
                                    self.lc_mc_cost += 0
                                    self.lc_mc_newcost += 0
                                elif self.lc_mc_zaehler > 58:
                                    self.lc_mc_faktor *= 1.04
                                    self.lc_mc_faktor_temp *= 1.04
                                    self.lc_mc_cost *= 1.035
                                    self.lc_mc_newcost *= 1.035
                                else:
                                    self.lc_mc_faktor *= 1.06
                                    self.lc_mc_faktor_temp *= 1.06
                                    self.lc_mc_cost += 100000
                                    self.lc_mc_newcost += 100000
                            else:
                                self.lc_mc_faktor *= 1.08
                                self.lc_mc_faktor_temp *= 1.08
                                self.lc_mc_cost += 50000
                                self.lc_mc_newcost += 50000
                        else:
                            self.lc_mc_faktor *= 1.1
                            self.lc_mc_faktor_temp *= 1.1
                            self.lc_mc_cost += 10000
                            self.lc_mc_newcost += 10000
                    else:
                        self.lc_mc_faktor *= 1.2
                        self.lc_mc_faktor_temp *= 1.2
                        self.lc_mc_cost += 1000
                        self.lc_mc_newcost += 1000
                else:
                    self.lc_mc_faktor *= 1.3
                    self.lc_mc_faktor_temp *= 1.3
                    self.lc_mc_cost += 100
                    self.lc_mc_newcost += 100

            self.lc_show_mc_newcost = "{:.0f}".format(self.lc_mc_newcost)
            self.lc_show_mc_faktor = "{:.1f}".format(self.lc_mc_faktor_temp)
            if self.lc_mc_faktor_temp >= 100:
                self.lc_show_mc_faktor = "{:.0f}".format(self.lc_mc_faktor_temp)
            if self.lc_mc_faktor_temp >= 1000:
                self.lc_show_mc_faktor_temp = self.lc_mc_faktor_temp / 1000
                self.lc_show_mc_faktor_temp2 = "{:.2f}".format(self.lc_show_mc_faktor_temp)
                self.lc_show_mc_faktor = f"{(self.lc_show_mc_faktor_temp2)}k"
            if self.lc_mc_faktor_temp >= 10000:
                self.lc_show_mc_faktor_temp = self.lc_mc_faktor_temp / 1000
                self.lc_show_mc_faktor_temp2 = "{:.1f}".format(self.lc_show_mc_faktor_temp)
                self.lc_show_mc_faktor = f"{(self.lc_show_mc_faktor_temp2)}k"
            if self.lc_mc_faktor_temp >= 1000000:
                self.lc_show_mc_faktor_temp = self.lc_mc_faktor_temp / 1000000
                self.lc_show_mc_faktor_temp2 = "{:.2f}".format(self.lc_show_mc_faktor_temp)
                self.lc_show_mc_faktor = f"{(self.lc_show_mc_faktor_temp2)}m"
            if self.lc_mc_newcost >= 1000:
                self.lc_show_mc_newcost_temp = self.lc_mc_newcost / 1000
                self.lc_show_mc_newcost_temp2 = "{:.0f}".format(self.lc_show_mc_newcost_temp)
                self.lc_show_mc_newcost = f"{self.lc_show_mc_newcost_temp}k"
            if self.lc_mc_newcost >= 1000000:
                self.lc_show_mc_newcost_temp = self.lc_mc_newcost / 1000000
                self.lc_show_mc_newcost_temp2 = "{:.1f}".format(self.lc_show_mc_newcost_temp)
                self.lc_show_mc_newcost = f"{self.lc_show_mc_newcost_temp2}m"
            if self.lc_mc_newcost >= 1000000000:
                self.lc_show_mc_newcost_temp = self.lc_mc_newcost / 1000000000
                self.lc_show_mc_newcost_temp2 = "{:.2f}".format(self.lc_show_mc_newcost_temp)
                self.lc_show_mc_newcost = f"{self.lc_show_mc_newcost_temp2}b"
            self.lc_mc_min = self.lc_mc_cost - 1
            self.lc_multiclick_anzeige.set(f"[-{self.lc_show_mc_newcost}🍋] MultiClick : x{self.lc_show_mc_faktor}")
            self.lc_B_multiclick_buy.configure(command=lambda: self.lc_multiclick_buy(self.lc_mc_min, self.lc_mc_faktor,
                                                                                self.lc_mc_cost, self.lc_mc_newcost))


        def lc_autofaktor_buy(self, min, faktor, cost, newcost):
            if self.lc_cookies > min:
                self.lc_autofaktor = faktor
                self.lc_af_count += 1
                self.lc_cookies -= cost
                self.lc_setcookies()
                self.lc_af_prices()

        def lc_af_prices(self):
            self.lc_af_zaehler += 1

            if self.lc_af_zaehler > 0:
                if self.lc_af_zaehler > 9:
                    if self.lc_af_zaehler == 10:
                        self.lc_af_faktor *= 1.5
                        self.lc_af_faktor_temp *= 1.5
                        self.lc_af_cost += 0
                        self.lc_af_newcost += 0
                    elif self.lc_af_zaehler > 19:
                        if self.lc_af_zaehler == 20:
                            self.lc_af_faktor *= 1.3
                            self.lc_af_faktor_temp *= 1.3
                            self.lc_af_cost += 0
                            self.lc_af_newcost += 0
                        elif self.lc_af_zaehler > 29:
                            if self.lc_af_zaehler == 30:
                                self.lc_af_faktor *= 1.1
                                self.lc_af_faktor_temp *= 1.1
                                self.lc_af_cost += 0
                                self.lc_af_newcost += 0
                            elif self.lc_af_zaehler > 39:
                                if self.lc_af_zaehler == 40:
                                    self.lc_af_faktor *= 1.06
                                    self.lc_af_faktor_temp *= 1.06
                                    self.lc_af_cost += 0
                                    self.lc_af_newcost += 0
                                elif self.lc_af_zaehler > 49:
                                    self.lc_af_faktor *= 1.03
                                    self.lc_af_faktor_temp *= 1.03
                                    self.lc_af_cost *= 1.03
                                    self.lc_af_newcost *= 1.03
                                else:
                                    self.lc_af_faktor *= 1.04
                                    self.lc_af_faktor_temp *= 1.04
                                    self.lc_af_cost += 1000000
                                    self.lc_af_newcost += 1000000
                            else:
                                self.lc_af_faktor *= 1.06
                                self.lc_af_faktor_temp *= 1.06
                                self.lc_af_cost += 100000
                                self.lc_af_newcost += 100000
                        else:
                            self.lc_af_faktor *= 1.09
                            self.lc_af_faktor_temp *= 1.09
                            self.lc_af_cost += 10000
                            self.lc_af_newcost += 10000
                    else:
                        self.lc_af_faktor *= 1.1
                        self.lc_af_faktor_temp *= 1.1
                        self.lc_af_cost += 1000
                        self.lc_af_newcost += 1000
                else:
                    self.lc_af_faktor *= 1.3
                    self.lc_af_faktor_temp *= 1.3
                    self.lc_af_cost += 100
                    self.lc_af_newcost += 100

            self.lc_show_af_newcost = "{:.0f}".format(self.lc_af_newcost)
            self.lc_show_af_faktor = "{:.1f}".format(self.lc_af_faktor_temp)
            if self.lc_af_faktor_temp >= 100:
                self.lc_show_af_faktor = "{:.0f}".format(self.lc_af_faktor_temp)
            if self.lc_af_faktor_temp >= 1000:
                self.lc_show_af_faktor_temp = self.lc_af_faktor_temp / 1000
                self.lc_show_af_faktor_temp2 = "{:.2f}".format(self.lc_show_af_faktor_temp)
                self.lc_show_af_faktor = f"{(self.lc_show_af_faktor_temp2)}k"
            if self.lc_af_faktor_temp >= 10000:
                self.lc_show_af_faktor_temp = self.lc_af_faktor_temp / 1000
                self.lc_show_af_faktor_temp2 = "{:.1f}".format(self.lc_show_af_faktor_temp)
                self.lc_show_af_faktor = f"{(self.lc_show_af_faktor_temp2)}k"
            if self.lc_af_faktor_temp >= 1000000:
                self.lc_show_af_faktor_temp = self.lc_af_faktor_temp / 1000000
                self.lc_show_af_faktor_temp2 = "{:.2f}".format(self.lc_show_af_faktor_temp)
                self.lc_show_af_faktor = f"{(self.lc_show_af_faktor_temp2)}m"
            if self.lc_af_newcost >= 1000:
                self.lc_show_af_newcost_temp = self.lc_af_newcost / 1000
                self.lc_show_af_newcost_temp2 = "{:.0f}".format(self.lc_show_af_newcost_temp)
                self.lc_show_af_newcost = f"{self.lc_show_af_newcost_temp}k"
            if self.lc_af_newcost >= 1000000:
                self.lc_show_af_newcost_temp = self.lc_af_newcost / 1000000
                self.lc_show_af_newcost_temp2 = "{:.0f}".format(self.lc_show_af_newcost_temp)
                self.lc_show_af_newcost = f"{self.lc_show_af_newcost_temp}m"
            self.lc_af_min = self.lc_af_cost - 1
            self.lc_autofaktor_anzeige.set(f"[-{self.lc_show_af_newcost}🍋] MultiAuto : x{self.lc_show_af_faktor}")
            self.lc_B_autofaktor_buy.configure(command=lambda: self.lc_autofaktor_buy(self.lc_af_min, self.lc_af_faktor,
                                                                                self.lc_af_cost, self.lc_af_newcost))

        def lc_setcookies(self):
            self.lc_showcookies = "{:.0f}".format(self.lc_cookies)
            self.lc_cookiecount.set(f"{self.lc_showcookies}🍋")
            if self.lc_cookies >= 1000:
                self.lc_cookies_temp = self.lc_cookies / 1000
                self.lc_showcookies = "{:.2f}".format(self.lc_cookies_temp)
                self.lc_cookiecount.set(f"{self.lc_showcookies}k🍋")
            if self.lc_cookies >= 10000:
                self.lc_cookies_temp = self.lc_cookies / 1000
                self.lc_showcookies = "{:.1f}".format(self.lc_cookies_temp)
                self.lc_cookiecount.set(f"{self.lc_showcookies}k🍋")
            if self.lc_cookies >= 1000000:
                self.lc_cookies_temp = self.lc_cookies / 1000000
                self.lc_showcookies = "{:.2f}".format(self.lc_cookies_temp)
                self.lc_cookiecount.set(f"{self.lc_showcookies}m🍋")
            if self.lc_cookies >= 1000000000:
                self.lc_cookies_temp = self.lc_cookies / 1000000000
                self.lc_showcookies = "{:.2f}".format(self.lc_cookies_temp)
                self.lc_cookiecount.set(f"{self.lc_showcookies}b🍋")
            if self.lc_cookies >= 1000000000000:
                self.lc_cookies_temp = self.lc_cookies / 1000000000000
                self.lc_showcookies = "{:.2f}".format(self.lc_cookies_temp)
                self.lc_cookiecount.set(f"{self.lc_showcookies}t🍋")



        def lc_autoClick(self):
            self.lc_cookies += self.lc_autofaktor
            self.lc_setcookies()
            self.display.after(1000, self.lc_autoClick)

        def lc_autoclick_buy(self, min, cost, newcost):
            if self.lc_cookies > min:
                self.lc_cookies -= cost
                self.lc_setcookies()
                self.lc_ac_count += 1
                self.appmenu.after(1, self.lc_autoClick)
                self.lc_ac_prices()

        def lc_ac_prices(self):
            self.lc_ac_zaehler += 1

            if self.lc_ac_zaehler > 0:
                if self.lc_ac_zaehler > 9:
                    if self.lc_ac_zaehler == 10:
                        self.lc_ac_cost += 0
                        self.lc_ac_newcost += 0
                    elif self.lc_ac_zaehler > 19:
                        if self.lc_ac_zaehler == 20:
                            self.lc_ac_cost += 0
                            self.lc_ac_newcost += 0
                        elif self.lc_ac_zaehler > 29:
                            if self.lc_ac_zaehler == 30:
                                self.lc_ac_cost += 0
                                self.lc_ac_newcost += 0
                            elif self.lc_ac_zaehler > 59:
                                if self.lc_ac_zaehler == 40:
                                    self.lc_ac_cost += 0
                                    self.lc_ac_newcost += 0
                                elif self.lc_ac_zaehler > 58:
                                    if self.lc_ac_zaehler == 50:
                                        self.lc_ac_cost += 0
                                        self.lc_ac_newcost += 0
                                    elif self.lc_ac_zaehler > 100:
                                        self.lc_ac_cost += 1000000
                                        self.lc_ac_newcost += 1000000
                                    else:
                                        self.lc_ac_cost += 100000
                                        self.lc_ac_newcost += 100000
                                else:
                                    self.lc_ac_cost += 100000
                                    self.lc_ac_newcost += 100000
                            else:
                                self.lc_ac_cost += 50000
                                self.lc_ac_newcost += 50000
                        else:
                            self.lc_ac_cost += 1000
                            self.lc_ac_newcost += 1000
                    else:
                        self.lc_ac_cost += 100
                        self.lc_ac_newcost += 100
                else:
                    self.lc_ac_cost += 10
                    self.lc_ac_newcost += 10

            self.lc_show_ac_newcost = "{:.0f}".format(self.lc_ac_newcost)
            if self.lc_ac_count >= 1000:
                self.lc_show_ac_count_temp = self.lc_ac_count / 1000
                self.lc_show_ac_count_temp2 = "{:.2f}".format(self.lc_show_ac_count_temp)
                self.lc_show_ac_count = f"{self.lc_show_ac_count_temp2}k"
            if self.lc_ac_newcost >= 1000:
                self.lc_show_ac_newcost_temp = self.lc_ac_newcost // 1000
                self.lc_show_ac_newcost_temp2 = "{:.0f}".format(self.lc_show_ac_newcost_temp)
                self.lc_show_ac_newcost = f"{self.lc_show_ac_newcost_temp}k"
            if self.lc_ac_newcost >= 1000000:
                self.lc_show_ac_newcost_temp = self.lc_ac_newcost / 1000000
                self.lc_show_ac_newcost_temp2 = "{:.1f}".format(self.lc_show_ac_newcost_temp)
                self.lc_show_ac_newcost = f"{self.lc_show_ac_newcost_temp2}m"
            if self.lc_ac_newcost >= 10000000:
                self.lc_show_ac_newcost_temp = self.lc_ac_newcost / 1000000
                self.lc_show_ac_newcost_temp2 = "{:.0f}".format(self.lc_show_ac_newcost_temp)
                self.lc_show_ac_newcost = f"{self.lc_show_ac_newcost_temp}m"
            self.lc_ac_min = self.lc_ac_cost - 1
            self.lc_autoclicker_anzeige.set(f"[-{self.lc_show_ac_newcost}🍋] AutoClick : {self.lc_ac_count}")
            self.lc_B_autoclick_buy.configure(command=lambda: self.lc_autoclick_buy(self.lc_ac_min, self.lc_ac_cost, self.lc_ac_newcost))

        def lc_cookie_clicker(self):
            self.lc_cookies += self.lc_multiclick
            self.lc_setcookies()



######################################################################################################
######################################################################################################
        def register_Btn(self):
            global logged_in
            self.pw1 = self.E_pw.get()
            self.pw2 = self.E_pw2.get()
            self.getname = self.E_name.get()
            self.pw1_length = len(self.pw1)
            self.pw2_length = len(self.pw2)
            self.name_length = len(self.getname)
            if self.name_length > 3 and not self.getname == "mind. 4 Zeichen":
                if self.pw1_length > 5 and not self.pw1 == "mind. 6 Zeichen":
                    if self.pw1 == self.pw2:
                        self.username = self.E_name.get()
                        self.save_name = open("assets/username.txt", "a")
                        pickle.dump(self.username, open("assets/username.txt", "wb"))
                        self.save_name.close()

                        self.password = self.E_pw.get()
                        self.save_pw = open("assets/password.txt", "a")
                        pickle.dump(self.password, open("assets/password.txt", "wb"))
                        self.save_pw.close()

                        logged_in = True
                        self.remembervalue = self.remember_var.get()

                        if self.remembervalue is True:
                            self.rememberedvalue = "1"
                            self.save_rememberer = pickle.dump(self.rememberedvalue, open("assets/login.txt", "wb"))
                        elif not self.remembervalue:
                            self.rememberedvalue = "0"
                            self.save_rememberer = pickle.dump(self.rememberedvalue, open("assets/login.txt", "wb"))

                        self.register.withdraw()
                        self.Root2()
                    elif self.pw2 == "Passwort bestätigen" or self.pw2_length == 0:
                        self.tip_text.set("Passwort bestätigen!")
                        self.L_tip.after(2500, self.tip)
                    else:
                        self.tip_text.set("Passwörter nicht gleich!")
                        self.L_tip.after(2500, self.tip)
                elif self.pw1_length > 0 and self.pw1_length < 6:
                    self.tip_text.set("Passwort zu klein!")
                    self.L_tip.after(2500, self.tip)
                else:
                    self.tip_text.set("Gib ein Passwort ein!")
                    self.L_tip.after(2500, self.tip)
            elif self.name_length < 4 and self.name_length > 0:
                self.tip_text.set("Nutzername zu klein!")
                self.L_tip.after(2500, self.tip)
            else:
                self.tip_text.set("Gib einen Namen ein!")
                self.L_tip.after(2500, self.tip)

        def tip(self):
            self.tip_text.set("")

        def login_Btn(self):
            global logged_in
            self.open_name = open("assets/username.txt", "r")
            self.check_name = pickle.load(open("assets/username.txt", "rb"))
            self.open_pw = open("assets/password.txt", "r")
            self.check_pw = pickle.load(open("assets/password.txt", "rb"))
            self.pw = self.E_pw.get()
            self.getname = self.E_name.get()
            self.getpw = self.E_pw.get()
            if self.getname == self.check_name:
                if self.pw == self.check_pw:
                    logged_in = True # login abfragen zum zurückkehren nach pw()

                    self.remembervalue = self.remember_var.get()

                    if self.remembervalue is True:
                        self.rememberedvalue = "1"
                        self.save_rememberer = pickle.dump(self.rememberedvalue, open("assets/login.txt", "wb"))
                    elif not self.remembervalue:
                        self.rememberedvalue = "0"
                        self.save_rememberer = pickle.dump(self.rememberedvalue, open("assets/login.txt", "wb"))

                    self.login.withdraw()
                    self.Root2()
                elif self.pw in self.empty:
                    self.tip_text.set("Gib dein Passwort ein!")
                    self.L_tip.after(2500, self.tip)
                else:
                    self.tip_text.set("Falsches Passwort!")
                    self.L_tip.after(2500, self.tip)
            elif self.getname in self.empty:
                self.tip_text.set("Gib einen Namen ein!")
                self.L_tip.after(2500, self.tip)
            else:
                self.tip_text.set("Unbekannter Nutzername!")
                self.L_tip.after(2500, self.tip)

        def loop(self):
            self.save_name = open("assets/username.txt", "a")
            self.save_name.close()
            self.namecheck = open("assets/username.txt", "r")
            self.username = self.namecheck.read()

            self.remember_read = "0"
            self.save_remember = open("assets/login.txt", "a")
            self.save_remember.close()
            self.remember_check = open("assets/login.txt", "r")
            if not self.remember_check.read() in self.empty:
                self.remember_read = pickle.load(open("assets/login.txt", "rb"))

            if self.remember_read == "1":
                self.Root1()
            elif self.username in self.empty:
                    self.register()
            else:
                    self.login()


    if __name__ == "__main__":
        Login = Login()

login()
