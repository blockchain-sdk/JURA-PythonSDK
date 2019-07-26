# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import base58
from secp256k1 import PrivateKey, PublicKey
# 获取随机私钥字符串
def randomprivatekey():
    privateKey = PrivateKey()
    return privateKey.serialize()

# 从私钥字符串得到公钥（bytearray：Uint8Array in javascript）
def getPublicKeyfromPrivateKey(key):
    privateKey = PrivateKey(bytes(bytearray.fromhex(key)), raw=True)
    # pubkey_ser = privateKey.pubkey.serialize()
    pubkey_ser_uncompressed = privateKey.pubkey.serialize(compressed=False)
    return pubkey_ser_uncompressed

# 从公钥得到地址
def getAddressFromPublicKey(pubkey_ser_uncompressed):
    return base58.b58encode(pubkey_ser_uncompressed)

if __name__ == '__main__':
    prikey = randomprivatekey()
    pubkey = getPublicKeyfromPrivateKey(prikey)
    address = getAddressFromPublicKey(pubkey)
    print ("\n\n私钥:{0}\n\n公钥:{1}\n\n地址:{2}".format(prikey,pubkey,address))