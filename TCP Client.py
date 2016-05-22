from socket import *
from time import time

targetHost = "193.11.185.60"
targetPort = 12000

client = socket(AF_INET, SOCK_STREAM)
counter = 0
payload = ";" + "".zfill(94)

packageDelay = 1/10

duration = 15
now = time()
endTime = now + duration
nextPackageTime = now + packageDelay

client.connect((targetHost, targetPort))

while now < endTime:
    now = time()
    if (now > nextPackageTime):
        message = format(counter, '05') + payload
        client.send(message.encode())
        nextPackageTime = now + packageDelay
        counter += 1
        #print(client.recv(2024).decode())
