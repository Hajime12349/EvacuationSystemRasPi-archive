from  Utils.srial_comm import SrialComm
import time

if __name__=='__main__':
    sc = SrialComm()
    PORTNAME='COM5'
    sc.open(PORTNAME)
    while(1):
        # res,data = sc.recv(5)
        data = "date;type;level;area;detail;end".encode()
        # 末尾が:endかどうか バイナリで判別する必要があるか検証
        if data[-4:]==";end".encode():
        # if data.hex()[-8:]=='3b656e64':
            # print(res,data)
            data = data.decode().split(';')
            print(data)
            break
        time.sleep(0.1)
