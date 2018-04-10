import time
import socket
import sys
from Maestro import Controller

part = ''
direction = ''
dur = 0

def parse_data(msg):
    data = msg

    while data != 'end':    
            

            
               
                words = data.split()
                global part
                global direction
                global dur
                # speech syntax
                # start (run go function)
                # move forward for three seconds (move wheels forward for 3 seconds)
                # move back for three seconds (move wheels forward for 3 seconds)
                # turn head left for three seconds (turn head for three seconds)
                # turn body left for three seconds
                while len(words) > 0:

                    word = words.pop(0)
                    print('word:', word)

                    word = word.lower()
                    
                    if (dur == 0):
                        dur = get_number(word)

                    if word == 'forward':
                          direction = 'forward'

                        # if for moving robot back
                    elif word == 'back' or word == 'backward' or word == 'backwards':
                           direction = 'back'

                        # if for turning head/body
                    elif word == 'left' or word == 'right' or word == 'up' or word == 'down' or word == 'center':
                           direction = word

                    elif word == 'head' or word == 'body' or word == 'wheels':
                           part = word

                    elif word == 'move' or word == 'go' or word == 'turn':
                           part = 'wheels'
                            
                    #else:
                    #    print('didn\'t recognize word: ', word)

                    #if ((part != '' and direction != '' and dur != '') or ((part == 'head' or part == 'body') and direction != '')) :
#                          gui.add(part, direction, time)
                    elif word == 'start':                           
                        print("Here is what is recieved and we'll make an element:  "+part +"----"+ direction +"----"+ str(dur))

                        run()
                        word = ''
                        part = ''
                        direction = ''
                        dur = 0
                        data = 'end'




def get_number(number):
        if number == 'one' or number =='1':
            number = 1
        elif number == 'two' or number == '2' or number == 'to':
            number = 2 
        elif number == 'three' or number == '3':
            number = 3 
        elif number == 'four' or number == '4':
            number = 4
        elif number == 'five' or number == '5':
            number = 5
        elif number == 'six' or number == '6':
            number = 6
        else:
            return 0

        return number

def run():
    global part
    global direction
    global dur
    rob = Controller()

    if (part == 'wheels'):
        if (direction == 'forward'):
            rob.setTarget(1, 5000)
        elif (direction == 'back'):
            rob.setTarget(1, 7000)
        elif (direction == 'left'):
            rob.setTarget(2, 7000)
        elif (direction == 'right'):
            rob.setTarget(2, 5000)
        time.sleep(dur)
        rob.setTarget(1, 6000)
        rob.setTarget(2, 6000)

    elif (part == 'head'):
        if (direction == 'up'):
            rob.setTarget(4, 7500)
        elif (direction ==  'down'):
            rob.setTarget(4, 4500)
        elif (direction == 'left'):
            rob.setTarget(3, 7500)
        elif (direction == 'right'):
            rob.setTarget(3, 4500)
        elif (direction == 'center'):
            rob.setTarget(4, 6000)
            rob.setTarget(3, 6000)

    elif (part == 'body'):
        if (direction == 'left'):
            rob.setTarget(0, 7500)
        elif (direction == 'right'):
            rob.setTarget(0, 4500)
        elif (direction == 'center'):
            rob.setTarget(0, 6000)

    time.sleep(1)


  


