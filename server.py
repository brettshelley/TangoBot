import socket
import sys

host = '10.200.84.87'
port = 5001
m = ""

def __main__():
    connect()
    send()
    startUp()

def connect():
    global connect
    connect = True

def send(msg):
    global send
    send = True
    m = msg

def startUp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ('Socket Created')
    try:
        sock.bind((host, port))
    except socket.error as err:
        print ("Did not connect" + str(err[0]) + err[1])
        sys.exit
    print ("Socket was built!")

    sock.listen(10)
    print ("I'm listening for you!")
    while 1:
        global connect
        if (connect):
            conn, addr = sock.accept()
            print ('Connect with' + addr[0] + ':' + str(addr[1]))
            
            global send
            global m
            if (send == True):
                conn.send(bytes(m + "\n", "UTF-8"))
                send = False
            else:
                conn.send(bytes("\n", "UTF-8"))
            
            reply = ""
            while (reply == ""):
                reply = conn.recv(1024)
                if (reply != ""):
                    reply = reply + conn.recv(1024)
                    print (reply)
            
            connect = False

    sock.close()

__main__()
