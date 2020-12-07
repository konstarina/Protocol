# Protocol
The protocol stack that should contain three modules: transport, session, and application levels.
### Transport Level
In the transport.transport.py, it is implemented a protocol atop UDP with error checking and retransmission. 
It compares the checksums of the received packets, and if they are equal the packet is acknowledged.
It creates an UDP socket through which our Client and Server will communicate

### Session Level
For ensuring the secure connection and sending and receiving messages securely 

### Application Level
It is not implemented yet fully, because I am stuck with Diffie-Hellman.
