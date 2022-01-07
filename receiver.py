# ---------------------------------------------------------
# Prediction:
#     - UDP Socket Communication
#       ------------------------
#     - Packets receiver handler
#       - - - - - - - - - - - - - -  
#       December /021
#       - - - - - - - - - -
# ---------------------------------------------------------

from socket import socket, AF_INET, SOCK_DGRAM
from sys import argv, stdout
from transmtnVldt import ip_checksum
    # impots essential support libraries

    # pkt info and destination dfn
def send(content, to):
    checksum = ip_checksum(content)
    send_sock.sendto(checksum + content, to)

if __name__ == "__main__":
    dest_addr = argv[1]
    dest_port = int(argv[2])
    dest = (dest_addr, dest_port)
    listen_addr = argv[3]
    listen_port = int(argv[4])
    listen = (listen_addr, listen_port)

    # control sockets dfn
    send_sock = socket(AF_INET, SOCK_DGRAM)
    recv_sock = socket(AF_INET, SOCK_DGRAM)

    # sets socket to listening mode
    recv_sock.bind(listen)

    expecting_seq = 0
    # pkts validation
    while True:
        message, address = recv_sock.recvfrom(4096)

        checksum = message[:2]
        seq = message[2]
        content = message[3:]
        # check pkt repetition 
        if ip_checksum(content) == checksum:
            send("ACK" + seq, dest)
            if seq == str(expecting_seq):
                stdout.write(content)
                expecting_seq = 1 - expecting_seq
        else:
            negative_seq = str(1 - expecting_seq)
            send("ACK" + negative_seq, dest)
