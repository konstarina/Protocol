import transport.transport as tr
import application.application
import sys


if __name__ == "__main__":
    server_handler = tr.server_socket("127.0.0.1", int(sys.argv[1]))
    tr.recv(server_handler)
    my_public = 197
    his_public = 151
    my_private = 199

    app = application.App(tr, server_handler, my_public, his_public, my_private, 'server')
    app.communicate()

    msg = "Hello UDP Client!"
    tr.send(server_handler, msg)
    msg = tr.recv(server_handler)
    print(msg)

    tr.send(server_handler, "How are you doing?")
    msg_new = tr.recv(server_handler)
    print(msg_new)


