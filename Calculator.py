
# coding: utf-8

# In[40]:

from Tkinter import *
 
def frame(root, side):
    f = Frame(root)
    f.pack(side=side, expand=YES, fill=BOTH)
    return f
 
def button(root, side, text, command=None):
    b = Button(root, text=text, command=command)
    b.pack(side=side,expand=YES, fill=BOTH)
    return b
 
class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Calculator')
        
 
        display = StringVar()
        Entry(self, relief=SUNKEN, textvariable=display).pack(side=TOP, expand=YES, fill=BOTH)
 
        for num in ("123", "456", "789", "-0."):
            F = frame(self, TOP)
            for n in num:
                button(F, LEFT, n, lambda w=display, s='%s'%n: w.set(w.get() + s))
 
        F = frame(self, TOP)
        for char in "+-*/=":
            if char == '=':
                btn = button(F, LEFT, char)
                btn.bind('<ButtonRelease-1>', lambda e, s = self, w=display: s.calc(w), '+')
            else:
                btn = button(F, LEFT, char, lambda w=display, c=char: w.set(w.get() + ' '+c+' '))
        F = frame(self, BOTTOM)
        button(F, LEFT, 'Clr', lambda w=display: w.set(''))
    def calc(self, display):
        try:
            display.set( eval(display.get()) )
        except ValueError:
            display.set("type error")
 


Calculator().mainloop()


# In[ ]:



