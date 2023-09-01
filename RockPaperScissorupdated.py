import tkinter
from tkinter import *
import random

myroot = Tk()
myroot.geometry('350x350')
myroot.maxsize(350, 350)
myroot.minsize(350, 350)
myroot.title('RockPaperScissor')

myframe = Frame(myroot, height=350, width=350, bg='#98F5FF')
myframe.pack()

lbl = Label(myframe, height=1, width=17, text='Make Your Choice')
lbl.place(x=110, y=40)

btn1 = Button(myframe, height=3, width=8, bg='#00CDCD', text='ROCK', command=lambda: onclick('0'))
btn1.place(x=40, y=90)

btn2 = Button(myframe, height=3, width=8, bg='#DC143C', text='PAPER', command=lambda: onclick('1'))
btn2.place(x=140, y=90)

btn3 = Button(myframe, height=3, width=8, bg='#458B00', text='SCISSOR', command=lambda: onclick('2'))
btn3.place(x=240, y=90)

lbl = Label(myframe, text="Computer's choice->", height=1, width=16)
lbl.place(x=60, y=170)

opt1 = Entry(myframe, width=8, bg='#FFFAF0')
opt1.place(x=185, y=171)

opt = Entry(myframe, width=35, bg='#FFFAF0')
opt.place(x=60, y=210)

lbl1 = Label(myframe, height=4, width=8, text='ScoreBoard', bg='#F2F2F2')
lbl1.place(x=130, y=240)

lbl2 = Label(myframe, height=1, width=4, text='You', bg='#F2F2F2')
lbl2.place(x=80, y=245)

lbl3 = Label(myframe, height=1, width=4, text='com.', bg='#F2F2F2')
lbl3.place(x=210, y=245)

scru = Entry(myframe, width=5, bg='#FFFAF0')
scru.place(x=80, y=275)

scrc = Entry(myframe, width=5, bg='#FFFAF0')
scrc.place(x=210, y=275)
su, sc = 0, 0

def onclick(n):
    global su, sc 

    cc = random.randint(0, 2)
    uc = int(n)

    opt1.delete(0, tkinter.END)
    if cc == 0:
        opt1.insert(tkinter.END, 'Rock')
    elif cc == 1:
        opt1.insert(tkinter.END, 'Paper')
    else:
        opt1.insert(tkinter.END, 'Scissor')

    if cc == 2 and uc == 0:
        opt.delete(0, tkinter.END)
        opt.insert(tkinter.END, 'Congratulations! You Win')
        su += 1
        scru.delete(0, tkinter.END)
        scru.insert(tkinter.END, su)
    elif cc == 0 and uc == 2:
        opt.delete(0, tkinter.END)
        opt.insert(tkinter.END, 'Sorry, You Lost')
        sc += 1
        scrc.delete(0, tkinter.END)
        scrc.insert(tkinter.END, sc)
    elif cc > uc:
        opt.delete(0, tkinter.END)
        opt.insert(tkinter.END, 'Sorry, You Lost')
        sc += 1
        scrc.delete(0, tkinter.END)
        scrc.insert(tkinter.END, sc)
    elif cc < uc:
        opt.delete(0, tkinter.END)
        opt.insert(tkinter.END, 'Congratulations!  You Win')
        su += 1
        scru.delete(0, tkinter.END)
        scru.insert(tkinter.END, su)
    else:
        opt.delete(0, tkinter.END)
        opt.insert(tkinter.END, 'DRAW')

myroot.mainloop()
