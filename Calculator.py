from tkinter import *

okno = Tk()
okno.title("Калькулятор")

pole = Entry(okno, width=16, font=("Arial", 20))
pole.grid(row=0, column=0, columnspan=4)

def knopka(t):
    pole.insert(END, t)

def ravno():
    s = pole.get()
    pole.delete(0, END)
    pole.insert(0, eval(s))

def sbros():
    pole.delete(0, END)

Button(okno, text="7", width=5, height=2, command=lambda: knopka("7")).grid(row=1, column=0)
Button(okno, text="8", width=5, height=2, command=lambda: knopka("8")).grid(row=1, column=1)
Button(okno, text="9", width=5, height=2, command=lambda: knopka("9")).grid(row=1, column=2)
Button(okno, text="/", width=5, height=2, command=lambda: knopka("/")).grid(row=1, column=3)
Button(okno, text="4", width=5, height=2, command=lambda: knopka("4")).grid(row=2, column=0)
Button(okno, text="5", width=5, height=2, command=lambda: knopka("5")).grid(row=2, column=1)
Button(okno, text="6", width=5, height=2, command=lambda: knopka("6")).grid(row=2, column=2)
Button(okno, text="*", width=5, height=2, command=lambda: knopka("*")).grid(row=2, column=3)
Button(okno, text="1", width=5, height=2, command=lambda: knopka("1")).grid(row=3, column=0)
Button(okno, text="2", width=5, height=2, command=lambda: knopka("2")).grid(row=3, column=1)
Button(okno, text="3", width=5, height=2, command=lambda: knopka("3")).grid(row=3, column=2)
Button(okno, text="-", width=5, height=2, command=lambda: knopka("-")).grid(row=3, column=3)
Button(okno, text="0", width=5, height=2, command=lambda: knopka("0")).grid(row=4, column=0)
Button(okno, text=".", width=5, height=2, command=lambda: knopka(".")).grid(row=4, column=1)
Button(okno, text="=", width=5, height=2, command=ravno).grid(row=4, column=2)
Button(okno, text="+", width=5, height=2, command=lambda: knopka("+")).grid(row=4, column=3)
Button(okno, text="C", width=22, height=2, command=sbros).grid(row=5, column=0, columnspan=4)

okno.mainloop()
