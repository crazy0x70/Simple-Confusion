from CoreCode import features as modules
from argparse import ArgumentParser, FileType
import random

def main(src,dst,func,key):
    if not key:
        key = random.randint(1,200)
    content = src.read()
    out = getattr(modules,func)(content,key)
    if isinstance(out,str):
        with open(dst,"w+") as file:
            file.write(out)
    elif isinstance(out,bytes):
        with open(dst,"wb+") as file:
            file.write(out)
    print("[*] xor key: %s" % key)

if __name__ == '__main__':
    parser = ArgumentParser(prog="confuse tools",description="payload 混淆 \t > By: 渔夫 Email：ace.queen.p@gmail.com")
    parser.add_argument("-s",'--src',help="需要混淆的文件",type=FileType('rb'),required=True)
    parser.add_argument('-d', '--dst', help='完成后输出的文件名', type=str, required=True)
    parser.add_argument('-f', '--func', help='需要使用混淆的func', type=str, required=True)
    parser.add_argument('-k', '--key', help='指定XOR异或混淆的Key 默认随机生成', type=int, required=False)
    args = parser.parse_args()
    main(src=args.src,dst=args.dst,func=args.func,key=args.key)
    print("[+] 混淆完成")
