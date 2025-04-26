import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
import string
import random
import sv_ttk as sv


fB = "Bahnschrift SemiCondensed"


def root():
    class Klasse:
        def __init__(self):
            super().__init__()
            self.root = tk.Tk()
            sv.use_dark_theme()
            self.root.title("Passwort Generator")
            self.root.geometry("550x250")

            self.f_small = tkfont.Font(family=fB, size=13)
            self.f_smol_b = tkfont.Font(family=fB, size=12, weight="bold")
            self.s = ttk.Style()
            self.s.configure("TButton",
                             font=self.f_smol_b)

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

            self.pw_laenge = range(2,
                                   257)

            self.pw_option_var = tk.StringVar(self.root)

            self.pw_create_widgets()

        def pw_create_widgets(self):
            self.pw_F_overall = ttk.Frame(self.root)
            self.pw_F_left = ttk.Frame(self.pw_F_overall)
            self.pw_F_left_top = ttk.Frame(self.pw_F_left)
            self.pw_F_left_bottom = ttk.Frame(self.pw_F_left)
            self.pw_F_left_bottom2 = ttk.Frame(self.pw_F_left)
            self.pw_F_left_bottom3 = ttk.Frame(self.pw_F_left)
            self.pw_F_right = ttk.Frame(self.pw_F_overall)

            self.pw_text_upper = tk.StringVar(self.root,
                                              "ABC: An")
            self.pw_text_lower = tk.StringVar(self.root,
                                              "abc: An")
            self.pw_text_digits = tk.StringVar(self.root,
                                               "123: An")
            self.pw_text_symbols = tk.StringVar(self.root,
                                                "%<&: An")

            self.warn = ttk.Label(self.pw_F_overall, text="Zu hohe Zahl kann zum crash führen!")

            self.pw_Btn_upper = ttk.Button(self.pw_F_left_bottom,
                                           textvariable=self.pw_text_upper,
                                           command=lambda: self.pw_content(0),
                                           width=10)
            self.pw_Btn_lower = ttk.Button(self.pw_F_left_bottom,
                                           textvariable=self.pw_text_lower,
                                           command=lambda: self.pw_content(1),
                                           width=10)
            self.pw_Btn_digits = ttk.Button(self.pw_F_left_bottom2,
                                            textvariable=self.pw_text_digits,
                                            command=lambda: self.pw_content(2),
                                            width=10)
            self.pw_Btn_symbols = ttk.Button(self.pw_F_left_bottom2,
                                             textvariable=self.pw_text_symbols,
                                             command=lambda: self.pw_content(3),
                                             width=10)
            self.pw_Btn_gen = ttk.Button(self.pw_F_left_bottom3,
                                         text="Generieren",
                                         command=lambda: self.pw_generator(int(self.pw_option_var.get())),
                                         width=10)
            self.pw_Btn_copy = ttk.Button(self.pw_F_left_bottom3,
                                          text="Kopieren",
                                          command=lambda: self.pw_copy(),
                                          width=10)

            self.pw_label = ttk.Label(self.pw_F_left_top,
                                      text='Passwortlänge: ',
                                      font=self.f_small)
            self.pw_option_menu = ttk.Combobox(self.pw_F_left_top,
                                               textvariable=self.pw_option_var,
                                               values=(1, *self.pw_laenge))

            self.pw_textbox = tk.Text(self.pw_F_right,
                                      height=10,
                                      width=28,
                                      bg="grey28",
                                      fg="white")
            self.pw_textbox.configure(state=tk.DISABLED)

            self.pw_textbox.pack(side="left")
            self.pw_F_overall.pack(expand=True)
            self.pw_F_left.pack(side="left",
                                padx=7,
                                pady=7)
            self.pw_F_left_top.pack(side="top",
                                    expand=True, )
            self.pw_F_left_bottom.pack(expand=True,
                                       fill="both")
            self.pw_F_left_bottom2.pack(expand=True,
                                        fill="both")
            self.pw_F_left_bottom3.pack(side="bottom",
                                        expand=True,
                                        fill="both")
            self.pw_F_right.pack(side="right",
                                 padx=7,
                                 pady=7)

            self.pw_label.pack(side="left",
                               padx=5,
                               pady=5)

            self.pw_option_menu.pack(side="right",
                                     padx=5,
                                     pady=5)

            self.pw_Btn_upper.pack(side="left",
                                   expand=True,
                                   fill="both",
                                   padx=3,
                                   pady=3)
            self.pw_Btn_lower.pack(side="left",
                                   expand=True,
                                   fill="both",
                                   padx=3,
                                   pady=3)
            self.pw_Btn_digits.pack(side="left",
                                    expand=True,
                                    fill="both",
                                    padx=3,
                                    pady=3)
            self.pw_Btn_symbols.pack(side="left",
                                     expand=True,
                                     fill="both",
                                     padx=3,
                                     pady=3)
            self.pw_Btn_gen.pack(side="left",
                                 expand=True,
                                 fill="both",
                                 padx=3,
                                 pady=3)
            self.pw_Btn_copy.pack(side="left",
                                  expand=True,
                                  fill="both",
                                  padx=3,
                                  pady=3)

            self.root.mainloop()

        def pw_generator(self, pw_length):
            if pw_length < 257:
                self.pw_pwtemp = random.choices((self.pw_upper + self.pw_lower + self.pw_digits + self.pw_symbols),
                                                weights=None,
                                                cum_weights=None,
                                                k=pw_length)
                self.pw_passwort = "".join(self.pw_pwtemp)
                self.pw_textbox.configure(state=tk.NORMAL)
                self.pw_textbox.delete(1.0,
                                       'end')
                self.pw_textbox.insert('end',
                                       self.pw_passwort)
                self.pw_textbox.configure(state=tk.DISABLED)

        def pw_content(self, pw_choice):
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
            self.root.clipboard_clear()
            self.root.clipboard_append(value)

    if __name__ == "__main__":
        Klasse = Klasse()

root()