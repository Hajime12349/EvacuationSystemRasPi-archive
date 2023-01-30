import japanize_kivy
from kivy.app import App

from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen,NoTransition
from kivy.uix.button import Button
from kivy.graphics import Color,RoundedRectangle
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.dropdown import DropDown
from Utils.srial_comm import SrialComm
import time


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_press_recvData(self):
        # @check
        # 別スレッドで走らせる必要がありそう。
        sc = SrialComm()
        PORTNAME='/dev/ttyUSB0'
        # ms = MenuScreen()
        sc.open(PORTNAME)
        # COMMAND='tcps 2001:db8::34'
        # contents = 'date;type;level;area;detail;end'.encode('shift_jis').hex()
        # res, bdata = "test",f"{COMMAND} {contents}\r\n".encode('utf-8')
        while(1):
            res, bdata = sc.recv(5)
            # 末尾が:endかどうか
            if bdata[-10:]==b'3b656e64\r\n':
                # print(res,data)
                bdata = bdata.split()[2]
                print(bdata)
                data = bytes.fromhex(bdata.decode('utf-8')).decode('shift_jis')
                print(data)
                self.applyData(data)
                break
            time.sleep(0.1)

    def applyData(self,data):
        # データの抽出と加工↓
        # test data------------------
        # data = "date;type;level;area;detail;end"
        dataList = data.split(";")
        # test data------------------

        # @check
        # 文章は要検討（的場に相談）
        # レベルによってメッセージ変えるみたいなの，一応思いついたので書いただけです
        cautionMes=["","逃げる準備をしながら，新しい情報に注意して!","逃げる準備を始めてね!","逃げれそうなら逃げて!","とても危険だから逃げて!","今すぐ安全なところへ逃げて!!"]

        title_content = f"{dataList[3]}で{dataList[1]}が起きてます！ レベル：{dataList[2]}"
        #content_content = f"{dataList[0]}に{dataList[3]}で{dataList[1]}が発生しました。\nとても危険だから逃げて!\n詳細や追加情報\n{dataList[4]}"
        content_content = f"{dataList[0]}に{dataList[3]}で{dataList[1]}が発生しました。\n\n{cautionMes[dataList[2]]}\n\n詳細や追加情報\n\n{dataList[4]}"

        # title_content = f"{dataList[3]}で{dataList[1]}が発生！ レベル{dataList[2]}"
        # content_content = f"{dataList[0]}に{dataList[3]}で{dataList[1]}が発生しました。\n危険ですので直ちに避難してください\n詳細は、{dataList[4]}"
        # データの抽出と加工↑
        self.ids['title'].text = title_content
        self.ids['content'].text = content_content


class UserHistoryScreen(Screen):
    pass

class ColorLabel(BoxLayout):
    pass


class SystemInit(App):
    def __init__(self, **kwargs):
        super(SystemInit, self).__init__(**kwargs)
        # @check
        # 何も考えてなかったけど変えた方がいいかも
        self.title = 'Evacuation System'


    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(UserHistoryScreen(name='userHistory'))
        return sm


# メインの定義
if __name__ == '__main__':
    Builder.load_file('./eva_system_user.kv')
    Window.size=(197*5,110*5)
    Window.fullscreen = True
    # マルチスレッドで実行
    # t = threading.Thread(target=recvData,args=())
    # main_t = threading.Thread(target=SystemInit().run,args=())
    # t.start()
    # main_t.start()
    # t.join()
    # main_t.join()
    # print(threading.current_thread().name)
    SystemInit().run()
