import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

####################################################### AND WINDOW ##############################################################################
def and_window():
    global root1
    try:
        if root1.state() == "normal": root1.focus()
    except:
        root1 = tk.Toplevel()
        root1.geometry("300x300+500+200")
    canvas_height = 1000
    canvas_width = 700
    root1.geometry('400x400')  
    root1.title("And Gate")
    myframe=Frame(root1)
    myframe.pack(fill=BOTH, expand=NO)
    canvas1 = Canvas(root1, height = 700, width = 300, bg = 'sandy brown') 
    canvas1.pack(fill = 'both')
    def moved(event):
        canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
    canvas1.bind("<Motion>", moved)
    tag = canvas1.create_text(10, 10, text="", anchor="nw")  #nw = north-west

    #a label,entry
    aEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    aEntry.pack(padx=20, pady=20)
    aEntry.place(x=60, y=50)
    aEntry.config(font=("Courier", 12, 'bold'))

    aLabel = Label(canvas1,text='a', justify = LEFT, bg='sandy brown', fg='black')
    aLabel.config(font=("Courier", 12, 'bold'))
    aLabel.pack()
    aLabel.place(x=90, y=50)


    #b label,entry
    bEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    bEntry.pack(padx=20, pady=20)
    bEntry.place(x=60, y=80)
    bEntry.config(font=("Courier", 12, 'bold'))

    bLabel = Label(canvas1,text='b', justify = LEFT, bg='sandy brown', fg='black')
    bLabel.config(font=("Courier", 12, 'bold'))
    bLabel.pack()
    bLabel.place(x=90, y=80)
    canvas1.create_line(115,60,200,60)
    canvas1.create_line(115,90,200,90)
    #canvas1.create_line(200,40,200,110)
    #add an arc here after the lines
    #           (Shift in x axis1) y1(from bottom)      y2(from bottom(upwards)) starting point     #degree
    arc1 = canvas1.create_arc(165, 110,            235, 40,                      start = -90,       extent=180, fill="#000000")
    canvas1.create_line(235,75,300,75)

    #c entry
    cEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    cEntry.pack(padx=20, pady=20)
    cEntry.place(x=310, y=65)
    cEntry.config(font=("Courier", 12, 'bold'))

    #button
    def andgate():
        cEntry.delete(0,END)
        try:
            a=int(aEntry.get())
            b=int(bEntry.get())
            if (a==0 or a==1)and(b==0 or b==1):
                c=str(a*b)
                cEntry.insert(0,c)
            else:
                mb.showinfo('Wrong Input', 'Logic Gates accept only binary')
        except:
            mb.showinfo('Wrong Input', 'Logic Gates accept only binary')
    andButton=Button(canvas1, relief=tk.FLAT, width=5, text="AND", anchor = CENTER, command=andgate)
    andButton.pack(padx=20,pady=20)
    andButton.place(x=180,y=150)
    andButton.config(font=("Courier", 12, 'bold'))

    #canvas1.update()
    root1.mainloop()

################################################################# END OF AND WINDOW ##############################################################

#################################################################### AND WINDOW ##############################################################################

def or_window():
    global root2
    try:
        if root2.state() == "normal": root2.focus()
    except:
        root2 = tk.Toplevel()
        root2.geometry("300x300+500+200")


    canvas_height = 1000
    canvas_width = 700
    root2.geometry('400x400')  
    root2.title("Or Gate")

    myframe=Frame(root2)
    myframe.pack(fill=BOTH, expand=NO)
    canvas1 = Canvas(root2, height = 700, width = 300, bg = 'sandy brown') 
    canvas1.pack(fill = 'both')

    def moved(event):
        canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
    canvas1.bind("<Motion>", moved)
    tag = canvas1.create_text(10, 10, text="", anchor="nw")  #nw = north-west

    #a label,entry
    aEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    aEntry.pack(padx=20, pady=20)
    aEntry.place(x=60, y=50)
    aEntry.config(font=("Courier", 12, 'bold'))

    aLabel = Label(canvas1,text='a', justify = LEFT, bg='sandy brown', fg='black')
    aLabel.config(font=("Courier", 12, 'bold'))
    aLabel.pack()
    aLabel.place(x=90, y=50)


    #b label,entry
    bEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    bEntry.pack(padx=20, pady=20)
    bEntry.place(x=60, y=80)
    bEntry.config(font=("Courier", 12, 'bold'))

    bLabel = Label(canvas1,text='b', justify = LEFT, bg='sandy brown', fg='black')
    bLabel.config(font=("Courier", 12, 'bold'))
    bLabel.pack()
    bLabel.place(x=90, y=80)


    canvas1.create_line(115,60,200,60)
    canvas1.create_line(115,90,200,90)
    canvas1.create_line(235,75,300,75)
    canvas1.create_line(190,40,220,75,190,110, smooth="true")
    canvas1.create_line(190,40,235,75)
    canvas1.create_line(190,110,235,75)    

    #c entry
    cEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    cEntry.pack(padx=20, pady=20)
    cEntry.place(x=310, y=65)
    cEntry.config(font=("Courier", 12, 'bold'))

    #button
    def orgate():
        cEntry.delete(0,END)
        try:
            a=int(aEntry.get())
            b=int(bEntry.get())
            if (a==0 or a==1)and(b==0 or b==1):
                c=str(a+b)
                cEntry.insert(0,c)
            else:
                mb.showinfo('Wrong Input', 'Logic Gates accept only binary')
        except:
            mb.showinfo('Wrong Input', 'Logic Gates accept only binary')
    orButton=Button(canvas1, relief=tk.FLAT, width=5, text="OR", anchor = CENTER, command=orgate)
    orButton.pack(padx=20,pady=20)
    orButton.place(x=180,y=150)
    orButton.config(font=("Courier", 12, 'bold'))

    #canvas1.update()
    root2.mainloop()

