import tkinter as tk
import customtkinter as ctk
import pandas as pd
from tkextrafont import Font

root = tk.Tk()

# title
root.title("Pocket Calculator")

# dimension
width, height = 270, 515
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
# root.geometry("270x515")
root.geometry(f"{width}x{height}+{x}+{y}")

# icon
icon = tk.PhotoImage(file="PocketCalculatorIcon.png")
root.iconphoto(True, icon)

# disable fullscreen & maximize
root.attributes("-fullscreen", False)
root.resizable(False, False)

# background
root.config(background="#c78a19")

# fonts
bitcount_single = Font(file="BitcountSingle-Regular.ttf", family="Bitcount Single", size=15, weight="bold")
tektur = Font(file="Tektur-Regular.ttf", family="Tektur", size=15, weight="bold")

# dynamic grids
total_row = 5
for i in range(2, total_row + 2):
    root.rowconfigure(i, weight=1, uniform="buttons")
total_col = 4
for i in range(total_col):
    root.columnconfigure(i, weight=1, uniform="buttons")

# OOP
class Calculator:
    def __init__(self):
        self.input_str = ""
        self.output_str = ""
        self.previous_output = ""

    def press_key(self, key):
        # max space of 17 characters
        if (len(self.input_str) <= 16):
            self.input_str += key
            self.output_str = ""
            update_displays(self.input_str, self.output_str)

    def clear(self):
        self.input_str = ""
        self.output_str = ""
        update_displays(self.input_str, self.output_str)

    def delete(self):
        if self.output_str == "":
            original_str = self.input_str
            self.input_str = original_str[:-1]
            update_displays(self.input_str, self.output_str)

    def calculate(self, input_str):
        try: 
            calculated_num = pd.eval(input_str)
            # if-else to round non-decimal (10.0)
            if calculated_num % 1 == 0:
                self.output_str = int(calculated_num)
                self.previous_output = str(int(calculated_num))
            else:
                self.output_str = calculated_num      
                self.previous_output = str(calculated_num)
        except SyntaxError as e:
            self.output_str = "Invalid Expression"
        except ZeroDivisionError:
            self.output_str = "Cannot divide by 0"
        update_output(self.output_str)

calc = Calculator()

def update_displays(input_str, output_str):
    input_display.config(text=input_str)
    output_display.config(text=output_str)

def update_output(output_str):
    output_display.config(text=output_str)
    calc.input_str = "" # reset input_display, but don't update it yet
     

# screen display
input_display = tk.Label(root, height=2, text="", font=bitcount_single, anchor="w", padx=10, fg="#000000", bg="#79887D")
input_display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=(15, 0))
output_display = tk.Label(root, height=2, text="", font=tektur, anchor="e", padx=10, fg="#000000", bg="#79887D")
output_display.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=(0, 8))

