import threading
from enum import Enum
import random
import gameServer as server
import time
from control import commands

class direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Player():

    msg = ""

    current = None
    nxt = None
    facing = None
    straight = None
    back = None
    left = None
    right = None

    end = False

    turns = 0

    hp = 100

    def __init__(self, start):
        self.current = Board.board[start]
        self.facing = direction.SOUTH
    
    def run(self):
        c.superReset()
        while (not conn.ready):
            time.sleep(1)
        while (not self.end and self.turns < 20):
            self.turns += 1
            self.paths()
            self.move()
        
    def paths(self):
        if self.facing == direction.NORTH:
            self.straight = self.current.north
            self.back = self.current.south
            self.left = self.current.west
            self.right = self.current.east
        elif self.facing == direction.SOUTH:
            self.straight = self.current.south
            self.back = self.current.north
            self.left = self.current.east
            self.right = self.current.west
        elif self.facing == direction.EAST:
            self.straight = self.current.east
            self.back = self.current.west
            self.left = self.current.north

            self.right = self.current.south
        elif self.facing == direction.WEST:
            self.straight = self.current.west
            self.back = self.current.east
            self.left = self.current.south
            self.right = self.current.north

        if self.straight != None:
            print ("There is a path straight ahead")
            conn.send("I can go forward")
            time.sleep(2)
        if self.back != None:
            print ("There is a path behind me")
            conn.send("I can go backward")
            time.sleep(2)
        if self.left != None:
            print ("There is a path to the left")
            conn.send("I can go left")
            time.sleep(2)
        if self.right != None:
            print ("There is a path to the right")
            conn.send("I can go right")
            time.sleep(2)

    def move(self):

        move = None
        while (move == None):
            conn.send("Choose a direction")
            time.sleep(2)
            conn.send("listen")
            while (self.msg == ""):
                time.sleep(1)
            sel = self.msg
            #sel = input("\nSelect a direction to move\n")
            sel = sel.lower()

            if (sel.find("forward") != -1 or sel.find("straight") != -1) and self.straight != None:
                self.nxt = Board.board[self.straight]
                move = "forward"
                c.forward()
            elif sel.find("back") != -1 and self.back != None:
                self.nxt = Board.board[self.back]
                self.facing = direction((self.facing.value + 2) % 4)
                move = "back"
                c.backward()
            elif sel.find("left") != -1 and self.left != None:
                self.nxt = Board.board[self.left]
                self.facing = direction((self.facing.value - 1) % 4)
                move = "left"
                c.left()
            elif sel.find("right") != -1 and self.right != None:
                self.nxt = Board.board[self.right]
                self.facing = direction((self.facing.value + 1) % 4)
                move = "right"
                c.right()

            if move == None:
                print ("\nNo path in that direction")
                conn.send("No path in that direction")
                time.sleep(2)

            self.msg = ""

        print ("Moving " + move)
        conn.send("Moving" + move)
        time.sleep(2)
        self.current = self.nxt
        self.execute()

    def execute(self):

        if self.current.room == "easy":
            enemies = [25] * int(random.uniform(3, 6))
            self.fight(enemies)
        elif self.current.room == "medium":
            enemies = [50] * int(random.uniform(2, 5))
            self.fight(enemies)
        elif self.current.room == "hard":
            enemies = [75] * int(random.uniform(1, 3))
            self.fight(enemies)
        elif self.current.room == "charge":
            print ("Charge it up! Sir Robot is restored to full health")
            conn.send("I have found a charging station. My health is restored")
            time.sleep(4)
            self.hp = 100
        elif self.current.room == "coffee":
            print ("The exit is that way")
            conn.send("I should go " + Board.hint)
        elif self.current.room == "fun":
            questions = ["Who are you?", "Who is your father", "Who is the best?", "question", "question", "question"]
            q = int(random.uniform(0, len(questions)-1))
            ans = ""
            while (ans != "Hunter Lloyd"):
                #ans = input(questions[q] + "\n")
                conn.send(questions[q])
                time.sleep(2)
                conn.send("listen")
                while (self.msg == ""):
                    time.sleep(1)
                ans = self.msg
                self.msg = ""
            print ("\n")
            conn.send("That is correct")
            time.sleep(2)
        elif self.current.room == "end":
            print ("You have reached the end")
            conn.send("I have reached the end. Hooray")
            self.end = True

    def fight(self, enemies):
        conn.send("Oh no, there are enemies here")
        time.sleep(2)
        size = len(enemies)

        if enemies[0] == 25:
            m = ("Uh oh! Sir Robot has encountered "+str(size)+" festering goblin children\n")
            enemyCount = len(enemies)
            for i in range(0,len(enemies)):
                print("What should Sir Robot do? Fight or Flee!?!")
                print("There are "+str(enemyCount)+" festering goblin children remaining\n")
                #act = input("")
                conn.send("There are " + str(enemyCount) + " festering goblins. Should I fight or run away?")
                time.sleep(4)
                conn.send("listen")
                while self.msg == "":
                    time.sleep(1)
                act = self.msg
                self.msg = ""
                act = act.lower()
                if act.find("fight")!=-1:
                    enemyHealth = 25
                    while enemyHealth >= 0:
                     c.fight()
                     hit = int(random.uniform(10,20))
                     damage = enemyCount * 1
                     self.hp = self.hp-damage
                     if self.hp <= 0:
                        print ("Sir Robot has died")
                        self.end = True
                        c.die()
                        quit()
                     conn.send("ow")
                     time.sleep(1)
                     print("Sir Robot hit a " + str(hit) + " on a goblin child")
                     print("Sir Robot took " + str(damage) +" damage!, He has " + str(self.hp) + " health remaining\n")
                     enemyHealth = enemyHealth-hit
                     if enemyHealth >= 0:
                        print("The one you've attacked is still alive you attack again!!!!")
                     else:
                        print("Great Hit! you've defeated a goblin child")
                        enemyCount = enemyCount - 1
                    conn.send("I killed one, I have " + str(self.hp) + " health reamaining")
                    time.sleep(4)
                elif act.find("run")!=-1:
                    self.flee()
                    print("We have fled!")
                    break

        elif enemies[0] == 50:
            print("Uh oh! Sir Robot has encountered "+str(size)+ " Sweaty Hob Goblins\n")
            enemyCount = len(enemies)
            for i in range(0,len(enemies)):
                print("What should Sir Robot do? Fight or Flee!?!")
                print("There are "+str(enemyCount)+" Sweaty Hob Goblins\n")
                #act = input("")
                conn.send("There are " + str(enemyCount) + " hob goblins. Should I fight or run away?")
                time.sleep(4)
                conn.send("listen")
                while self.msg == "":
                    time.sleep(1)
                act = self.msg
                self.msg = ""
                act = act.lower()
                if act.find("fight")!=-1:
                    enemyHealth = 50
                    while enemyHealth >= 0:
                     c.fight()
                     hit = int(random.uniform(15,50))
                     damage = enemyCount * 3
                     self.hp = self.hp-damage
                     if self.hp <= 0:
                        print ("Sir Robot has died")
                        self.end = True
                        c.die()
                        quit()
                     conn.send("ow")
                     time.sleep(1)
                     print("Sir Robot hit a " + str(hit) + " on a hob goblin")
                     print("Sir Robot took " + str(damage) +" damage!, He has " + str(self.hp) + " health remaining\n")
                     enemyHealth = enemyHealth-hit
                     if enemyHealth >= 0:
                        print("The one you've attacked is still alive you attack again!!!!")
                     else:
                        print("Great Hit! you've defeated a goblin child")
                        enemyCount = enemyCount - 1
                    conn.send("I killed one, I have " + str(self.hp) + " health remaining")
                    time.sleep(4)
                elif act.find("run")!=-1:
                    self.flee() 
                    print("We have fled!")
                    break

        if enemies[0] == 75:
            print("Uh oh! Sir Robot has encoutered "+str(size)+" Hunter Lloyd Changelings\n")
            enemyCount = len(enemies)
            for i in range(0,len(enemies)):
                print("What should Sir Robot do? Fight or Flee!?!")
                print("There are "+str(enemyCount)+" Hunter Lloyd Changelings remaining\n")
                #act = input("")
                conn.send("There are " + str(enemyCount) + " changelings. Should I fight or run away?")
                time.sleep(4)
                conn.send("listen")
                while self.msg == "":
                    time.sleep(1)
                act = self.msg
                self.msg = ""
                act = act.lower()
                if act.find("fight")!=-1:
                    enemyHealth = 75
                    while enemyHealth >= 0:
                     c.fight()
                     hit = int(random.uniform(25,75))
                     damage = enemyCount * 8
                     self.hp = self.hp-damage
                     if self.hp <= 0:
                        print("Sir Robot has died")
                        self.end = True
                        c.die()
                        quit()
                     conn.send("ow")
                     time.sleep(1)
                     print("Sir Robot hit a " + str(hit) + " on a Hunter Lloyd")
                     print("Sir Robot took " + str(damage) +" damage!, It has " + str(self.hp) + " health remaining\n")
                     enemyHealth = enemyHealth-hit
                     if enemyHealth >= 0:
                        print("Its still alive you attack again!!!!")
                     else:
                        print("Great Hit! you've defeated a goblin child")
                        enemyCount = enemyCount - 1
                    conn.send("I killed one. I have " + str(self.hp) + " health remaining")
                    time.sleep(4)
                elif act.find("run")!=-1:
                    self.flee()
                    print("We have fled!")
                    break
                     
        
        if (enemyCount == 0):
            print("You've defeated the baddies, continue on with your adventure")
            conn.send("I have defeated the enemies")
            time.sleep(2)

    def flee(self):
        fleeTo = None
        while (fleeTo == None):
            i = int(random.uniform(1, 4))
            if (i == 1 and self.right != None):
                fleeTo = self.right
            elif (i == 2 and self.left != None):
                fleeTo = self.left
            elif (i == 3 and self.straight != None):
                fleeTo = self.straight
            elif (i == 4 and self.back != None):
                fleeTo = self.back

        self.current = Board.board[fleeTo]
        conn.send("I have escaped to a safe place")
        time.sleep(4)
                