################################################################# END OF AND WINDOW ################################################################


#################################################################### NOT WINDOW ##############################################################################

def not_window():
    global root3
    try:
        if root3.state() == "normal": root3.focus()
    except:
        root3 = tk.Toplevel()
        root3.geometry("300x300+500+200")

    canvas_height = 1000
    canvas_width = 700
    root3.geometry('400x400')  
    root3.title("Not Gate")

    myframe=Frame(root3)
    myframe.pack(fill=BOTH, expand=NO)
    canvas1 = Canvas(root3, height = 700, width = 300, bg = 'sandy brown') 
    canvas1.pack(fill = 'both')

    def moved(event):
        canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
    canvas1.bind("<Motion>", moved)
    tag = canvas1.create_text(10, 10, text="", anchor="nw")  #nw = north-west

    #b label,entry
    bEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    bEntry.pack(padx=20, pady=20)
    bEntry.place(x=60, y=80)
    bEntry.config(font=("Courier", 12, 'bold'))

    bLabel = Label(canvas1,text='b', justify = LEFT, bg='sandy brown', fg='black')
    bLabel.config(font=("Courier", 12, 'bold'))
    bLabel.pack()
    bLabel.place(x=90, y=80)


    canvas1.create_line(115,90,200,90)
    points=[200,60,200,120,260,90]
    canvas1.create_polygon(points)
    canvas1.create_line(260,90,320,90)

    #c entry
    cEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    cEntry.pack(padx=20, pady=20)
    cEntry.place(x=330, y=80)
    cEntry.config(font=("Courier", 12, 'bold'))

    #button
    def notgate():
        cEntry.delete(0,END)
        try:
            b=int(bEntry.get())
            if b==0:
                cEntry.insert(0,"1")
            elif b==1:
                cEntry.insert(0,"0")
            else:
                mb.showinfo('Wrong Input', 'Logic Gates accept only binary')
        except:
            mb.showinfo('Wrong Input', 'Logic Gates accept only binary')
    notButton=Button(canvas1, relief=tk.FLAT, width=5, text="NOT", anchor = CENTER, command=notgate)
    notButton.pack(padx=20,pady=20)
    notButton.place(x=180,y=150)
    notButton.config(font=("Courier", 12, 'bold'))

    #canvas1.update()
    root3.mainloop()

########################################################## END OF NOT GATE #####################################################################

########################################################## NAND GATE #########################################################333
def nand_window():
    global root4
    try:
        if root4.state() == "normal": root4.focus()
    except:
        root4 = tk.Toplevel()
        root4.geometry("300x300+500+200")
    canvas_height = 1000
    canvas_width = 700
    root4.geometry('400x400')  
    root4.title("Nand Gate")
    myframe=Frame(root4)
    myframe.pack(fill=BOTH, expand=NO)
    canvas1 = Canvas(root4, height = 700, width = 300, bg = 'sandy brown') 
    canvas1.pack(fill = 'both')
    def moved(event):
        canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
    canvas1.bind("<Motion>", moved)
    tag = canvas1.create_text(10, 10, text="", anchor="nw")  #nw = north-west

    #a label,entry
    aEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    aEntry.pack(padx=20, pady=20)
    aEntry.place(x=60, y=50)
    aEntry.config(font=("Courier", 12, 'bold'))

    aLabel = Label(canvas1,text='a', justify = LEFT, bg='sandy brown', fg='black')
    aLabel.config(font=("Courier", 12, 'bold'))
    aLabel.pack()
    aLabel.place(x=90, y=50)


    #b label,entry
    bEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    bEntry.pack(padx=20, pady=20)
    bEntry.place(x=60, y=80)
    bEntry.config(font=("Courier", 12, 'bold'))

    bLabel = Label(canvas1,text='b', justify = LEFT, bg='sandy brown', fg='black')
    bLabel.config(font=("Courier", 12, 'bold'))
    bLabel.pack()
    bLabel.place(x=90, y=80)
    canvas1.create_line(115,60,200,60)
    canvas1.create_line(115,90,200,90)
    arc1 = canvas1.create_arc(165, 110,235, 40,start = -90,extent=180, fill="#000000")
    canvas1.create_line(235,75,300,75)
    canvas1.create_oval(245, 80, 235, 70,fill="black", width=2)
    
    #c entry
    cEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    cEntry.pack(padx=20, pady=20)
    cEntry.place(x=310, y=65)
    cEntry.config(font=("Courier", 12, 'bold'))

    #button
    def nandgate():
        cEntry.delete(0,END)
        try:
            a=int(aEntry.get())
            b=int(bEntry.get())
            if (a==0 or a==1)and(b==0 or b==1):
                c=str(a*b)
                if c=="0":
                    cEntry.insert(0,"1")
                else:
                    cEntry.insert(0,"0")
            else:
                mb.showinfo('Wrong Input', 'Logic Gates accept only binary')
        except:
            mb.showinfo('Wrong Input', 'Logic Gates accept only binary')
    andButton=Button(canvas1, relief=tk.FLAT, width=5, text="NAND", anchor = CENTER, command=nandgate)
    andButton.pack(padx=20,pady=20)
    andButton.place(x=180,y=150)
    andButton.config(font=("Courier", 12, 'bold'))

    #canvas1.update()
    root4.mainloop()

