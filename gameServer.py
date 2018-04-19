import socket
import sys
import gameCmds

class Server():
    
    host = "10.200.1.119"
    port = 5000
    m = ""
    connect = False
    send = False

    def __init__(self, g):
        self.game = g

    def send(self, msg):i
        self.connect = True
        self.send = True
        self.m = msg + "  "

    def startUp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ('Socket Created')
        try:
            sock.bind((self.host, self.port))
        except socket.error as err:
            print ("Did not connect" + str(err[0]) + err[1])
            sys.exit
        print ("Socket was built!")

        sock.listen(10)
        print ("I'm listening for you!")
        while 1:
            if (self.connect):
                conn, addr = sock.accept()
                print ('Connect with' + addr[0] + ':' + str(addr[1]))
            
                if (send == True):
                    conn.send(bytes(self.m + "\n", "UTF-8"))
                    self.send = False
                else:
                    conn.send(bytes("\n", "UTF-8"))
            
                reply = ""
                while (reply == ""):
                    reply = conn.recv(1024)
                    if (reply != ""):
                        reply = reply + conn.recv(1024)
                        print (reply)
                        if (m == "listen"):
                            self.game.move(reply.decode("UTF-8"))
            
                self.connect = False

        sock.close()

