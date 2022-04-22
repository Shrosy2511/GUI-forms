import tkinter as tk

num = 0
divide = False
autoclickerState = ""

def plus(event=None):
    global num, divide, autoclickerState
    autoclickerState = "plus"
    num += 1
    divide = True
    checkbox.config(state="active")
    color()

def minus(event=None):
    global num, divide, autoclickerState
    autoclickerState = "minus"
    num -= 1
    divide = False
    checkbox.config(state="active")
    color()

def color(event=None):
    global num
    label.config(text=f"{num:.0f}")
    if num == 0:
        window.config(bg="grey")
    elif num > 0:
        window.config(bg="green")
    else:
        window.config(bg="red")

def ColorChange(event=None):
    window.config(bg="yellow")

def divideBy3(event=None):
    global num, divide, autoclickerState
    if divide == True:
        autoclickerState = "times"
        num = num * 3
    elif divide == False:
        autoclickerState = "divide"
        num = num / 3
    label.config(text=f"{num:.0f}")
    checkbox.config(state="active")
    color()
# if plus is active autloclick is active
def autoclick(event=None):
    global BoolCheckbox, num, divide, autoclickerState
    print(BoolCheckbox.get())
    if autoclickerState == "plus":
        if BoolCheckbox.get() == True:
            num += 1
    elif autoclickerState == "times":
        if BoolCheckbox.get() == True:
            num = num * 3
    elif autoclickerState == "minus":
        if BoolCheckbox.get() == True:
            num -= 1
    elif autoclickerState == "divide":
        if BoolCheckbox.get() == True:
            num = num / 3
    elif BoolCheckbox.get() == False:
        window.after_cancel(autoclick)
    label.config(text=f"{num:.0f}")
    window.after(200, autoclick)


window = tk.Tk()
window.geometry("300x300")

BoolCheckbox = tk.BooleanVar()

checkbox = tk.Checkbutton(window, text="autoclick", command=autoclick, variable=BoolCheckbox)
checkbox.config(state="disabled")
checkbox.place(x=0, y=0)

label = tk.Label(text=f"{num}", bg="black", fg="white", font=("danger", 30))
label.place(relx=0.5, rely=0.5, anchor="center")

button = tk.Button(text="click here for +", bg="black", fg="white", width=20, height=5)
button.config(command=plus)
button.pack(side=tk.TOP)

button1 = tk.Button(text="click here for -", bg="black", fg="white", width=20, height=5)
button1.config(command=minus)
button1.pack(side=tk.BOTTOM)

label.bind("<Enter>", ColorChange)
label.bind("<Leave>", color)
label.bind("<Double-Button-1>", divideBy3)

window.bind("=", plus)
window.bind("-", minus)
window.bind("<space>", divideBy3)

window.mainloop()