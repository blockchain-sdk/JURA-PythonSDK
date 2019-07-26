# JURA-PythonSDK
JURA非官方的pythonSDK


前提：

```
sudo apt install gyp
sudo apt install protobuf-compiler
sudo apt install pandoc
sudo apt install pkg-config
sudo apt install autoconf automake libtool
sudo apt install python3 python3-pip
```

更新 pip3
```
pip3 install --upgrade setuptools
```

如果更新后，pip3不能执行，则进行如下修复：

打开文件
```
sudo nano /usr/bin/pip
```

替换内容
```
from pip._internal import main
```

生成proto的python文件
```
mkdir protolib
cd proto
python3 -m grpc_tools.protoc -I. --python_out=../protolib --grpc_python_out=../protolib ./wallet.proto
python3 -m grpc_tools.protoc -I. --python_out=../protolib --grpc_python_out=../protolib ./common.proto
```

需要安装的库
```
pip3 install grpcio
pip3 install grpcio-tools
pip3 install eth-keys
pip3 install eth-utils
pip3 install base58
pip3 install eth-hash
pip3 install eth-hash[pycryptodome]
pip3 install eth-account
pip3 install secp256k1
```

或直接全部安装
```
pip3 install -r requirements.txt
```


如果缺什么，有纰漏，请安装后执行：

```
pip3 freeze > requirements.txt
```