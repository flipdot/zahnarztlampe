import socket
from time import sleep

UDP_IP = "192.168.3.102"
UDP_PORT = 2390
sleepytime = 0.01
maxbrightness = 255

while True:
    sock = socket.socket(socket.AF_INET,
                 socket.SOCK_DGRAM)
    packet = "%d:%d:%d" % (maxbrightness, maxbrightness, maxbrightness)
    sock.sendto(packet, (UDP_IP, UDP_PORT))
    sleep(sleepytime)
    packet = "0:0:0"
    sock.sendto(packet, (UDP_IP, UDP_PORT))
    sleep(sleepytime)
    sock.close()