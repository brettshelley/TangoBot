import threading
from enum import Enum
import random

class direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Player():

    current = None
    nxt = None
    facing = None
    straight = None
    back = None
    left = None
    right = None

    end = False

    hp = 100

    def __init__(self, start):
        self.current = start
        self.facing = direction.SOUTH

        while (not self.end):
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
        if self.back != None:
            print ("There is a path behind me")
        if self.left != None:
            print ("There is a path to the left")
        if self.right != None:
            print ("There is a path to the right")

    def move(self):

        move = None
        while (move == None):
            sel = input("\nSelect a direction to move\n")
            sel = sel.lower()

            if (sel.find("forward") != -1 or sel.find("straight") != -1) and self.straight != None:
                self.nxt = Board.board[self.straight]
                move = "forward"
            elif sel.find("back") != -1 and self.back != None:
                self.nxt = Board.board[self.back]
                self.facing = direction((self.facing.value + 2) % 4) 
                move = "back"
            elif sel.find("left") != -1 and self.left != None:
                self.nxt = Board.board[self.left]
                self.facing = direction((self.facing.value - 1) % 4)
                move = "left"
            elif sel.find("right") != -1 and self.right != None:
                self.nxt = Board.board[self.right]
                self.facing = direction((self.facing.value + 1) % 4)
                move = "right"

            if move == None:
                print ("\nNo path in that direction")

        print ("Moving " + move + "\n")
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
            self.hp = 100
        elif self.current.room == "coffee":
            print (Board.hint)
        elif self.current.room == "fun":
            questions = ["Who is your father?", "Who did 9 11?", "Who is the best professor?", "Who do you love the most?", "Who is a robot in disguise?"]
            q = int(random.uniform(0, len(questions)-1))
            ans = ""
            while (ans != "Hunter Lloyd"):
                ans = input(questions[q] + "\n")
            print ("\n")
        elif self.curren.room == "end":
            print ("You have reached the end")
            self.end = True

    def fight(self, enemies):
        return

class Board():

    board = [None] * 26
    hint = ""

    def __init__(self):

        i = int(random.uniform(1, 4))
        j = int(random.uniform(1, 5))
        k = int(random.uniform(1, 5))

        if i == 1:
            start = j
            end = k + 20
            hint = "south"
        elif i == 2:
            start = 5 * j
            end = (5 * (k-1)) + 1
            hint = "west"
        elif i == 3:
            start = j + 20
            end = k
            hint = "north"
        elif i == 4:
            start = (5 * (j-1)) + 1
            end = 5 * k
            hint = "east"

        self.board[start] = Node(start, "start")
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

        print ("Starting at node " + str(start))
        p = Player(self.board[start])


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


Board()
