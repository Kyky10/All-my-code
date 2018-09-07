from random import randint, choice
from tkinter import Canvas, Tk

def thinter_loop():
    size = 500
    window = Tk()
    c = Canvas(window, width = size, height = size)
    c.pack()
    for i in range(3000):
        col = choice(['green2', 'yellow', 'red', 'snow', 'purple1', 'blue', 'cyan', 'deep sky blue'])
        x0 = randint(0, size)
        y0 = randint(0, size)
        d = randint(0, size/5)
        c.create_oval(x0, y0, x0 + d, y0 + d, fill = col)
        window.update()
    window.destroy()
    thinter_loop()
thinter_loop()