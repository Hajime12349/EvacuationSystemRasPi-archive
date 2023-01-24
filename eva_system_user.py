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
    
    def recvData(self):
        # @check
        # 別スレッドで走らせる必要がありそう。
        sc = SrialComm()
        PORTNAME='COM5'
        sc.open(PORTNAME)
        while(1):
            res, bdata = "test","data".encode()
            res,bdata = sc.recv(5)
            # 末尾が:endかどうか
            if bdata[-10:]==b'3b656e64\r\n':
                # print(res,data)
                bdata = bdata.split()[2]
                data = bytes.fromhex(bdata.decode('utf-8')).decode('shift_jis')
                print(data)
                self.applyData(data)
            time.sleep(0.1)

    
    def applyData(self,data):
        # データの抽出と加工↓
        # test data------------------
        data = "date;type;level;area;detail;end"
        dataList = data.split(";")
        # test data------------------
        
        # @check
        # 文章は要検討（的場に相談）
        title = f"{dataList[3]}で{dataList[1]}が発生！ レベル{dataList[2]}"
        content = f"{dataList[0]}に{dataList[3]}で{dataList[1]}が発生しました。\n危険ですので直ちに避難してください\n詳細は、{dataList[4]}"
        # データの抽出と加工↑
        self.ids.title.text = title
        self.ids.content.text = content
    

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
    SystemInit().run()
