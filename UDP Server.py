from socket import *
from time import time

serverPort = 12000

server = socket(AF_INET, SOCK_DGRAM)
server.bind(('', serverPort))
print("listening on port {}".format(serverPort))

now = time()
lastId = -1
lastTime = now
timeDelta = 0
avrgDelta = 0
packetsOutOfOrder = 0

while 1:
    message = server.recv(2048)
    now = time()
    thisId = int(message.decode()[:5])
    if thisId != lastId + 1:
        packetsOutOfOrder += 1
        print("out of order: was {} expected {}"
              .format(thisId, lastId + 1))

    timeDelta = now - lastTime
    avrgDelta = (avrgDelta + timeDelta) / 2
    lastTime = now
    lastId = thisId

    print("OOO: {}, {:.1f}hz".format( packetsOutOfOrder, 1 / avrgDelta))
