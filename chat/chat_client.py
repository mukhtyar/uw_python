"""
chat client, usage:

 python chat_client.py <host> <port>

Both host and port are optional, defaults: localhost 50005
host must be present if you want to provide port

"""

import select
import socket
import sys
import time
import datetime

host = 'localhost' 
port = 50005 # different default port than echo, both can run on same server
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

server = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
server.connect((host,port)) 
print 'Connection accepted by chat server (%s,%s)' % (host, port)
#sys.stdout.write('> ')
#sys.stdout.flush() # force print of line without \n

timeout = 60 #seconds
input = [server,sys.stdin]
running = True

while running:
    sys.stdout.write('>')
    sys.stdout.flush()
    
    inputready,outputready,exceptready = select.select(input,[],[],timeout)
    
    # timeout
    if not inputready:  
        # could do periodic housekeeping here
        print 'chat client running at %s' % datetime.datetime.now()
    
    for s in inputready:
        
        if s == sys.stdin:
            #handle standard input
            msg = sys.stdin.readline().strip('\n')
            if msg:
                server.send(msg)
            else:
                server.close()
                running = False
        
        elif s:
            data = server.recv(size)
            sys.stdout.write(data + '\n')
            sys.stdout.flush()