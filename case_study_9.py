
    
from tkinter import *
root = Tk()


numb1= Entry(root)
numb2= Entry(root)
resbox = Entry(root)


num1 = Label(root,text="Input Number 1:" )
num2 = Label(root,text="Input Number 2:" )
but1 = Button(root, text="+",padx=40,)
but2 = Button(root, text="-",padx=40,)
but3 = Button(root, text="*",padx=40,)
but4  = Button(root, text="/",padx=40,)
res = Label(root,text="Result",padx=40,)
    #placement
num1.grid( row=0, column =0)
numb1.grid(row=0,column=1)
num2.grid( row=1, column =0)
numb2.grid( row=1, column =1)

but1.grid( row=2, column =0)
but2.grid( row=2, column =1)
but3.grid( row=2, column =2)
but4.grid( row=2, column =3)


res.grid( row=3, column=0)
resbox.grid(row=3, column=1)


root.mainloop



'''def box1():
 top = Tk()
 L1 = Label(top,text="Input Number 1:" )
 L1.pack( side = LEFT)
 E1 = Label(top,text="Input Number 2:" )
 E1 = Entry(top, bd =5)
 E1.pack(side = RIGHT)
 box2()

box1()


    

master = tk.Tk()
tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

master.mainloop()
'''
