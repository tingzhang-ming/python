import Tkinter


def t1():
    top = Tkinter.Tk()
    label = Tkinter.Label(top, text='Hello World')
    label.pack()
    Tkinter.mainloop()


def t2():
    top = Tkinter.Tk()
    quit = Tkinter.Button(top, text='Hello World', command=top.quit)
    quit.pack()
    Tkinter.mainloop()


def t3():
    top = Tkinter.Tk()
    label = Tkinter.Label(top, text='Hello World')
    label.pack()
    quit = Tkinter.Button(top, text='quit', command=top.quit, bg='red', fg='white')
    quit.pack(fill=Tkinter.X, expand=1)
    Tkinter.mainloop()


if __name__ == '__main__':
    t3()
