import Maestro
import tkinter as tk
import time
import queue

class Button():
    def createMove():
        global count
        count=count+1
        m = Move()
        instance = tk.Button(frame, text="Move", width=25, height=10, command=m.popUp)
        Button.place(instance)
        m.popUp

    def createTurn():
        global count
        count=count+1
        t = Turn()
        instance = tk.Button(frame, text="Turn", width=25, height=10, command=t.popUp)
        Button.place(instance)

    def createBody():
        global count
        count=count+1
        b = Body()
        instance = tk.Button(frame, text="Body", width=25, height=10, command=b.popUp)
        Button.place(instance)

    def createHead():
        global count
        count=count+1
        h = Head()
        instance = tk.Button(frame, text="Head", width=25, height=10, command=h.popUp)
        Button.place(instance)

    def place(instance):
        if (count < 5):
            r=0
        elif(count < 9):
            r=1
        else:
            r=2

        if (count%4 == 1):
            c=0
        elif (count%4 == 2):
            c=1
        elif(count%4 == 3):
            c=2
        elif(count%4 == 0):
            c=3

        instance.grid(row=r, column=c)
    
class Move():
    def __init__(self):
        self.speed=0
        self.stop=6000
        self.sleep=0

        global q
        q.put(self)

    def popUp(self):
        pop = tk.Toplevel()
        pop.minsize(180, 150)
        pop.title("Properties")

        self.var = tk.IntVar()
        forward = tk.Radiobutton(pop, text="Forward", variable=self.var, value=0, command=self.direction)
        backwards = tk.Radiobutton(pop, text="Reverse", variable=self.var, value=1, command=self.direction)
        label = tk.Label(pop, text="Duration:")
        self.duration = tk.Spinbox(pop, width=5, from_=0, to=30, increment=0.5, command=self.duration) 
        
        forward.grid(pady=15)
        backwards.grid()
        label.grid(pady=20)
        self.duration.grid(column=2, row=2, padx=5)

    def direction(self):
        d = self.var
        if (d==0):
            self.speed=1000
        elif (d==1):
            self.speed=-1000

    def duration(self):
        d = self.duration.get()
        self.sleep=d

class Turn():
    def __init__(self):
        self.speed=0
        self.stop=6000
        self.sleep=0

        global q
        q.put(self)

    def popUp(self):
        pop = tk.Toplevel()
        pop.minsize(180, 150)
        pop.title("Properties")
        
        self.var = tk.IntVar()
        left = tk.Radiobutton(pop, text="Left", variable=self.var, value=0, command=self.direction)
        right = tk.Radiobutton(pop, text="Right", variable=self.var, value=1, command=self.direction)
        label = tk.Label(pop, text="Duration:")
        self.duration = tk.Spinbox(pop, width=5, from_=0, to=30, increment=0.5, command=self.duration) 
        
        left.grid(pady=15)
        right.grid()
        label.grid(pady=20)
        self.duration.grid(column=2, row=2, padx=5)

    def direction(self):
        d = self.var
        if (d==0):
            self.speed=1000
        elif (d==1):
            self.speed=-1000

    def duration(self):
        d = self.duration.get()

class Body():
    def __init__(self):
        self.center=6000
        self.turn=0

        global q
        q.put(self)

    def popUp(self):
        pop=tk.Toplevel()
        pop.minsize(180, 110)
        pop.title("Properties")
        
        self.var = tk.IntVar()
        left = tk.Radiobutton(pop, text="Left", variable=self.var, value=0, command=self.direction)
        right = tk.Radiobutton(pop, text="Right", variable=self.var, value=1, command=self.direction)

        left.grid(pady=15)
        right.grid()

    def direction(self):
        d = self.var
        if (d==0):
            self.turn=4500
        elif (d==1):
            self.speed=7500

class Head():
    def __init__(self):
        self.center=6000
        self.turn=0

        global q
        q.put(self)

    def popUp(self):
        pop=tk.Toplevel() 
        pop.minsize(180, 180)
        pop.title("Properties")
        
        self.var = tk.IntVar()
        left = tk.Radiobutton(pop, text="Left", variable=self.var, value=0, command=self.direction)
        right = tk.Radiobutton(pop, text="Right", variable=self.var, value=1, command=self.direction)
        up = tk.Radiobutton(pop, text="Up", variable=self.var, value=2, command=self.direction)
        down = tk.Radiobutton(pop, text="Down", variable=self.var, value=3, command=self.direction)

        left.grid(pady=15)
        right.grid()
        up.grid(pady=15)
        down.grid()

    def direction(self):
        d = self.var
        if (d==0 or d==2):
            self.turn=4500
        elif (d==1 or d==3):
            self.speed=7500

class Control():
    def run():
        global q
        qTemp = queue.Queue()
        for i in range(q.qsize()):
            x = q.get()
            qTemp.put(x)
            
            # Maestro code to execute each command

        q = qTemp

    def reset():
        q.queue.clear()
        for j in frame.winfo_children():
            j.destroy()

q = queue.Queue()
count=0

win = tk.Tk()
win.title("Tango Bot")

moveButton = tk.Button(win, width="20", text="Move", command=Button.createMove)
turnButton = tk.Button(win, width="20", text="Turn", command=Button.createTurn)
bodyButton = tk.Button(win, width="20", text="Rotate Body", command=Button.createBody)
headButton = tk.Button(win, width="20", text="Move Head", command=Button.createHead)
moveButton.grid(column=0, row=0, pady=10)
turnButton.grid(column=1, row=0, pady=10)
bodyButton.grid(column=2, row=0, pady=10)
headButton.grid(column=3, row=0, pady=10)

frame = tk.Frame(win, width=920, height=500)
frame.grid(columnspan=4, row=1, padx=15, pady=15)
frame.grid_propagate(False)

reset = tk.Button(win, width="25", text="Reset", command=Control.reset)
run = tk.Button(win, width="25", text="Run", command=Control.run)
reset.grid(columnspan=2, column=0, row=2, pady=10)
run.grid(columnspan=2, column=2, row=2, pady=10)

win.mainloop()
