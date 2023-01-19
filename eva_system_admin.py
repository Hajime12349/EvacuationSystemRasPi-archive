import serial

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


def generate_send_data(
    date_str:str,
    type_num:int,
    level_num:int,
    area_num:int,
    detail:str
    ):

    ser=serial.Serial()
    send_data_str=f'{date_str} {type_num} {level_num} {area_num} {detail}'
    send_data_bin=send_data_str.encode('shift_jis')
    ser.write(send_data_bin)


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # # ボタン押下時に呼ばれる
    # def on_press_report(self):
    #     print('report')

    # def on_press_history(self):
    #     print('history')

class InputScreen(Screen):
    def on_press_confirm(self):
        print('conf')

class CheckScreen(Screen):
    def on_press_send(self):
        print('com')
    pass

class ResultScreen(Screen):
    pass

class HistoryScreen(Screen):
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
        sm.add_widget(InputScreen(name='input'))
        sm.add_widget(CheckScreen(name='check'))
        sm.add_widget(ResultScreen(name='result'))
        sm.add_widget(HistoryScreen(name='history'))
        return sm






# メインの定義
if __name__ == '__main__':
    Builder.load_file('./eva_system_admin.kv')
    Window.size=(197*5,110*5)
    SystemInit().run()