class Board():

    board = [None] * 26
    hint = ""
    start = None

    def __init__(self):

        i = int(random.uniform(1, 4))
        j = int(random.uniform(1, 5))
        k = int(random.uniform(1, 5))

        if i == 1:
            self.start = j
            end = k + 20
            self.hint = "south"
        elif i == 2:
            self.start = 5 * j
            end = (5 * (k-1)) + 1
            self.hint = "west"
        elif i == 3:
            self.start = j + 20
            end = k
            self.hint = "north"
        elif i == 4:
            self.start = (5 * (j-1)) + 1
            end = 5 * k
            self.hint = "east"

        self.board[self.start] = Node(self.start, "start")
        self.board[end] = Node(end, "end")

        rooms = ["charge"] * 4
        rooms = rooms + (["coffee"] * 2)
        rooms = rooms + (["easy"] * 6)
        rooms = rooms + (["medium"] * 5)
        rooms = rooms + (["hard"] * 3)
        rooms = rooms + (["fun"] * 3)

        random.shuffle(rooms)

        for i in range(1,26):
            if self.board[i] == None:
                self.board[i] = Node(i, rooms.pop())

        print ("Starting at node " + str(self.start))
        #p = Player(self.board[start])


class Node():
    
    north = None
    east = None
    south = None
    west = None
    room = None
    

    def __init__(self, pos, r):

        self.room = r

        if pos == 1:
            self.east = 2
        elif pos == 2:
            self.west = 1
            self.east = 3
            self.south = 7
        elif pos == 3:
            self.south = 8
            self.west = 2
        elif pos == 4:
            self.east = 5
        elif pos == 5:
            self.west = 4
            self.south = 10
        elif pos == 6:
            self.east = 7
            self.south = 11
        elif pos == 7:
            self.west = 6
            self.north = 2
            self.south = 12
        elif pos == 8:
            self.north = 3
        elif pos == 9:
            self.east = 10
            self.south = 14
        elif pos == 10:
            self.north = 5
            self.west = 9
            self.south = 15
        elif pos == 11:
            self.north = 6
            self.south = 16
        elif pos == 12:
            self.north = 7
            self.east = 13
        elif pos == 13:
            self.west = 12
            self.east = 14
        elif pos == 14:
            self.north = 9
            self.west = 13
            self.south = 19
        elif pos == 15:
            self.north = 10
            self.south = 20
        elif pos == 16:
            self.north = 11
            self.east = 17
        elif pos == 17:
            self.west = 16
            self.south = 22
        elif pos == 18:
            self.south = 23
        elif pos == 19:
            self.north = 14
            self.east = 20
            self.south = 24
        elif pos == 20:
            self.north = 15
            self.west = 19
        elif pos == 21:
            self.east = 22
        elif pos == 22:
            self.west = 21
            self.north = 17
            self.east = 23
        elif pos == 23:
            self.west = 22
            self.north = 18
        elif pos == 24:
            self.north = 19
            self.east = 25
        elif pos == 25:
            self.west = 24


if __name__ == '__main__':

    print ("Starting main")

    c = commands()
    
    b = Board()
    print (b.start)
    p = Player(b.start)
    conn = server.Server(p)

    threads = []
    threads.append(threading.Thread(name='server', target=conn.startUp))

    for thread in threads:
        thread.start()

    p.run()

    for thread in threads:
        thread.join()

