from  Utils.srial_comm import SrialComm
import time

if __name__=='__main__':
    sc = SrialComm()
    PORTNAME='COM5'
    sc.open(PORTNAME)
    while(1):
        res,data = sc.recv(5)
        if data[len(data)-4:-1]==":end":
            print(res,data)
        time.sleep(0.1)
