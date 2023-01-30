#import japanize_kivy
import datetime

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
from kivy.resources import resource_add_path
from kivy.core.text import LabelBase, DEFAULT_FONT

from Utils.srial_comm import SrialComm


def generate_send_data(
    date_str:str,
    type_num:int,
    level_num:int,
    area_num:int,
    detail:str
    ):

    #ser=srial.Serial()
    send_data_str=f'{date_str};{type_num};{level_num};{area_num};{detail};end'
    #send_data_bin=send_data_str.encode('shift_jis')
    #ser.write(send_data_bin)
    return send_data_str

# global title_content
# global content_content
# title_content=""
# content_content=""
class preview(object):
    def __init__(self,title):
        self.title = ""
        # self.content = content
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # # ボタン押下時に呼ばれる
    # def on_press_report(self):
    #     print('report')

    # def on_press_history(self):
    #     print('history')

send_data=''

class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        dt_now = datetime.datetime.now()
        str_date=dt_now.strftime('%Y/%m/%d')
        str_time=dt_now.strftime('%H:%M')
        self.ids['date'].text=str_date
        self.ids['time'].text=str_time

    def on_press_confirm(self):
        global send_data
        send_data=generate_send_data(
        self.ids['date'].text+' '+self.ids['time'].text,
        self.ids['type'].text,
        self.ids['level'].text,
        self.ids['area'].text,
        self.ids['rmarks'].text)
        # self.send_data=generate_send_data(
        # self.ids['date'].text+' '+self.ids['time'].text,
        # self.ids['type'].text,
        # self.ids['level'].text,
        # self.ids['area'].text,
        # self.ids['rmarks'].text)
        # print(self.send_data)
        #print(send_data)
        global title_content
        global content_content
        # プレビュー用のデータに加工
        cautionMes=["","逃げる準備をしながら，新しい情報に注意して!","逃げる準備を始めてね!","逃げれそうなら逃げて!","とても危険だから逃げて!","今すぐ安全なところへ逃げて!!"]
        dataList = send_data.split(";")
        level = self.get_level_num(dataList[2])
        title_content = f"{dataList[3]}で{dataList[1]}が起きてます！ レベル：{dataList[2]}"
        content_content = f"{dataList[0]}に{dataList[3]}で{dataList[1]}が発生しました。\n\n{cautionMes[level]}\n\n詳細や追加情報\n\n{dataList[4]}"
        
        self.manager.get_screen('check').ids['title'].text = title_content
        self.manager.get_screen('check').ids['content'].text = content_content
        
    def get_data(self):
        return self.send_data
    
    def get_level_num(self,level_str):
        level_table= ['危険なし','早期注意情報','警戒レベル2','警戒レベル3','警戒レベル4','警戒レベル5']
        return level_table.index(level_str)
        



class CheckScreen(Screen):
    
    def on_press_send(self):
        # input=InputScreen()
        # print(input.get_data())
        #send_data=input.get_data().encode('shift_jis').hex()
        global send_data
        print(send_data)

        send_data=send_data.encode('shift_jis').hex()

        srial=SrialComm()
        PORTNAME = 'COM5'
        srial.open(PORTNAME)
        COMMAND='tcps 2001:db8::34'
        srial.send(f"{COMMAND} {send_data}\r\n".encode('utf-8'))
        print('end of sending')



class ResultScreen(Screen):
    pass

class HistoryScreen(Screen):
    pass

class ColorLabel(BoxLayout):
    pass

class CustomSpinner(Spinner):
    pass
    # saved_value=''
    def on_press_spinner(self):
        pass
    #     if(self.is_list_open):
    #         self.is_list_open=False
    #     else:

class SpinnerOption(Button):
    pass







pre = preview('')


class SystemInit(App):
    def __init__(self, **kwargs):
        super(SystemInit, self).__init__(**kwargs)
        self.title = 'Evacuation System'

    def build(self):
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(CheckScreen(name='check'))
        sm.add_widget(ResultScreen(name='result'))
        sm.add_widget(HistoryScreen(name='history'))
        return sm






# メインの定義
if __name__ == '__main__':
    Builder.load_file('./eva_system_admin.kv')
    resource_add_path('./Utils/BIZ_UDPGothic')
    LabelBase.register(DEFAULT_FONT, 'BIZUDPGothic-Regular.ttf')
    #Window.size=(197*5,110*5)
    Window.size=(1920,1080)
    Window.fullscreen = True
    SystemInit().run()
