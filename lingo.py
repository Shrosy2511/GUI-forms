import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

lstAnswer = []
lstLetters = []
num = 0

def checkAntwoord():
    global num, lstLetters
    for index in range(len(letters)):
        if letters[index] == lstAnswer[index].get():
            num +=  len(letters)
            lstLetters.append(letters[index])
            if lstLetters == letters:
                messagebox.showinfo("Gewonnen", "je punten zijn" + str(num))
        else:
            lstLetters = []
            messagebox.showinfo("Fout", "je punten zijn" + str(num))
            num -= 2
            print('fout')
            

def checkLetters(event=None):
    global lstAnswer,letters

    letters = list(entry.get())
    if len(letters) >= 4 and len(letters) <= 7:
        window.destroy()
        windowAnswer = tk.Tk()
        windowAnswer.title("Answer")
        windowAnswer.geometry("400x400")    

        lstAlpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        rel = 0.15
        for i in range(len(letters)):
            for index,value in enumerate(lstAlpha):
                if letters[i] == value:
                    lstAlpha.pop(index)
                    print(value, index)
            lst = [random.choice(lstAlpha) for x in range(4)]
            lst.append(entryvar.get()[i])
            random.shuffle(lst)
            box = ttk.Combobox(windowAnswer, values=[y for y in lst], state='readonly')
            box.place(relx=rel, rely=0.3, anchor=CENTER, width=35)
            lstAnswer.append(box)
            rel += 0.17
        
        antwoordKnop = tk.Button(windowAnswer, text="doe een gok",command= checkAntwoord)
        antwoordKnop.place(relx=0.5, rely=0.5, anchor=CENTER)

        afsluitKnop = tk.Button(windowAnswer, text="Quit", command= windowAnswer.destroy)
        afsluitKnop.place(relx=0.5, rely=0.7, anchor=CENTER)

        windowAnswer.mainloop()
    else:
        print('sorry je heb niet het juiste aantal letters ingevuld')

window = tk.Tk()
window.title("Lingo")
window.geometry("400x400")

label = tk.Label(text="vul een woord in", font=("Helvetica", 20))
label.pack()

entryvar = tk.StringVar()
entry = tk.Entry(window, width=20, font=("Helvetica", 20), textvariable= entryvar)
entry.pack()

label1 = tk.Label(text="tussen de 4 en 7 letters", font=("Helvetica", 10))
label1.pack()

button = tk.Button(text="start", font=("Helvetica", 10), width=20, height=2, command=lambda: checkLetters(entry.get()))
button.pack()

window.mainloop()



