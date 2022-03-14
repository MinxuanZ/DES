import socket, os, sys, binascii
import des, dh, random
import easygui
from time import *


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


# 消息发送端程序
def sender(msg):
    # 设置接收端端口
    address = ('localhost', 6666)

    # 建立发送端
    try:
        sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Sending terminal start!')
    except socket.error as error:
        print("Socket failed. Error code: " + str(error[0]) + ", Error message: " + msg[1])
        sys.exit()

    # 建立连接
    try:
        sender.connect(address)
        print("Connect with receiver successful!")
    except socket.error as error:
        print("Socket failed. Error code: " + str(error[0]) + ", Error message: " + msg[1])
        sys.exit()

    # 发送数据
    try:
        sender.sendall(msg)
    except socket.error:
        print('send failed!')
        sys.exit()

    # 接收反馈
    global i
    reply = sender.recv(4096)
    i = reply.decode()
    print(reply.decode())

    # 断开连接
    sender.close()




i = 0
# 加密消息，并发送密文
def main():
    cipher_message = []

    # global i
    p = '353'
    a = '3'
    sender(p.encode())
    sender(a.encode())
    X1 = random.randint(0, int(p) - 1)
    Y1 = dh.get_calculation(int(p), int(a), X1)
    sender(str(Y1).encode(encoding='utf-8'))
    Y2 = i
    Key = dh.get_key(X1, int(Y2), int(p))
    print('----------------')
    print('X1:', X1)
    print('Y1', Y1)
    print('Y2', Y2)
    print('Key:', Key)
    Key1 = (str(Key) + 'E') * 2 + (str(Key) + '0') * 2
    print('Key1:', Key1)
    print('----------------')
    n = len(Key1)
    if n < 16:
        Key1 = Key1 + '2'*(16 - n)
    print('Key1:', Key1)

    # 读取消息，将ASCII码转化为16进制
    #msg = read_message('messages.txt').encode()
    #msg = input('please input messages:').encode()
    msg = easygui.enterbox(msg='请输入消息：',title = '输入框')
    #if msg == NULL:

    #msg = input(" :")
    file = open("message1.txt", 'w')
    file.write(str(msg))

    file.close()

    msg = read_message('message1.txt')
    msg_copy = msg
    binary = str(msg)
    for num in binary:
        res = binary.count(num)
    print('--------')
    print('字节数：', res +1)
    print('--------')
    msg = read_message('message1.txt').encode()

    msg = binascii.hexlify(msg).decode('ascii')
    # des的ECB模式加密消息
    #des_key = read_message('des_key.txt')
    title = easygui.msgbox('Sent messages:\n' + binary, title="加密", ok_button="加密传输")
    begin_time = time()
    des_cipher = des._DES(msg, Key1, IV=[0x51, 0xA2, 0x6C, 0x32, 0x11, 0xF1, 0xD4, 0x09], temp=0)
    cipher_message.append(des_cipher)
    end_time = time()
    run_time = end_time - begin_time
    print('----------------')
    print('run_time:', run_time)
    print('----------------')

    sender(','.join(cipher_message).encode())
    print('\nSent messages:\n' + ','.join(cipher_message))
    s = '\nSent messages:\n' + ','.join(cipher_message)
    msg = '发送方'
    if run_time != 0:
        e=float(res)/float(run_time)
    else:
        e = float(res)/0.000001256

    easygui.msgbox('\nSent cipher_messages:\n' + ','.join(cipher_message)+'\n'+'original messages:\n' +binary + '\n' + 'Efficience:\n'+str(e), msg)


if __name__ == "__main__":
    main()