# calculator buttons
# row 2
answer_btn = ctk.CTkButton(root, text="ANS", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#b15c0d", text_color="#ffffff", hover_color="#a35206", command=lambda: calc.press_key(calc.previous_output))
answer_btn.grid(row=2, column=0, sticky="nsew", padx=5, pady=8)

clear_btn = ctk.CTkButton(root, text="C", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#b15c0d", text_color="#ffffff", hover_color="#a35206", command=calc.clear)
clear_btn.grid(row=2, column=1, sticky="nsew", padx=5, pady=8)

delete_btn = ctk.CTkButton(root, text="DEL", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#b15c0d", text_color="#ffffff", hover_color="#a35206", command=calc.delete)
delete_btn.grid(row=2, column=2, sticky="nsew", padx=5, pady=8)

divide_btn = ctk.CTkButton(root, text="÷", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#aaaaaa", text_color="#ffffff", hover_color="#888888", command=lambda: calc.press_key("/"))
divide_btn.grid(row=2, column=3, sticky="nsew", padx=5, pady=8)

# row 3
seven_btn = ctk.CTkButton(root, text="7", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#ffffff", text_color="#000000", hover_color="#dddddd", command=lambda: calc.press_key("7"))
seven_btn.grid(row=3, column=0, sticky="nsew", padx=5, pady=8)

eight_btn = ctk.CTkButton(root, text="8", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#ffffff", text_color="#000000", hover_color="#dddddd", command=lambda: calc.press_key("8"))
eight_btn.grid(row=3, column=1, sticky="nsew", padx=5, pady=8)

nine_btn = ctk.CTkButton(root, text="9", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#ffffff", text_color="#000000", hover_color="#dddddd", command=lambda: calc.press_key("9"))
nine_btn.grid(row=3, column=2, sticky="nsew", padx=5, pady=8)

multiply_btn = ctk.CTkButton(root, text="x", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#aaaaaa", text_color="#ffffff", hover_color="#888888", command=lambda: calc.press_key("*"))
multiply_btn.grid(row=3, column=3, sticky="nsew", padx=5, pady=8)

# row 4
four_btn = ctk.CTkButton(root, text="4", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#ffffff", text_color="#000000", hover_color="#dddddd", command=lambda: calc.press_key("4"))
four_btn.grid(row=4, column=0, sticky="nsew", padx=5, pady=8)

five_btn = ctk.CTkButton(root, text="5", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#ffffff", text_color="#000000", hover_color="#dddddd", command=lambda: calc.press_key("5"))
five_btn.grid(row=4, column=1, sticky="nsew", padx=5, pady=8)

six_btn = ctk.CTkButton(root, text="6", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#ffffff", text_color="#000000", hover_color="#dddddd", command=lambda: calc.press_key("6"))
six_btn.grid(row=4, column=2, sticky="nsew", padx=5, pady=8)

minus_btn = ctk.CTkButton(root, text="–", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#aaaaaa", text_color="#ffffff", hover_color="#888888", command=lambda: calc.press_key("-"))
minus_btn.grid(row=4, column=3, sticky="nsew", padx=5, pady=8)

# row 5
one_btn = ctk.CTkButton(root, text="1", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#ffffff", text_color="#000000", hover_color="#dddddd", command=lambda: calc.press_key("1"))
one_btn.grid(row=5, column=0, sticky="nsew", padx=5, pady=8)

two_btn = ctk.CTkButton(root, text="2", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#ffffff", text_color="#000000", hover_color="#dddddd", command=lambda: calc.press_key("2"))
two_btn.grid(row=5, column=1, sticky="nsew", padx=5, pady=8)

three_btn = ctk.CTkButton(root, text="3", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#ffffff", text_color="#000000", hover_color="#dddddd", command=lambda: calc.press_key("3"))
three_btn.grid(row=5, column=2, sticky="nsew", padx=5, pady=8)

add_btn = ctk.CTkButton(root, text="+", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#aaaaaa", text_color="#ffffff", hover_color="#888888", command=lambda: calc.press_key("+"))
add_btn.grid(row=5, column=3, sticky="nsew", padx=5, pady=8)

# row 6
dot_btn = ctk.CTkButton(root, text="•", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#ffffff", text_color="#000000", hover_color="#dddddd", command=lambda: calc.press_key("."))
dot_btn.grid(row=6, column=0, sticky="nsew", padx=5, pady=8)

zero_btn = ctk.CTkButton(root, text="0", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#ffffff", text_color="#000000", hover_color="#dddddd", command=lambda: calc.press_key("0"))
zero_btn.grid(row=6, column=1, sticky="nsew", padx=5, pady=8)

negative_btn = ctk.CTkButton(root, text="(-)", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#ffffff", text_color="#000000", hover_color="#dddddd", command=lambda: calc.press_key("-"))
negative_btn.grid(row=6, column=2, sticky="nsew", padx=5, pady=8)

enter_btn = ctk.CTkButton(root, text="=", font=("Roboto", 20, "bold"), corner_radius=5, fg_color="#aaaaaa", text_color="#ffffff", hover_color="#888888", command=lambda: calc.calculate(input_display.cget("text")))
enter_btn.grid(row=6, column=3, sticky="nsew", padx=5, pady=8)

root.mainloop()
