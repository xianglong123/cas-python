from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
import base64
import subprocess


class SM4Utils:

    def __init__(self, ):
        pass

    # 加密方法
    def encryptData_ECB(self, plain_text):
        # 创建 SM4对象
        crypt_sm4 = CryptSM4()
        # 定义key值
        secret_key = bytes().fromhex('0e00bca58b4b9243e0550dd9d22ff700')
        # print("key: ", secret_key)

        # 设置key
        crypt_sm4.set_key(secret_key, SM4_ENCRYPT)

        # 调用加密方法加密(十六进制的bytes类型)
        encrypt_value = crypt_sm4.crypt_ecb(plain_text)
        # print("encrypt_value: ", encrypt_value)

        # 用base64.b64encode转码（编码后的bytes）
        cipher_text = base64.b64encode(encrypt_value)

        # print("加密后：", cipher_text)
        # print(cipher_text.decode('utf-8', 'ignore'))
        # 返回加密后的字符串
        return cipher_text.decode('utf-8', 'ignore')

    def decryptData_ECB(self, cipher_text):
        crypt_sm4 = CryptSM4()
        secret_key = bytes().fromhex('0e00bca58b4b9243e0550dd9d22ff700')
        crypt_sm4.set_key(secret_key, SM4_DECRYPT)
        # 将转入参数base64.b64decode解码成十六进制的bytes类型
        byt_cipher_text = base64.b64decode(cipher_text)
        # 调用加密方法解密，解密后为bytes类型
        decrypt_value = crypt_sm4.crypt_ecb(byt_cipher_text)
        return decrypt_value.decode('utf-8', 'ignore')


# 实现拷贝
def copy(text):
    p = subprocess.Popen(["pbcopy", "w"], stdin=subprocess.PIPE, close_fds=True)
    # 将内容(text)拷贝起来
    p.communicate(input=text.encode("utf-8"))


# 实现粘贴
def paste():
    p = subprocess.Popen(["pbpaste", "r"], stdout=subprocess.PIPE, close_fds=True)
    stdout, stderr = p.communicate()
    # 返回粘贴内容
    return stdout.decode("utf-8")


if __name__ == '__main__':
    SM4_Utils = SM4Utils()
    print("规则：长度11加密，非11解密")
    date = input("输入数据[明文/密文]：")
    if len(date) == 11:
        ecb = SM4_Utils.encryptData_ECB(date.encode("utf-8"))
        copy(ecb)
        print(ecb)
        print('已自动复制至粘贴板')
    else:
        print(SM4_Utils.decryptData_ECB(date.encode("utf-8")))
