# -*- coding: utf-8 -*-

import serial
import time
import threading

"""
シリアル通信クラス
"""
class SrialComm:
    # 初期化
    def __init__(self):
        # シリアルを開く
        # オープンフラグ
        self.isPortOpen = False
        # 受信データ
        self.recvData = bytearray()
        # イベント生成
        self.event = threading.Event()

    # データ受信待ち(タイムアウト付き[sec])
    def recv(self, timeout=3):
        # タイムアウト用時間取得
        time_start = time.time()
        time_end = time_start
        # スレッド待ちイベントクリア
        self.event.clear()
        # 受信データクリア
        self.recvData.clear()
        # 受信結果 True:成功 False:失敗(タイムアウト)
        result = False

        # データ受信待ち
        while not self.event.is_set():
            # タイムアウトチェック
            time_end = time.time()
            if (time_end - time_start > timeout):
                # データ送受信停止して失敗(タイムアウト)とする
                result = False
                self.stop()
                print("timeout:{0}sec".format(timeout))
                break

            # 受信データ読み取り
            buff = self.comm.read()

            # 受信データ判定
            if len(buff) > 0:
                print('receaved')
                # 受信データ追加
                self.recvData.extend(buff)
                # (仮)¥nを受信済なら成功とする
                # print("recvData:",self.recvData)
                if (self.recvData.find(b'\r\n')) >= 0:
                    # データ送受信停止して成功とする
                    result = True
                    self.stop()
                    break

        # 結果を返す
        return (result, self.recvData)

    # データ送信
    def send(self, data):
        if self.isPortOpen:
            self.comm.write(data)
        else:
            print("Not connected")

    # データ送受信停止
    def stop(self):
        self.event.set()

    # シリルポートオープン
    def open(self,PORTNAME):
        tty=PORTNAME
        baud='115200'
        comm=None
        try:
            self.comm = serial.Serial(tty, baud, timeout=0.1)
            self.isPortOpen = True
            print("try")
        except Exception as e:
            self.isPortOpen = False
            print("exc")

        return self.isPortOpen

    # シリアルポートクローズ(明示的に閉じる)
    def close(self):
        self.stop()
        if (self.isPortOpen):
            self.comm.close()
        self.isPortOpen = False

if __name__=='__main__':
    # シリアルを開く
    comm = SrialComm()
    # PORTNAME='COM5'
    # comm.open(PORTNAME, '115200')
    # COMMAND='tcps 2001:db8::34'
    # COMMAND='reset'

    # データ送信
    comm.send('11')
    #comm.send(f"{COMMAND} 11\r\n".encode('utf-8'))
    # comm.send(f"{COMMAND}\r\n".encode('utf-8'))

    # データ受信(タイムアウト=10sec)
    result, data = comm.recv(10)
    print(result)
    print(data)

    # シリアルを閉じる
    comm.close();