# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import grpc
from protolib import wallet_pb2, wallet_pb2_grpc
import base58
from . import config
_HOST = config.getHost()
_PORT = config.getPort()

from secp256k1 import PrivateKey, PublicKey

conn = grpc.insecure_channel(_HOST + ':' + _PORT)  # 监听频道
client = wallet_pb2_grpc.WalletServiceStub(channel=conn)   # 客户端使用Stub类发送请求,参数为频道,为了绑定链接

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


def getbalance(address):
    account = base58.b58decode(address)
    response = client.CheckBalance(wallet_pb2.CheckBalanceRequest(account=account))   # 返回的结果就是proto中定义的类
    return response

def tx(from_address,to_address,amount,privatekey):
    return true