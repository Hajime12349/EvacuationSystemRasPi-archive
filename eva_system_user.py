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
        # 別スレッドで走らせる必要がありそう。
        # sc = SrialComm()
        # PORTNAME='COM5'
        # sc.open(PORTNAME)
        while(1):
            res, data = "test","data"
            # res,data = sc.recv(5)
            # 末尾が:endかどうか
            print(res,data)
            # @check
            # :endはバイナリでくるからそっちで判定
            if data[-4:]==":end":
                # @check
                # ここで復元する
                print(res,data)
            time.sleep(0.1)

    
    def applyData(self):
        # データの抽出と加工↓
        # data = function()
        data = "date:type:level:area:detail:end"
        dataList = data.split(":")
        # 文章は要検討（的場に相談）
        title = f"{dataList[3]}で{dataList[1]}が発生！ レベル{dataList[2]}"
        content = f"{dataList[0]}に{dataList[3]}で{dataList[1]}が発生しました。\n危険ですので直ちに避難してください\n{dataList[4]}"
        # データの抽出と加工↑
        self.ids.title.text = ''
        self.ids.content.text = ''
    

class UserHistoryScreen(Screen):
    pass

class ColorLabel(BoxLayout):
    pass


class SystemInit(App):
    def __init__(self, **kwargs):
        super(SystemInit, self).__init__(**kwargs)
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
