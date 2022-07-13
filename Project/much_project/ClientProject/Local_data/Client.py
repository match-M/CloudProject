import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.88.238",9000))



def TcpClient(user_name, user_password):
    for n in range(5):
        user_data = user_name+' '+user_password
        s.send(user_data.encode())
        Data = s.recv(10485760).decode()
        if Data == 'Welcome':
                break
 
        return Data


print("  登入")
for i in range(5):
    user_name = input("用户名：")
    user_password = input("密码：")

    server_data = TcpClient(user_name,user_password)
    print(server_data)
    i = i + 1
    if server_data == 'Welcome':
            break
if i >= 5:
        Data = s.recv(10485760).decode()
        print(Data)
s.close()