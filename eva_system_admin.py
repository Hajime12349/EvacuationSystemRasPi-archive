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


Builder.load_file('./eva_system_admin.kv')

Window.size=(197*5,110*5)

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
    pass

class CheckScreen(Screen):
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
    SystemInit().run()
