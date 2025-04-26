import tkinter as tk
import tkinter.font as tkfont
import pickle

# Internet modules

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
# Variablen
fB = "Bahnschrift SemiCondensed"
cookies = 0

ac_min = 9
ac_cost = 10
ac_newcost = -10
ac_zaehler = 0
ac_count = 0

af_min = 99
af_faktor = 1.2
af_faktor_temp = 1
af_cost = 100
af_newcost = -100
af_zaehler = 0
af_count = 0

mc_min = 99
mc_faktor = 1.2
mc_faktor_temp = 1
mc_cost = 100
mc_newcost = -100
mc_zaehler = 0
mc_count = 0

prestigefaktor = 1
prestige1_enabled = False
prestige2_enabled = False
prestige3_enabled = False
prestige4_enabled = False

autofaktor = 1 * prestigefaktor

multiclick = 1 * prestigefaktor

empty = {""}
########################
# Save
save_cookies = open("assets/cookies.txt", "a")
save_cookies.close()
savecheck = open("assets/cookies.txt", "r")
savedcookies = savecheck.read()
if savedcookies in empty:
    pickle.dump(cookies, open("assets/cookies.txt", "wb"))
cookies = pickle.load(open("assets/cookies.txt", "rb"))

# Autoclick save

save_autoclick = open("assets/autoclick.txt", "a")
save_autoclick.close()
saveread_autoclick = open("assets/autoclick.txt", "r")
saved_autoclick = saveread_autoclick.read()
if saved_autoclick in empty:
    pickle.dump(ac_count, open("assets/autoclick.txt", "wb"))
saved_ac = pickle.load(open("assets/autoclick.txt", "rb"))

# multiclick save

save_multiclick = open("assets/multiclick.txt", "a")
save_multiclick.close()
saveread_multiclick = open("assets/multiclick.txt", "r")
saved_multiclick = saveread_multiclick.read()
if saved_multiclick in empty:
    pickle.dump(mc_count, open("assets/multiclick.txt", "wb"))
saved_mc = pickle.load(open("assets/multiclick.txt", "rb"))

# Autofaktor save

save_autofaktor = open("assets/autofaktor.txt", "a")
save_autofaktor.close()
saveread_autofaktor = open("assets/autofaktor.txt", "r")
saved_autofaktor = saveread_autofaktor.read()
if saved_autofaktor in empty:
    pickle.dump(af_count, open("assets/autofaktor.txt", "wb"))
saved_af = pickle.load(open("assets/autofaktor.txt", "rb"))

########################
# CookieClicker
CookieClicker = tk.Tk()
CookieClicker.title("LimeClicker v1.2")
CookieClicker.configure(bg="grey28",width="50",height="25")
CookieClicker.geometry("400x400")
CookieClicker.resizable(width=False,height=False)
center(CookieClicker)

# Custom Fonts:
f_smol = tkfont.Font(family=fB,size=11)
f_smol_b = tkfont.Font(family=fB,size=11,weight="bold")
f_small = tkfont.Font(family=fB,size=13)
f_small_b = tkfont.Font(family=fB,size=13,weight="bold")
f_medium = tkfont.Font(family=fB,size=16)
f_medium_b = tkfont.Font(family=fB,size=16,weight="bold")
f_big = tkfont.Font(family=fB,size=20)
f_big_b = tkfont.Font(family=fB,size=20,weight="bold")
f_giant = tkfont.Font(family=fB,size=30, weight="bold")
########################################################################################
# COOKIE CLICKER
########################################################################################

autoclicker_anzeige = tk.StringVar(CookieClicker, f"[-10🍋] AutoClick : {ac_count}")


autofaktor_anzeige = tk.StringVar(CookieClicker, f"[-100🍋] MultiAuto : {autofaktor}")

multiclick_anzeige = tk.StringVar(CookieClicker, f"[-100🍋] MultiClick : {multiclick}")

# Frame
F_cookies = tk.Frame(bg="grey28")
F_buttons = tk.Frame(bg="grey28")
F_achievements = tk.Frame(bg="grey28")

