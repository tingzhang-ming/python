from Tkinter import *


def t1():
    def resize(ev=None):
        label.config(font='Helvetica -%d bold' % scale.get())
    top = Tk()
    top.geometry('250x250')
    label = Label(top, text='Hello World', font='Helvetica -12 bold')
    label.pack()

    scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
    scale.set(12)
    scale.pack(fill=X, expand=1)

    quit = Button(top, text='quit', command=top.quit, activebackground='red', activeforeground='white')
    quit.pack()
    mainloop()


if __name__ == '__main__':
    t1()
