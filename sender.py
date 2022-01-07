# ---------------------------------------------------------
# Prediction:
#     - UDP Socket Communication
#       ------------------------
#     - Packets transmission handler
#       - - - - - - - - - - - - - -  
#       December /021
#       - - - - - - - - - -
# ---------------------------------------------------------

from socket import socket, AF_INET, SOCK_DGRAM, timeout
from sys import argv
from transmtnVldt import ip_checksum
    # impots essential support libraries

SEGMENT_SIZE = 100
    # dfn pkt segment size

if __name__ == "__main__":
    dest_addr = argv[1]
    dest_port = int(argv[2])
    dest = (dest_addr, dest_port)
    listen_addr = argv[3]
    listen_port = int(argv[4])
    listen = (listen_addr, listen_port)
    filename = argv[5]
        # control variables dfn

    with open(filename) as f:
        content = f.read()
        # reads file info

    send_sock = socket(AF_INET, SOCK_DGRAM)
    recv_sock = socket(AF_INET, SOCK_DGRAM)
        # socket objects dfn

    recv_sock.bind(listen)
    recv_sock.settimeout(1)
        # sockets tim control dfn

    offset = 0
    seq = 0
        # control variable initial states

        # sende-receiver notiication states control
    while offset < len(content):
        if offset + SEGMENT_SIZE > len(content):
            segment = content[offset:]
        else:
            segment = content[offset:offset + SEGMENT_SIZE]
        offset += SEGMENT_SIZE

        ack_received = False
            # ACK initial state

            # ACK/timeout states control
        while not ack_received:
            send_sock.sendto(ip_checksum(segment) + str(seq) + segment, dest)

            try:
                message, address = recv_sock.recvfrom(4096)
            except timeout:
                print ("Timeout")
            else:
                print (message)
                checksum = message[:2]
                ack_seq = message[5]
                if ip_checksum(message[2:]) == checksum and ack_seq == str(seq):
                    ack_received = True

        seq = 1 - seq
