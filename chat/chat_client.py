"""
chat client, usage:

 python chat_client.py <host> <port>

Both host and port are optional, defaults: localhost 50005
host must be present if you want to provide port

"""

import select
import socket
import sys

host = 'localhost' 
port = 50005 # different default port than echo, both can run on same server
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port)) 
print 'Connection accepted by (%s,%s)' % (host, port)

input = [s,sys.stdin]
running = True

while running:
    sys.stdout.write('>')
    sys.stdout.flush()
    
    inputready,outputready,exceptready = select.select(input,[],[])
    
    for i in inputready:
        if i == sys.stdin:
            msg = sys.stdin.readline().strip()
            if msg:
                i.send(msg)
            else:
                i.close()
                break
        
        elif i == s:
            data = i.recv(size)
            if not data:
                print 'chat closed'
                running = False
                break
            else:
                sys.stdout.write(data + '\n')
                sys.stdout.flush()