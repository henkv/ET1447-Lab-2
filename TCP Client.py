from socket import *
from time import time
from sys import argv


duration = int(argv[1])
package_per_sec = int(argv[2])
targetHost = argv[3]
targetPort = 12000

print("Duration: "    + argv[1] + ", "
    + "Packages/s: "  + argv[2] + ", "
    + "Target: "      + argv[3] + "\n")

client = socket(AF_INET, SOCK_STREAM)
counter = 0
payload = ";" + "".zfill(94)

packageDelay = 1/package_per_sec

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
