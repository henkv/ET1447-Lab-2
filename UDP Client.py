from socket import *
from time import time

targetHost = "1.1.1.2"
targetPort = 12000

client = socket(AF_INET, SOCK_DGRAM)
counter = 0
payload = ";" + "".zfill(94)

packageDelay = 1/50

duration = 15
now = time()
endTime = now + duration
nextPackageTime = now + packageDelay

while now < endTime:
    now = time()
    if (now > nextPackageTime):
        message = format(counter, '05') + payload
        client.sendto(message.encode(), (targetHost, targetPort))
        nextPackageTime = now + packageDelay
        counter += 1
