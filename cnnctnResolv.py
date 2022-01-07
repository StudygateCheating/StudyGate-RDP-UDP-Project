# ---------------------------------------------------------
# Prediction:
#     - UDP Socket Communication
#       ------------------------
#     - Error detection/retransmission/timeout
#       - - - - - - - - - - - - - - - - - - 
#       December /021
#       - - - - - - - - - -
# ---------------------------------------------------------

from socket import *
import random
import time
    # imports essential support libraries

def usage():
    print "Usage: sender < - - > receiver transmission"
    exit()

    # delay time handler
def timeoutCtl():
    """
    Sleep for a uniformly random amount of time between 80 and 120ms.
    """
    delay = random.random() * 0.02
    sign = random.randint(0, 1)
    if (sign == 1):
        delay = -delay
    delay += 0.1
    time.sleep(delay)

    # Validate pkt status
def corrupt(pkt):
    # corrupt a packet
    index = random.randint(0, len(pkt)-1)
    pkt = pkt[:index] + str(unichr(random.randint(0, 95))) + pkt[index+1:]
    return pkt

    # Drop corrupt pkts
def intercept(pkt, outSock, addr):
    rand = random.randint(1, 20)
    if rand >= 1 and rand <= 5:
        print "Dropped"
        return
    if rand >= 6 and rand <= 10:
        pkt = corrupt(pkt)
        print "Corrupted to:", pkt
    timeoutCtl()
    outSock.sendto(pkt, addr)

from sys import argv
if len(argv) < 5:
    usage()

    # Addresses dfn
fromSenderAddr = ('localhost', int(argv[1]))
toReceiverAddr = ('localhost', int(argv[2]))
fromReceiverAddr = ('localhost', int(argv[3]))
toSenderAddr = ('localhost', int(argv[4]))

    # Sockets dfn
fromSenderSock = socket(AF_INET, SOCK_DGRAM)
fromSenderSock.bind(fromSenderAddr)
fromSenderSock.setblocking(0)
fromReceiverSock = socket(AF_INET, SOCK_DGRAM)
fromReceiverSock.bind(fromReceiverAddr)
fromReceiverSock.setblocking(0)

outSock = socket(AF_INET, SOCK_DGRAM)
    
    # stage pkt waiting session
print "Listening..."
while True:
    try:
        pkt = fromSenderSock.recv(4096)
        print "Received packet from sender:", pkt
        intercept(pkt, outSock, toReceiverAddr)
    except error:
        pass
    try:
        pkt = fromReceiverSock.recv(4096)
        print "Received packet from receiver:", pkt
        intercept(pkt, outSock, toSenderAddr)
    except error:
        pass
