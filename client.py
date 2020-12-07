import transport.transport as tr
import application.application as application
import sys


if __name__ == "__main__":
    his_public = 197
    my_public = 151
    my_private = 157
    trans_handler = tr.socket()
    tr.connect_to(trans_handler, "127.0.0.1", int(sys.argv[1]))

    app = application.App(tr, trans_handler, my_public, his_public, my_private, 'client', "message")
    app.communicate("Hello")
    message = app.communicate()

    msg = tr.recv(trans_handler)
    print(msg)

    tr.send(trans_handler, "Hello UDP Server.")
    msg_new = tr.recv(trans_handler)
    print(msg_new)
