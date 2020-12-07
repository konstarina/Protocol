class DiffieHellman(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = self.public_key1 ** self.private_key
        partial_key = partial_key % self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = partial_key_r ** self.private_key
        full_key = full_key % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, msg):
        encrypted_msg = ""
        key = self.full_key
        for c in msg:
            encrypted_msg += chr(ord(c) + key)
        return encrypted_msg

    def decrypt_message(self, encrypted_msg):
        decrypted_msg = ""
        key = self.full_key
        for c in encrypted_msg:
            decrypted_msg += chr(ord(c) - key)
        return encrypted_msg


class Session:
    def __init__(self, tr, trans_handler, my_public, his_public, private, type, msg):
        self.encrypted = self.create.encrypt_message(msg)
        self.message = self.create.decrypt_message(self.tr.recv(self.trans_handler))
        self.msg = msg
        self.tr = tr
        self.trans_handler = trans_handler
        self.my_public = my_public
        self.private = private
        self.create = DiffieHellman(my_public, his_public, private)
        self.partial = self.create.generate_partial_key()
        self.tr.send(self.trans_handler, str(self.partial))
        self.his_partial = int(self.tr.recv(self.trans_handler))
        self.full = self.create.generate_full_key(self.his_partial)
        self.type = type

    def communicate(self, msg):
        if self.type == 'client':
            self.secureSend(msg)
            response = self.secureReceive()
            return response
        else:
            response = self.secureRecieve()
            self.secureSend(msg)
            return response


    def secureSend(self, msg):
        self.tr.send(self.trans_handler, msg)

    def secureRecieve(self):
        return self.message




