import session.session as session


class App:
    def __init__(self, tr, trans_handler, my_public, his_public, private, type):
        self.session = session.Session(tr, trans_handler, my_public, his_public, private, type)

    def send(self, msg):
        self.session.secureSend(msg)

    def recieve(self):
        return self.session.secureRecieve()

    def communicate(self, msg):
        self.session.communicate(msg)