from socket import *
s = socket()                # Skapa ett socket-objekt
s.connect(("localhost", 12345))     # Anslut till server
