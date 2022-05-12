import tkinter as tk
from tkinter import *
from tkinter import ttk

def checkLetters(event=None):
    letters = list(entry.get())
    if len(letters) >= 4 and len(letters) <= 7:
        window.destroy()
        windowAnswer = tk.Tk()
        windowAnswer.title("Answer")
        windowAnswer.geometry("400x400")

        box = ttk.Combobox()
        box.place(relx=0.01, rely=0.05, anchor=W)

        windowAnswer.mainloop()
    else:
        print('sorry je heb niet het juiste aantal letters ingevuld')

window = tk.Tk()
window.title("Lingo")
window.geometry("400x400")

label = tk.Label(text="vul een woord in", font=("Helvetica", 20))
label.pack()

entryvar = StringVar()
entry = tk.Entry(window, width=20, font=("Helvetica", 20), textvariable= entryvar)
entry.pack()

label1 = tk.Label(text="tussen de 4 en 7 letters", font=("Helvetica", 10))
label1.pack()

button = tk.Button(text="start", font=("Helvetica", 10), width=20, height=2, command=lambda: checkLetters(entry.get()))
button.pack()

window.mainloop()

