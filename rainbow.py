import socket
from time import sleep

UDP_IP = "192.168.3.102"
UDP_PORT = 2390
sleepytime = 0.02
maxbrightness = 255

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

while True:
    for x in range(0, maxbrightness):
        y = maxbrightness - x
        packet = "%d:%d:0" % (x, y)
        sock.sendto(packet, (UDP_IP, UDP_PORT))
        sleep(sleepytime)

    for x in range(0, maxbrightness):
        y = maxbrightness - x
        packet = "%d:0:%d" % (y, x)
        sock.sendto(packet, (UDP_IP, UDP_PORT))
        sleep(sleepytime)

    for x in range(0, maxbrightness):
        y = maxbrightness - x
        packet = "0:%d:%d" % (x, y)
        sock.sendto(packet, (UDP_IP, UDP_PORT))
        sleep(sleepytime)