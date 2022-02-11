from socket import *
s = socket()                    # Skapa ett socket-objekt
s.bind(("localhost", 12345))    # ... som körs på den egna datorn på port 12345
s.listen()                      # Vänta på att klient ansluter.
print("Väntar på att en klient ska ansluta till servern...")
conn, addr = s.accept()         # När en klient ansluter
print("En klient anslöt från adressen", addr)
conn.close()