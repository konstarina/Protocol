import transport.transport as tr
import sys


if __name__ == "__main__":
    server_handler = tr.server_socket("127.0.0.1", int(sys.argv[1]))
    # Connected
    tr.recv(server_handler)

    msg = "Hello UDP Client, do the lab!"
    tr.sendto(server_handler, msg)
    msg = tr.recv(server_handler)
    print(msg)

    tr.sendto(server_handler, "Do the freaking lab!")
    msg_new = tr.recv(server_handler)
    print(msg_new)


