import hashlib
import socket as skt
import json

bufferSize = 1024


class Socket:
    def __init__(self, sock):
        self.sock = sock
        self.to_addr = None


def socket():
    return Socket(skt.socket(skt.AF_INET, skt.SOCK_DGRAM))


def server_socket(localIP, localPort):
    sock = socket()
    sock.sock.bind((localIP, localPort))
    return sock


def connect_to(sock, localIP, localPort):
    sock.to_addr = (localIP, localPort)
    send(sock, "Connected")
    print("Connected on " + str(localIP) + ":" + str(localPort))
    return sock


def make_packet(msg):
    return json.dumps({"cksm": hashlib.md5(msg.encode("utf-8")).hexdigest(), "payload": msg}).encode("utf-8")


def valid(des_packet):
    return des_packet["cksm"] == hashlib.md5(des_packet["payload"].encode("utf-8")).hexdigest()


def send(sock, msg):
    sock.sock.sendto(make_packet(msg), sock.to_addr)
    data, addr = sock.sock.recvfrom(bufferSize)
    packet = json.loads(data.decode("utf-8"))

    while packet["payload"] == "nack":
        sock.sock.sendto(make_packet(msg), sock.to_addr)
        [data, addr] = sock.sock.recvfrom(bufferSize)


def recv(sock):
    while True:
        data, addr = sock.sock.recvfrom(bufferSize)
        packet = json.loads(data.decode("utf-8"))

        if valid(packet):
            # print("The packet is acknowledged.")
            sock.sock.sendto(make_packet("ack"), addr)
            if packet["payload"] == "Connected":
                sock.to_addr = addr
                print("Connected!")
                return
            else:
                return packet["payload"]
        else:
            print("The packet is not acknowledged.")
            sock.sock.sendto(make_packet("nack"), addr)
