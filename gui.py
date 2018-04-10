from Maestro import Controller
import tkinter as tk
import time
import queue
from tkinter.font import Font
import server
import threading


class Button():
    def createMove():
        global count
        count=count+1
        m = Move()
        instance = tk.Button(frame, text="Move", width=19, height=6, command=m.popUp)
        Button.place(instance)
        m.popUp

    def createTurn():
        global count
        count=count+1
        t = Turn()
        instance = tk.Button(frame, text="Turn", width=19, height=6, command=t.popUp)
        Button.place(instance)

    def createBody():
        global count
        count=count+1
        b = Body()
        instance = tk.Button(frame, text="Body", width=19, height=6, command=b.popUp)
        Button.place(instance)

    def createHead():
        global count
        count=count+1
        h = Head()
        instance = tk.Button(frame, text="Head", width=19, height=6, command=h.popUp)
        Button.place(instance)

    def createListen():
        global count
        count=count+1
        l = Listen()
        instance = tk.Button(frame, text="Listen", width=19, height=6)
        Button.place(instance)

    def createSpeak():
        global count
        count=count+1
        s = Speak()
        instance = tk.Button(frame, text="Speak", width=19, height=6, command=s.popUp)
        Button.place(instance)

    def place(instance):
        global count
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
        pop.minsize(200, 150)
        pop.title("Properties")

        self.var = tk.IntVar()
        forward = tk.Radiobutton(pop, text="Forward", variable=self.var, value=0, command=self.direction)
        backwards = tk.Radiobutton(pop, text="Reverse", variable=self.var, value=1, command=self.direction)
        label = tk.Label(pop, text="Duration:")
        self.durationBox = tk.Spinbox(pop, width=5, from_=0, to=30, increment=0.5, command=self.duration, font=Font(family='Helvetica', size=20)) 
        save = tk.Button(pop, text=B"Save", width=10, height=2, command=pop.destroy)

        forward.grid(pady=15)
        backwards.grid()
        label.grid(pady=20)
        self.durationBox.grid(column=2, row=2, padx=5)
        save.grid(pady=20, columnspan=3)

        forward.invoke()

    def direction(self):
        d = self.var.get()
        if (d==0):
            self.speed=5000
        elif (d==1):
            self.speed=7000

    def duration(self):
        d = self.durationBox.get()
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
        self.durationBox = tk.Spinbox(pop, width=5, from_=0, to=30, increment=0.5, command=self.duration, font=Font(family='Helvetica', size=20)) 
        save = tk.Button(pop, text="Save", width=10, height=2, command=pop.destroy)
        
        left.grid(pady=15)
        right.grid()
        label.grid(pady=20)
        self.durationBox.grid(column=2, row=2, padx=5)
        save.grid(pady=20, columnspan=3)

        left.invoke()

    def direction(self):
        d = self.var.get()
        if (d==0):
            self.speed=7000
        elif (d==1):
            self.speed=5000

    def duration(self):
        d = self.durationBox.get()
        self.sleep=d

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
        center = tk.Radiobutton(pop, text="Center", variable=self.var, value=2, command=self.direction)
        save = tk.Button(pop, text="Save", width=10, height=2, command=pop.destroy)

        left.grid(pady=15)
        right.grid()
        center.grid(pady=15)
        save.grid(pady=20, padx=25)

        left.invoke()

    def direction(self):
        d = self.var.get()
        if (d==0):
            self.turn=7500
        elif (d==1):
            self.turn=4500
        elif (d==2):
            self.turn=self.center

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
        center = tk.Radiobutton(pop, text="Center", variable=self.var, value=4, command=self.direction)
        save = tk.Button(pop, text="save", width=10, height=2, command=pop.destroy)

        left.grid(pady=15)
        right.grid()
        up.grid(pady=15)
        down.grid()
        center.grid(pady=15)
        save.grid(pady=20, padx=25)

        left.invoke()

    def direction(self):
        d = self.var.get()
        if (d==0 or d==2):
            self.turn=7500
        elif (d==1 or d==3):
            self.turn=4500

class Listen():
    def __init__(self):
        global q
        q.put(self)

    def cmd(self):
        msg = "listen"


