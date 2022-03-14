import socket, sys, binascii
import des, dh, random
import easygui



t=0
# 读取文件信息
def read_message(filename):
    msg = ""
    with open(filename) as f:
        try:
            for line in f.readlines():
                msg += line
        finally:
            f.close()
    return msg


# 写入文件信息
def write_message(filename, msg):
    try:
        f = open(filename, 'a')
        f.write(msg + '\n')
    finally:
        f.close()


def receiver():
    # 设置接收端端口
    address = ('127.0.0.1', 6666)


    # 建立接收端
    try:
        receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Receiving terminal start!")
    except socket.error as msg:
        print("Socket failed. Error code: " + str(msg[0]) + ", Error message: " + msg[1])
        sys.exit()

    # 绑定监听
    try:
        receiver.bind(address)
        print("Binding port succeed!")
    except socket.error as msg:
        print("Bind failed. Error code: " + str(msg[0]) + ", Error message: " + msg[1])
        sys.exit()

    # 设置连接数为 1
    receiver.listen(1)

    # 接收连接,读取数据
    while True:
        connect, address = receiver.accept()
        data = connect.recv(4096)
        print('\nReceived messages:\n' + data.decode())
        global t
        t='\nReceived messages:\n' + data.decode()
        #easygui.msgbox('\nReceived messages:\n' + data.decode())
        if not data:
            break
        connect.sendall(str(Y2).encode())
        return data.decode()

    # 断开连接
    connect.close()
    receiver.close()


# 接收密文，并解密消息
def main():
    # 获取消息
    global Y2
    Y2 = 0
    p = receiver()
    a = receiver()
    X2 = random.randint(0, int(p) - 1)
    Y2 = dh.get_calculation(int(p), int(a), X2)
    # Y2 = str(Y2).encode('utf-8')
    Y1 = receiver()
    Key = dh.get_key(X2, int(Y1), int(p))
    print('---------------')
    print('X2:', X2)
    print('Y2:', Y2)
    print('Y1', Y1)
    print('Key:', Key)
    Key1 = (str(Key) + 'E') * 2 + (str(Key) + '0') * 2
    print('Key1:', Key1)

    print('---------------')
    n = len(Key1)
    if n < 16:
        Key1 = Key1 + '2' * (16 - n)

    cipher_message = receiver().split(',')
    des_cipher = cipher_message[0]

    #des_key = read_message('des_key.txt')

    title = easygui.msgbox(t + '\n', title="解密", ok_button="解密")
    # 解密密文
    msg = des._DES(des_cipher, Key1, IV=[0x51, 0xA2, 0x6C, 0x32, 0x11, 0xF1, 0xD4, 0x09], temp=1)

    # 将16进制密文转化为ASCII码
    msg = binascii.unhexlify(msg).decode()

    file = open("message2.txt", 'w')
    file.write(str(msg))

    file.close()

    print('\nDecrypted messages: \n' + msg)
    g='\nDecrypted messages: \n' + msg
    #easygui.msgbox('\nDecrypted messages: \n' + msg)
    msg='接收方'
    easygui.msgbox(g,msg)


if __name__ == "__main__":
    main()
