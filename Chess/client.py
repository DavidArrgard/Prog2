from socket import *
def connect_to_server(): 
    s = socket()
    host = input("Ange serverns IP-adress:")
    port = 12345
    s.connect((host, port))
    return s
def listener_thread(conn):
    while True:
        b = conn.recv(1024)
        msg = b.decode("utf-16")
        print("\n"+msg)
conn = connect_to_server()
from _thread import *
start_new_thread(listener_thread, (conn, ))