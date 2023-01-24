from  Utils.srial_comm import SrialComm
import time

if __name__=='__main__':
    sc = SrialComm()
    PORTNAME='COM5'
    sc.open(PORTNAME)
    while(1):
        res,bdata = sc.recv(5)
        # data = "date;type;level;area;detail;end".encode()
        if bdata[-10:]==b'3b656e64\r\n':
            # print(res,data)
            bdata = bdata.split()[2]
            data = bdata.decode('utf-8')
            data = bytes.fromhex(data).decode('shift_jis')
            print(data)
        time.sleep(0.1)