from ast import Num
from cProfile import label
import socket
import threading
import time
import datetime

def Tcpbind():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.88.238", 9000))

def TcpServer(conn, addr):
    print("Have new accept %s:%s" % addr)
    while True:
        data = conn.recv(10485760).decode()
        Str = data[:3]
        num = data[:4]
        if Str == 'True':
            if num < 235:
                conn.send(b'.')
                now_h = datetime.datetime.now().strftime('%H')
                now_m = datetime.datetime.now().strftime('%M')
                now_s = datetime.datetime.now().strftime('%S')
                print("WarningValue:",num," Have People! Time: ",now_h,':',now_m,':',now_s,'\n')   
        else:
            if data == '  ':
                break                                                                                                            
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.88.238", 9000))
s.listen(5)
print("Waiting...")
while True:
    try:
        conn, addr = s.accept()
        TcpServer(conn, addr)
        conn.shutdown(2)
    except KeyboardInterrupt:
        print("\nOver!")
        conn.close()
        break
s.close()
