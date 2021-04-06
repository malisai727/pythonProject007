import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5

def rsaEncrypt(msg):
    key = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE\nO3F7gs' \
          '+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr\ntuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU' \
          '7z8uF6Gx+blEMGo8Dg+S\nkKlZFc8Br7SHtbL2tQIDAQAB\n-----END PUBLIC KEY-----\n'
    publickey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(publickey)
    #分段加密
    cipher_text= []
    for i in range(0,len(msg),80):
        cont = msg[i:i+80]
        cipher_text.append(cipher.encrypt(cont.encode()))
    #base64进行编码
    cipher_text = b''.join(cipher_text)
    cipher_result = base64.b64encode(cipher_text)
    #返回密文
    return cipher_result.decode()

if __name__ == '__main__':
    pwd = '123qwe'
    en_msg = rsaEncrypt(pwd)
    print(en_msg)