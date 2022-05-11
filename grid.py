import tkinter as tk

SIZE = 20

root = tk.Tk()

canvas = tk.Canvas(root)
canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

color = 'white'

for y in range(10):
    for x in range(10):
        x1 = x * SIZE
        y1 = y * SIZE
        x2 = x1 + SIZE
        y2 = y1 + SIZE
        canvas.create_rectangle((x1, y1, x2, y2), fill=color)
        if color == 'white':
            color = 'black'
        else:    
            color = 'white'

    if color == 'white':
        color = 'black'
    else:    
        color = 'white'

root.mainloop() 