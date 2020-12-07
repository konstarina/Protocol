# Protocol
The protocol stack that should contain three modules: transport, session, and application levels.
### Transport Level
In the transport.transport.py, it is implemented a protocol atop UDP with error checking and retransmission. 
It compares the checksums of the received packets, and if they are equal the packet is acknowledged.
It creates an UDP socket through which our Client and Server will communicate
```python
def make_packet(msg):
    return json.dumps({"cksm": hashlib.md5(msg.encode("utf-8")).hexdigest(), "payload": msg}).encode("utf-8")


def valid(des_packet):
    return des_packet["cksm"] == hashlib.md5(des_packet["payload"].encode("utf-8")).hexdigest()

```

### Session Level
For ensuring the secure connection and sending and receiving messages in the session 
level were implemented functions secureSend() and secureReceive()  
```python
 def communicate(self, msg):
        if self.type == 'client': # firstly the client sends the message to the server
            self.secureSend(msg)
            response = self.secureReceive()
            return response
        else: 
        # and if self.type == 'server' -> server receives the message from the client
            response = self.secureRecieve()
            self.secureSend(msg)
            return response


    def secureSend(self, msg):
        self.encrypted = self.create.encrypt_message(msg)
        self.tr.send(self.trans_handler, msg)

    def secureRecieve(self):
        self.message = self.create.decrypt_message(self.tr.recv(self.trans_handler))
        return self.message
```
### Application Level
At application level  I chose the option to make a protocol based on the workings
 (state machine) of a stationary telephone, which are implemented (still in progress) in the class App:
 
 ```python
class App:
    def __init__(self, tr, trans_handler, my_public, his_public, private, type, msg):
        self.session = session.Session(tr, trans_handler, my_public, his_public, private, type, msg)

    def send(self, msg):
        self.session.secureSend(msg)

    def recieve(self):
        return self.session.secureRecieve()

    def communicate(self, msg):
        self.session.communicate(msg)

```
It 