# Bilder
P_cookie = tk.PhotoImage(file="./assets/cookie.png")

# Label:
prestigecount = 0
cookiecount = tk.StringVar(CookieClicker, f"{cookies}🍋")
Event1 = 0
Event2 = ""
Eventtext1 = tk.StringVar(CookieClicker, "")
Eventtext2 = tk.StringVar(CookieClicker, "")

L_cookies = tk.Label(F_cookies, textvariable=cookiecount,bg="grey28",
                     fg="white",font=f_giant).pack(expand=True,side="left")
L_Event_1 = tk.Label(F_achievements, textvariable=Eventtext1,bg="grey28",fg="white",font=f_smol)
L_Event_2 = tk.Label(F_achievements, textvariable=Eventtext2,bg="grey28",fg="white",font=f_smol)

# Button:
B_click = tk.Button(CookieClicker, image=P_cookie,bg="grey28",fg="white",font=f_small,borderwidth=0,
                    activebackground="grey28",activeforeground="white",command=lambda: cookie_clicker())
B_menu = tk.Button(CookieClicker, text="Menu",command=lambda: menu_open(),
                            bg="grey28",fg="white",activeforeground="grey75",activebackground="grey24",
                            disabledforeground="white",width=13,height=1,font=f_small)
B_autoclick_buy = tk.Button(F_buttons, textvariable=autoclicker_anzeige,command=lambda: autoclick_buy(ac_min,ac_cost,ac_newcost),
                            bg="grey28",fg="white",activeforeground="grey75",activebackground="grey24",
                            disabledforeground="white",width=25,height=1,font=f_small)
B_autofaktor_buy = tk.Button(F_buttons, textvariable=autofaktor_anzeige,command=lambda: autofaktor_buy(af_min,af_faktor,af_cost,af_newcost),
                             bg="grey28",fg="white",activeforeground="grey75",activebackground="grey24",
                             disabledforeground="white",width=25,height=1,font=f_small)
B_multiclick_buy = tk.Button(F_buttons, textvariable=multiclick_anzeige,command=lambda: multiclick_buy(mc_min,mc_faktor,mc_cost,mc_newcost),
                              bg="grey28",fg="white",activeforeground="grey75",activebackground="grey24",
                              disabledforeground="white",width=25,height=1,font=f_small)
########################################################################################
# Programme:
def exitreturn():
    global cookies
    pickle.dump(round(cookies), open("assets/cookies.txt", "wb"))
    pickle.dump(ac_count, open("assets/autoclick.txt", "wb"))
    pickle.dump(af_count, open("assets/autofaktor.txt", "wb"))
    pickle.dump(mc_count, open("assets/multiclick.txt", "wb"))
    CookieClicker.destroy()


def menu_open():
    B_click.pack_forget()
    F_buttons.pack(side="bottom")
    B_autoclick_buy.pack()  # F_buttons
    B_autofaktor_buy.pack()  # F_buttons
    B_multiclick_buy.pack()  # F_buttons
    B_menu.configure(text="Zurück <-",command=lambda: menu_exit())
    F_achievements.pack(side="bottom")
    L_Event_1.pack(side="right")  # F_achievements
    L_Event_2.pack(side="bottom")  # F_achievements


def menu_exit():
    B_click.pack(expand=True)  # CookieClicker
    F_buttons.pack_forget()
    B_menu.configure(text="Menu", command=lambda: menu_open())


def multiclick_buy(min,faktor,cost,newcost):
    global cookies
    global multiclick
    global mc_count
    if cookies > min:
        multiclick = faktor * prestigefaktor
        mc_count += 1
        cookies -= cost
        cookiecount.set(f"""{"{:.1f}".format(cookies)}🍋""")
        multiclick_anzeige.set(f"[{newcost}🍋] MultiClick : {round(mc_faktor, 2)}x")
        mc_prices()

