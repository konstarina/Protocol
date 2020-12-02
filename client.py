import protocols.transport as tr
from protocols.session import DHEndpoint
import sys


if __name__ == "__main__":
    trans_handler = tr.socket()
    tr.connect_to(trans_handler, "127.0.0.1", int(sys.argv[1]))

    msg = tr.recv(trans_handler)
    print(msg)

    tr.send(trans_handler, "Hello UDP Server.")
    msg_new = tr.recv(trans_handler)
    print(msg_new)