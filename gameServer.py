import socket
import sys
import cmdParser

host = '10.200.1.119'
port = 5000
m = ""
connect = False
send = False

class Server():
    def __init__(self, gui):
        self.gui = gui

    def connect(self):
        global connect
        connect = True

    def send(self, msg):
        global send
        global m
        send = True
        m = msg

    def startUp(self):
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
                        if (m == "listen"):
                            cmdParser.parse_data(reply.decode("UTF-8"))
            
                connect = False

        sock.close()

