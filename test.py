# ! /usr/bin/env python
# -*- coding: utf-8 -*-
from api import sdk
if __name__ == '__main__':
    print("随机私钥:{0}".format(sdk.randomprivatekey()))
    pub = sdk.getPublicKeyfromPrivateKey("0383fda6fc5877ff4724d6817b5c1095097900dc28729b5bf4eac21d51f45397")
    print("公钥:{0}".format(pub))
    print ("\n")
    print("地址:{0}".format(sdk.getAddressFromPublicKey(pub)))
    balance = sdk.getbalance("RW8VbQPAWpUJH3dtDDJPRaVTudXkgpv8LPAMe1kPTqwCKQ92BTArg9hxpYLwWeeKYzoxt7jdgzXRYtrxJPTDij5Y")
    print ("余额:{0}".format(balance))