class Speak():
    def __init__(self):
        self.msg='Hello'

        global q
        q.put(self)

    def popUp(self):
        pop=tk.Toplevel()
        pop.minsize(180, 180)
        pop.title("Properties")

        self.var = tk.IntVar()
        hello = tk.Radiobutton(pop, text="Hello", variable=self.var, value=0, command=self.phrase)
        beep = tk.Radiobutton(pop, text="Beep", variable=self.var, value=1, command=self.phrase)
        nothing = tk.Radiobutton(pop, text="Nothing Found", variable=self.var, value=2, command=self.phrase)
        what = tk.Radiobutton(pop, text="What should do?", variable=self.var, value=3, command=self.phrase)
        cat = tk.Radiobutton(pop, text= "Cat", variable=self.var, value=4, command=self.phrase)
        save = tk.Button(pop, text="save", width=10, height=2, command=pop.destroy)

        beep.grid(pady=15)
        hello.grid()
        nothing.grid(pady=15)
        what.grid()
        cat.grid(pady=15)
        save.grid(pady=20, padx=25)

    def phrase(self):
        choice = self.var.get()
        if choice==0:
            self.msg = "Hello"
        elif choice==1:
            self.msg = "Beep beep lettuce"
        elif choice==2:
            self.msg = "Nothing found here"
        elif choice==3:
            self.msg = "What should I do next"
        elif choice ==4:
            self.msg = "I like cats"

class Control():
    def run():
        global q
        qTemp = queue.Queue()
        for i in range(q.qsize()):
            x = q.get()
            qTemp.put(x)
            target = 0

            # Maestro code to execute each command
            if type(x) is Head:
                if (x.var.get() == 0 or x.var.get() == 1):
                    rob.setTarget(3, x.turn)
                elif (x.var.get() == 2 or x.var.get() == 3):
                    rob.setTarget(4, x.turn)
                elif (x.var.get() == 4):
                    rob.setTarget(3, x.center)
                    rob.setTarget(4, x.center)
            elif type(x) is Body:
                target = 0
            elif type(x) is Turn:
                target = 2
            elif type(x) is Move:
                target = 1
            
            if (type(x) is Body):
                rob.setTarget(target, x.turn)
            elif (type(x) is Turn or type(x) is Move):
                rob.setTarget(target, x.speed)
                time.sleep(float (x.sleep))
                rob.setTarget(target, x.stop)

            if (type(x) is Listen):
                conn.connect()
                conn.send("listen")
                time.sleep(7)
            elif (type(x) is Speak):
                conn.connect()
                conn.send(x.msg + "  ")
                
            time.sleep(1)

        q = qTemp

    def reset():
        q.queue.clear()
        for j in frame.winfo_children():
            j.destroy()

class GUI():
    def run(self):
        global rob
        rob = Controller()
        global q
        q = queue.Queue()
        global count
        count = 0

        win = tk.Tk()
        win.title("Tango Bot")

        moveButton = tk.Button(win, width="12", text="Move", command=Button.createMove)
        turnButton = tk.Button(win, width="12", text="Turn", command=Button.createTurn)
        bodyButton = tk.Button(win, width="12", text="Rotate Body", command=Button.createBody)
        headButton = tk.Button(win, width="12", text="Move Head", command=Button.createHead)
        listenButton = tk.Button(win, width="12", text="Listen", command=Button.createListen)
        speakButton = tk.Button(win, width="12", text="Speak", command=Button.createSpeak)
        moveButton.grid(column=0, row=0, pady=10)
        turnButton.grid(column=1, row=0, pady=10)
        bodyButton.grid(column=2, row=0, pady=10)
        headButton.grid(column=3, row=0, pady=10)
        listenButton.grid(column=4, row=0, pady=10)
        speakButton.grid(column=5, row=0, pady=10)
    
        global frame
        frame = tk.Frame(win, width=750, height=300)
        frame.grid(columnspan=6, row=1, padx=15, pady=15)
        frame.grid_propagate(False)

        reset = tk.Button(win, width="20", text="Reset", command=Control.reset)
        run = tk.Button(win, width="20", text="Run", command=Control.run)
        reset.grid(columnspan=3, column=0, row=2, pady=10)
        run.grid(columnspan=3, column=2, row=2, pady=10)

        win.mainloop()

if __name__ == '__main__':

    print("started main")

    gui = GUI()
    conn = server.Server(gui)

    # create list of threads
    threads = []

    # create server thread
    threads.append(threading.Thread(name='tcp_server', target=conn.startUp))

    # start all threads
    for thread in threads:
        print("starting thread", thread.name)
        thread.start()

    gui.run()

    # join all threads
    for thread in threads:
        thread.join()

