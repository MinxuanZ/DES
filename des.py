

# IP置换表
IP_box = [58, 50, 42, 34, 26, 18, 10, 2,
          60, 52, 44, 36, 28, 20, 12, 4,
          62, 54, 46, 38, 30, 22, 14, 6,
          64, 56, 48, 40, 32, 24, 16, 8,
          57, 49, 41, 33, 25, 17, 9, 1,
          59, 51, 43, 35, 27, 19, 11, 3,
          61, 53, 45, 37, 29, 21, 13, 5,
          63, 55, 47, 39, 31, 23, 15, 7]
# 逆IP置换表
Inv_IP_box = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]
# S盒中的S1盒
S1 = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
      0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
      4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
      15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
# S盒中的S2盒
S2 = [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
      3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
      0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
      13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
# S盒中的S3盒
S3 = [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
      13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
      13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
      1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
# S盒中的S4盒
S4 = [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
      13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
      10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
      3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
# S盒中的S5盒
S5 = [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
      14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
      4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
      11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
# S盒中的S6盒
S6 = [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
      10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
      9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
      4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
# S盒中的S7盒
S7 = [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
      13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
      1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
      6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
# S盒中的S8盒
S8 = [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
      1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
      7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
      2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
# S盒
S_box = [S1, S2, S3, S4, S5, S6, S7, S8]
# 用于对数据进行扩展置换，将32bit数据扩展为48bit
extend_box = [32, 1, 2, 3, 4, 5,
              4, 5, 6, 7, 8, 9,
              8, 9, 10, 11, 12, 13,
              12, 13, 14, 15, 16, 17,
              16, 17, 18, 19, 20, 21,
              20, 21, 22, 23, 24, 25,
              24, 25, 26, 27, 28, 29,
              28, 29, 30, 31, 32, 1]
# P盒
P_box = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25]

# 生成子密钥的置换表1，将64位的密钥转换为56位
key_box1 = [57, 49, 41, 33, 25, 17, 9,
            1, 58, 50, 42, 34, 26, 18,
            10, 2, 59, 51, 43, 35, 27,
            19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15,
            7, 62, 54, 46, 38, 30, 22,
            14, 6, 61, 53, 45, 37, 29,
            21, 13, 5, 28, 20, 12, 4]
# 生成子密钥的置换表2，将56位的密钥转换为48位
key_box2 = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32]


# 将输入ASCII码转化为二进制
# 将10进制数转化为二进制
def _ASCII_to_BitList(data):
    data = [ord(c) for c in data]
    # print(len(data))
    while (len(data) % 8) != 0:
        data.append(32)
    s1 = len(data) * 8
    pos = 0
    result = [0] * s1
    for ch in data:
        i = 7
        while i >= 0:
            if ch & (1 << i) != 0:
                result[pos] = 1
            else:
                result[pos] = 0
            pos += 1
            i -= 1
    return result


# 将二进制数组转换为字符串
# 将二进制转换为10进制
def _BitList_to_ASCII(data):
    result = []
    pos = 0
    s = 0
    while pos < len(data):
        s += data[pos] << (7 - (pos % 8))
        if (pos % 8) == 7:
            result.append(s)
            s = 0
        pos += 1
    return ''.join([chr(c) for c in result])


# lift move elements

def _Leftmove(tmp, step):
    return tmp[step:] + tmp[:step]


# create sub keys
def _Create_Subkeys(Key):
    key_result = []
    key0 = [0 for i in range(56)]

    for i in range(len(key_box1)):
        key0[i] = Key[key_box1[i] - 1]

    for i in range(16):
        key1 = [0 for i in range(48)]

        if (i == 0 or i == 1 or i == 8 or i == 15):
            step = 1
        else:
            step = 2
        tmp1 = key0[0:28]
        tmp2 = key0[28:56]
        tmp1 = _Leftmove(tmp1, step)
        tmp2 = _Leftmove(tmp2, step)
        key0 = tmp1 + tmp2
        for i in range(len(key_box2)):
            key1[i] = key0[key_box2[i] - 1]
        key_result.append(key1)
    return key_result


# IP盒置换，正取0，逆取1
def _IP(txt, op):
    tmp = [0 for i in range(64)]
    if op == 0:
        for i in range(64):
            tmp[i] = txt[IP_box[i] - 1]
        return tmp
    if op == 1:
        for i in range(64):
            tmp[i] = txt[Inv_IP_box[i] - 1]
        return tmp

    # 扩展表，32 to 48


def _Extend(txt):
    tmp = [0 for i in range(48)]
    for i in range(48):
        tmp[i] = txt[extend_box[i] - 1]
    return tmp


def _Int_to_Bit(n):
    tmp = []
    for i in range(4):
        tmp.append(n % 2)
        n = int(n / 2)
    return tmp[::-1]


# S盒， 48 to 32
def _S(txt):
    S_res = [0 for i in range(32)]
    for k in range(8):
        row = 2 * int(txt[k * 6]) + int(txt[k * 6 + 5])
        column = 8 * int(txt[k * 6 + 1]) + 4 * int(txt[k * 6 + 2]) + 2 * int(txt[k * 6 + 3]) + int(txt[k * 6 + 4])
        tmp = S_box[k][row * 16 + column]

        for j in range(4):
            S_res[4 * k + j] = _Int_to_Bit(tmp)[j]
    return S_res


# P盒， 置换
def _P(txt):
    tmp = [0 for i in range(32)]
    for i in range(32):
        tmp[i] = txt[P_box[i] - 1]
    return tmp


# 两个二进制数组异或
def _XOR(bit1, bit2):
    tmp = [0 for i in range(len(bit1))]
    for i in range(len(bit1)):
        tmp[i] = str(int(bit1[i]) ^ int(bit2[i]))
    return tmp


# 16进制转二进制
def _Hex_to_Bin(txt):
    txt = [int(c) for c in txt]
    s1 = len(txt) * 8
    result = [0] * s1
    pos = 0
    for ch in txt:
        i = 7
        while i >= 0:
            if ch & (1 << i) != 0:
                result[pos] = 1
            else:
                result[pos] = 0
            pos += 1
            i -= 1
    return result


# 2进制转16进制
def _Bin_to_Hex(txt):
    result = []
    pos = 0
    s = 0
    while pos < len(txt):
        s += txt[pos] << (7 - (pos % 8))
        if (pos % 8) == 7:
            result.append(s)
            s = 0
        pos += 1
    res = [0 for i in range(8)]
    for i in range(8):
        res[i] = hex(result[i])
    return "".join([i[2:].upper().rjust(2, '0') for i in res])


# 一次加密的过程
def _Encryption(txt, Key):
    # 创建子秘钥序列
    keybit = _Hex_to_Bin(Key)
    keylist = _Create_Subkeys(keybit)
    # 得到 L & R
    txt1 = _IP(txt, 0)
    L = [txt1[i] for i in range(32)]
    R = [txt1[i] for i in range(32, 64)]

    for i in range(16):
        tmp = R
        tmp = _Extend(tmp)
        tmp = _XOR(tmp, keylist[i])
        tmp = _S(tmp)
        tmp = _P(tmp)
        tmp = _XOR(tmp, L)
        L = R
        R = tmp
    L, R = R, L
    res = L
    res.extend(R)
    res = _IP(res, 1)
    return res


# 一次解密过程
def _Decryption(txt, Key):
    keybit = _Hex_to_Bin(Key)
    keylist = _Create_Subkeys(keybit)

    txt1 = _IP(txt, 0)
    L = [txt1[i] for i in range(32)]
    R = [txt1[i] for i in range(32, 64)]

    for i in range(16):
        tmp = R
        tmp = _Extend(tmp)
        tmp = _XOR(tmp, keylist[15 - i])
        tmp = _S(tmp)
        tmp = _P(tmp)
        tmp = _XOR(tmp, L)
        L = R
        R = tmp
    L, R = R, L
    res = L
    res.extend(R)
    res = _IP(res, 1)
    return res


# 总的加密过程
def _DES1(text, Key, IV):
    txt = text
    total = _ASCII_to_BitList(txt)
    res = ''
    # 用于CBC的异或序列
    tmp_xor = _Hex_to_Bin(IV)
    for k in range(len(total) // 64):
        p = _XOR(total[k * 64:(k + 1) * 64], tmp_xor)
        tmp1 = _Encryption(p, Key)
        # 更新CBC的异或序列
        tmp_xor = [int(i) for i in tmp1]
        tmp2 = _Bin_to_Hex([int(i) for i in tmp1])
        res += tmp2
    return res


# 总的解密过程
def _DES2(cipher, Key, IV):
    res2 = ''
    tmp_xor = _Hex_to_Bin(IV)
    for k in range(len(cipher) // 16):
        tmp1 = _Hexstring_to_Bin(cipher[k * 16:(k + 1) * 16])
        tmp2 = _Decryption(tmp1, Key)
        tmp3 = [int(i) for i in tmp2]
        tmp4 = _XOR(tmp3, tmp_xor)
        tmp5 = _BitList_to_ASCII([int(i) for i in tmp4])
        tmp_xor = tmp1
        res2 += tmp5
    return res2


def _Hex_to_Int(txt):
    tmp = [0 for i in range(8)]
    for i in range(8):
        tmp[i] = int(txt[i], 16)
    return tmp


# 哈希字符串转化为二进制数组
def _Hexstring_to_Bin(mm):
    nn = []
    for k in range(8):
        nn.append(mm[2 * k:2 * k + 2])

    nn1 = ['0x' + i for i in nn]
    nn2 = []
    for i in range(8):
        nn2.append(int(nn1[i], 16))

    nn3 = _Hex_to_Bin(nn2)
    return nn3


def _DES(text, key, IV, temp):
    key = _Hexstring_to_Bin(key)
    if temp == 0:
        return _DES1(text, key, IV)
    if temp == 1:
        return _DES2(text, key, IV)