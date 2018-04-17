import threading
from enum import Enum
import random

class direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Player():

    current = None
    facing = None
    straight = None
    back = None
    left = None
    right = None

    def __init__(self, start):
        self.current = start
        self.facing = direction.SOUTH
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

    def move(self):
        if self.straight != None:
            print ("There is a path straight ahead")
        if self.back != None:
            print ("There is a path behind me")
        if self.left != None:
            print ("There is a path to the left")
        if self.right != None:
            print ("There is a path to the right")

        move = None
        while (move == None):
            sel = input("\nSelect a direction to move\n")
            sel = sel.lower()

            if (sel.find("forward") != -1 or sel.find("straight") != -1) and self.straight != None:
                nxt = Board.board[self.straight]
                move = "forward"
            elif sel.find("back") != -1 and self.back != None:
                nxt = Board.board[self.back]
                move = "back"
            elif sel.find("left") != -1 and self.left != None:
                nxt = Board.board[self.left]
                move = "left"
            elif sel.find("right") != -1 and self.right != None:
                nxt = Board.board[self.right]
                move = "right"

            if move == None:
                print ("\nNo path in that direction")

        print ("Moving " + move)


class Board():

    board = [None] * 26

    def __init__(self):

        i = int(random.uniform(1, 4))
        j = int(random.uniform(1, 5))
        k = int(random.uniform(1, 5))

        if i == 1:
            start = j
            end = k + 20
        elif i == 2:
            start = 5 * j
            end = (5 * (k-1)) + 1
        elif i == 3:
            start = j + 20
            end = k
        elif i == 4:
            start = (5 * (j-1)) + 1
            end = 5 * k

        self.board[start] = Node(start, "start")
        self.board[end] = Node(end, "end")

        print ("Starting at node " + str(start))
        p = Player(self.board[start])

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
