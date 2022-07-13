import socket
import threading

user_data = ['admin admin12345']
def TcpServer(conn, addr):
    print("出现新的连接 %s:%s" % addr)
    for i in range(5):
        data = conn.recv(10485760).decode()
        if data not in user_data:
            conn.send(b"Error\n")
            i = i + 1
        else:
            conn.send(b"Welcome\n")
            break
        if i >= 5:
            conn.send(b"Too many mistake!\n")
        conn.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.88.238", 9091))
s.listen(5)
print("等待连接...")
conn, addr = s.accept()
TcpServer(conn, addr)