def mc_prices():
    global cookies
    global mc_min
    global mc_faktor
    global mc_faktor_temp
    global mc_cost
    global mc_newcost
    global mc_zaehler
    mc_zaehler += 1

    if mc_zaehler > 0:
        if mc_zaehler > 9:
            if mc_zaehler == 10:
                mc_faktor *= 1.2
                mc_faktor_temp *= 1.2
                mc_cost += 0
                mc_newcost += 0
            elif mc_zaehler > 19:
                if mc_zaehler == 20:
                    mc_faktor *= 1.1
                    mc_faktor_temp *= 1.1
                    mc_cost += 0
                    mc_newcost += 0
                elif mc_zaehler > 29:
                    if mc_zaehler == 30:
                        mc_faktor *= 1.08
                        mc_faktor_temp *= 1.08
                        mc_cost += 0
                        mc_newcost += 0
                    elif mc_zaehler > 39:
                        if mc_zaehler == 40:
                            mc_faktor *= 1.05
                            mc_faktor_temp *= 1.05
                            mc_cost += 0
                            mc_newcost += 0
                        elif mc_zaehler > 49:
                            mc_faktor *= 1.03
                            mc_faktor_temp *= 1.03
                            mc_cost += 1000000
                            mc_newcost -= 1000000
                    else:
                        mc_faktor *= 1.05
                        mc_faktor_temp *= 1.05
                        mc_cost += 100000
                        mc_newcost -= 100000
                else:
                    mc_faktor *= 1.08
                    mc_faktor_temp *= 1.08
                    mc_cost += 10000
                    mc_newcost -= 10000
            else:
                mc_faktor *= 1.1
                mc_faktor_temp *= 1.1
                mc_cost += 1000
                mc_newcost -= 1000
        else:
            mc_faktor *= 1.2
            mc_faktor_temp *= 1.2
            mc_cost += 100
            mc_newcost -= 100

    show_mc_faktor = "{:.1f}".format(mc_faktor_temp)
    mc_min = mc_cost - 1
    multiclick_anzeige.set(f"[{mc_newcost}🍋] MultiClick : {show_mc_faktor}x")
    B_multiclick_buy.configure(command= lambda: multiclick_buy(mc_min, mc_faktor, mc_cost, mc_newcost))

for i in range(saved_mc): multiclick_buy(0, mc_faktor, 0, 0)


def autofaktor_buy(min,faktor,cost,newcost):
    global cookies
    global autofaktor
    global  af_count
    if cookies > min:
        autofaktor = faktor * prestigefaktor
        af_count += 1
        cookies = cookies - cost
        cookiecount.set(f"""{"{:.1f}".format(cookies)}🍋""")
        autofaktor_anzeige.set(f"[{newcost}🍋] MultiAuto : {round(af_faktor, 2)}x")
        af_prices()

def af_prices():
    global cookies
    global af_min
    global af_faktor
    global af_faktor_temp
    global af_cost
    global af_newcost
    global af_zaehler
    af_zaehler += 1

    if af_zaehler > 0:
        if af_zaehler > 9:
            if af_zaehler == 10:
                af_faktor *= 1.2
                af_faktor_temp *= 1.2
                af_cost += 0
                af_newcost += 0
            elif af_zaehler > 19:
                if af_zaehler == 20:
                    af_faktor *= 1.1
                    af_faktor_temp *= 1.1
                    af_cost += 0
                    af_newcost += 0
                elif af_zaehler > 29:
                    if af_zaehler == 30:
                        af_faktor *= 1.08
                        af_faktor_temp *= 1.08
                        af_cost += 0
                        af_newcost += 0
                    elif af_zaehler > 39:
                        if af_zaehler == 40:
                            af_faktor *= 1.05
                            af_faktor_temp *= 1.05
                            af_cost += 0
                            af_newcost += 0
                        elif af_zaehler > 49:
                            af_faktor *= 1.03
                            af_faktor_temp *= 1.03
                            af_cost += 1000000
                            af_newcost -= 1000000
                    else:
                        af_faktor *= 1.05
                        af_faktor_temp *= 1.05
                        af_cost += 100000
                        af_newcost -= 100000
                else:
                    af_faktor *= 1.08
                    af_faktor_temp *= 1.08
                    af_cost += 10000
                    af_newcost -= 10000
            else:
                af_faktor *= 1.1
                af_faktor_temp *= 1.1
                af_cost += 1000
                af_newcost -= 1000
        else:
            af_faktor *= 1.2
            af_faktor_temp *= 1.2
            af_cost += 100
            af_newcost -= 100

    show_af_faktor = "{:.1f}".format(af_faktor_temp)
    af_min = af_cost - 1
    autofaktor_anzeige.set(f"[{af_newcost}🍋] MultiAuto : {show_af_faktor}x")
    B_autofaktor_buy.configure(command= lambda: autofaktor_buy(af_min, af_faktor, af_cost, af_newcost))