#####################################################################END OF NAND GATE###################################

#################################################################### NOR WINDOW ##############################################################################

def nor_window():
    global root5
    try:
        if root5.state() == "normal": root5.focus()
    except:
        root5 = tk.Toplevel()
        root5.geometry("300x300+500+200")


    canvas_height = 1000
    canvas_width = 700
    root5.geometry('400x400')  
    root5.title("Nor Gate")

    myframe=Frame(root5)
    myframe.pack(fill=BOTH, expand=NO)
    canvas1 = Canvas(root5, height = 700, width = 300, bg = 'sandy brown') 
    canvas1.pack(fill = 'both')

    def moved(event):
        canvas1.itemconfigure(tag, text="(%r, %r)" % (event.x, event.y))
    canvas1.bind("<Motion>", moved)
    tag = canvas1.create_text(10, 10, text="", anchor="nw")  #nw = north-west

    #a label,entry
    aEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    aEntry.pack(padx=20, pady=20)
    aEntry.place(x=60, y=50)
    aEntry.config(font=("Courier", 12, 'bold'))

    aLabel = Label(canvas1,text='a', justify = LEFT, bg='sandy brown', fg='black')
    aLabel.config(font=("Courier", 12, 'bold'))
    aLabel.pack()
    aLabel.place(x=90, y=50)


    #b label,entry
    bEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    bEntry.pack(padx=20, pady=20)
    bEntry.place(x=60, y=80)
    bEntry.config(font=("Courier", 12, 'bold'))

    bLabel = Label(canvas1,text='b', justify = LEFT, bg='sandy brown', fg='black')
    bLabel.config(font=("Courier", 12, 'bold'))
    bLabel.pack()
    bLabel.place(x=90, y=80)


    canvas1.create_line(115,60,200,60)
    canvas1.create_line(115,90,200,90)
    canvas1.create_line(190,40,220,75,190,110, smooth="true")
    canvas1.create_line(190,40,235,75)
    canvas1.create_line(190,110,235,75)
    canvas1.create_line(235,75,300,75)
    canvas1.create_oval(245, 80, 235, 70,fill="black", width=2)


    #c entry
    cEntry = Entry(canvas1, relief=tk.FLAT, width = 2)
    cEntry.pack(padx=20, pady=20)
    cEntry.place(x=310, y=65)
    cEntry.config(font=("Courier", 12, 'bold'))

    #button
    def norgate():
        cEntry.delete(0,END)
        try:
            a=int(aEntry.get())
            b=int(bEntry.get())
            if (a==0 or a==1)and(b==0 or b==1):
                c=str(a+b)
                if c=="0":
                    cEntry.insert(0,"1")
                else:
                    cEntry.insert(0,"0")
            else:
                mb.showinfo('Wrong Input', 'Logic Gates accept only binary')
        except:
            mb.showinfo('Wrong Input', 'Logic Gates accept only binary')
    orButton=Button(canvas1, relief=tk.FLAT, width=5, text="NOR", anchor = CENTER, command=norgate)
    orButton.pack(padx=20,pady=20)
    orButton.place(x=180,y=150)
    orButton.config(font=("Courier", 12, 'bold'))

    #canvas1.update()
    root5.mainloop()

################################################################# END OF NOR WINDOW ################################################################



win = tk.Tk()
win.geometry("200x200+200+100")
and_button = tk.Button(win, text="And Gate")
and_button['command'] = and_window
and_button.pack()

or_button = tk.Button(win, text="Or Gate")
or_button['command'] = or_window
or_button.pack()

not_button = tk.Button(win, text="Not Gate")
not_button['command'] = not_window
not_button.pack()

nand_button = tk.Button(win, text="NAND Gate")
nand_button['command'] = nand_window
nand_button.pack()

nor_button = tk.Button(win, text="Nor Gate")
nor_button['command'] = nor_window
nor_button.pack()

win.mainloop()
