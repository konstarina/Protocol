import transport.transport as tr
import application.application as application
import sys


if __name__ == "__main__":
    s_public = 197
    m_public = 151
    m_private = 157
    trans_handler = tr.socket()
    tr.connect_to(trans_handler, "127.0.0.1", int(sys.argv[1]))

    app = application.App(tr, trans_handler, m_public, s_public, m_private, 'client')
    app.communicate("Hello")
    message = app.communicate()

    msg = tr.recv(trans_handler)
    print(msg)

    tr.send(trans_handler, "Hello UDP Server.")
    msg_new = tr.recv(trans_handler)
    print(msg_new)
