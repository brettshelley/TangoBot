from Maestro import Controller
import time
import random

class commands:
    rob = Controller()
    

    def fight(self):
    
     targetR= 6
     targetL= 12
     targetRR = 8
     targetLL = 14

     self.rob.setTarget(targetR,0)
     self.rob.setTarget(targetL,0)
     self.rob.setTarget(targetRR,0)
     self.rob.setTarget(targetLL,0)

     for i in range(0,2):
        self.rob.setTarget(targetR,8000)
        self.rob.setTarget(targetL,2000)
        self.rob.setTarget(targetRR,8000)
        self.rob.setTarget(targetLL,8000)
        time.sleep(.5)
        self.rob.setTarget(targetR,0)
        self.rob.setTarget(targetL,0)
        self.rob.setTarget(targetRR,0)
        self.rob.setTarget(targetLL,0)
        time.sleep(.5)


    def randomFight(self):
        for i in range(0,20):
            target = int(random.uniform(6,17))
            amount = int(random.uniform(0,10))
            self.rob.setTarget(target,amount)
            self.rob.setTarget(target,amount)



    def reset(self):
        zeroVal = [6,12]
        sizVal = [8,9,10,11,15,16,17]
        for i in range(2):
            target = zeroVal[i]
            self.rob.setTarget(target,0)
        for i in range(7):
            target = sizVal[i]
            self.rob.setTarget(target,6000)
            time.sleep(1)
        for i in range(2):
            target = 7
            target2 = 13
            self.rob.setTarget(target,7000)
            self.rob.setTarget(target2,6000)
        target = 14
        self.rob.setTarget(target,7000)
        body = 0
        head = 3
        head2 = 4
        self.rob.setTarget(body,6000)
        self.rob.setTarget(head,6000)
        self.rob.setTarget(head2,6000)

    def superReset(self):
        headUP = 4
        headLR = 3
        body = 0
        upperRight = 6
        upperLeft = 12
        middleRight = 7
        middleLeft = 13
        self.rob.setTarget(headUP,6000)
        self.rob.setTarget(headLR,6000)
        self.rob.setTarget(body,6000)
        self.rob.setTarget(upperRight,0)
        self.rob.setTarget(upperLeft,0)
        self.rob.setTarget(middleRight,7000)
        self.rob.setTarget(middleLeft,6000)


    def die(self):
        targetUpArmR = 6
        targetUpArmL = 12
        targetout = 13
        targetoutR = 7
        body = 0
        head = 3
        headUp = 4
        for i in range (0,10000):
            self.rob.setTarget(targetUpArmR,9000)
        
        self.rob.setTarget(targetUpArmL,1000)
        self.rob.setTarget(body,6000)
        self.rob.setTarget(head,6000)
        time.sleep(2)
        self.rob.setTarget(targetout,2000)
        self.rob.setTarget(targetoutR,8000)
        self.rob.setTarget(headUp,8000)
        time.sleep(2)
        self.rob.setTarget(targetUpArmR,0)
        self.rob.setTarget(targetUpArmL,0)
        self.rob.setTarget(targetout,6000)
        self.rob.setTarget(targetoutR,7000)
        self.rob.setTarget(head,6000)
        self.rob.setTarget(headUp,4000)
        time.sleep(3)


    def look(self):
        headUD = 4
        headLR = 3

        self.rob.setTarget(headUD,6000)
        self.rob.setTarget(headLR,6000)
        time.sleep(1)
        self.rob.setTarget(headLR,4000)
        time.sleep(2)
        self.rob.setTarget(headLR,8000)
        time.sleep(2)
        self.rob.setTarget(headLR,6000)



    def corn(self):
        target2 = 12
        target3 = 14
        target4 = 15
        target5 = 16
        target6 = 17

        self.rob.setTarget(target2,5000)
        self.rob.setTarget(target3,8000)
        time.sleep(.5)
        self.rob.setTarget(target4,4000)
        self.rob.setTarget(target3,4000)
        time.sleep(.5)
        self.rob.setTarget(target4,8000)
        self.rob.setTarget(target3,8000)
        time.sleep(.5)
        self.rob.setTarget(target4,4000)
        self.rob.setTarget(target3,4000)
        time.sleep(.5)
        self.rob.setTarget(target4,8000)
        self.rob.setTarget(target3,8000)
        time.sleep(.5)
        self.rob.setTarget(target4,4000)
        self.rob.setTarget(target3,4000)
        time.sleep(.5)
        self.rob.setTarget(target4,8000)
        self.rob.setTarget(target3,8000)
        time.sleep(.5)
        self.rob.setTarget(target4,4000)
        self.rob.setTarget(target3,4000)
        time.sleep(.5)




        time.sleep(3)




    def wtf(self):
        target = 6
        self.rob.setTarget(target,2000)
        target = 12
        self.rob.setTarget(target,2000)



    def forward(self):
        target = 1
        self.rob.setTarget(target,5000)
        time.sleep(1)
        self.rob.setTarget(target,6000)

    def backward(self):
        target = 1
        self.rob.setTarget(target,7000)
        time.sleep(1)
        self.rob.setTarget(target,6000)

    def left(self):
        target = 2
        self.rob.setTarget(target,7000)
        time.sleep(2)
        self.rob.setTarget(target,6000)
        target = 1
        self.rob.setTarget(target,5000)
        time.sleep(1)
        self.rob.setTarget(target,6000)

    def right(self):
        target = 2
        self.rob.setTarget(target,5000)
        time.sleep(2)
        self.rob.setTarget(target,6000)
        target = 1
        self.rob.setTarget(target,5000)
        time.sleep(1)
        self.rob.setTarget(target,6000)
 
    def runAway(self):
        target = 2 
        self.rob.setTarget(target,3000)
        time.sleep(5)
        self.rob.setTarget(target,6000)
        target = 1
        self.rob.setTarget(target,5000)
        time.sleep(2)
        self.rob.setTarget(target,6000)


    def think(self):
        target = 12
        self

c = commands()
#c.die()
#c.look()
#c.corn()
#c.reset()
#c.fight()
#c.reset()
#c.wtf()