for i in range(saved_af): autofaktor_buy(0, af_faktor, 0, 0)


def autoClick():
    global cookies
    global ac_count
    cookies += autofaktor
    showcookies = "{:.1f}".format(cookies)
    cookiecount.set(f"{showcookies}🍋")
    CookieClicker.after(1000, autoClick)
    eventcheck()


def autoclick_buy(min,cost,newcost):
    global cookies
    global ac_count
    if cookies > min:
        cookies -= cost
        showcookies = "{:.1f}".format(cookies)
        cookiecount.set(f"{showcookies}🍋")
        ac_count += 1
        autoclicker_anzeige.set(f"[{newcost}🍋] AutoClick : {ac_count}")
        CookieClicker.after(1000, autoClick)
        ac_prices()

def ac_prices():
    global cookies
    global ac_min
    global ac_cost
    global ac_newcost
    global ac_zaehler
    ac_zaehler += 1

    if ac_zaehler > 0:
        if ac_zaehler > 9:
            if ac_zaehler == 10:
                ac_cost += 0
                ac_newcost += 0
            elif ac_zaehler > 19:
                if ac_zaehler == 20:
                    ac_cost += 0
                    ac_newcost += 0
                elif ac_zaehler > 29:
                    if ac_zaehler == 30:
                        ac_cost += 0
                        ac_newcost += 0
                    elif ac_zaehler > 39:
                        if ac_zaehler == 40:
                            ac_cost += 0
                            ac_newcost += 0
                        if ac_zaehler > 49:
                            ac_cost += 100000
                            ac_newcost -= 100000
                    else:
                        ac_cost += 10000
                        ac_newcost -= 10000
                else:
                    ac_cost += 1000
                    ac_newcost -= 1000
            else:
                ac_cost += 100
                ac_newcost -= 100
        else:
            ac_cost += 10
            ac_newcost -= 10

    ac_min = ac_cost - 1
    autoclicker_anzeige.set(f"[{ac_newcost}🍋] AutoClick : {ac_count}")
    B_autoclick_buy.configure(command=lambda: autoclick_buy(ac_min,ac_cost,ac_newcost))

for i in range(saved_ac): CookieClicker.after(100, autoclick_buy(0, 0, 0))


def cookie_clicker():
    global cookies
    cookies += multiclick
    showcookies = "{:.1f}".format(cookies)
    cookiecount.set(f"{showcookies}🍋")
    eventcheck()

milestone1 = False
milestone2 = False

def eventcheck():
    global Event1
    global Event2
    global event1_check
    global milestone1
    global milestone2
    if not milestone1:
        if cookies <= 500:
            Event1 = 500
            Eventtext1.set(f"{Event1} Meilenstein!")
            milestone1 = True
        else:
            return
    if not milestone2:
        if cookies <= 1000:
            Event1 = 1000
            Eventtext1.set(f"{Event1} Meilenstein!")
            milestone2 = True
        else:
            return
    if prestigecount == 1:
        Eventtext2.set(f"{prestigecount} Prestige!")
    else:
        return

########################################################################################
#grid/pack Manager:
B_menu.pack()
F_buttons.pack(side="top")
F_cookies.pack(expand=True)
B_click.pack(expand=True) # CookieClicker
# Trigger Events:
CookieClicker.protocol("WM_DELETE_WINDOW", lambda: exitreturn())
########################################################################################
CookieClicker.mainloop()