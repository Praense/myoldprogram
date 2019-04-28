from tkinter import *
def guilist():
    global text, root
    rootlist = Tk()
    text = Text(width=50, height=30)
    text.pack()
    with open('files/.urllofi', 'r') as _templofiurl:
        text.insert("1.0", _templofiurl.read())
    rootlist.protocol("WM_DELETE_WINDOW", ON_close)
    rootlist.mainloop()
def ON_close():
    with open('files/.urllofi', 'w') as _templofiwr:
        _templofiwr.write(text.get('0.1', END))
    rootlist.destroy()
