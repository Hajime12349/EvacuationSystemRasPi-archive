#import japanize_kivy
from kivy.app import App

from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import japanize_kivy


Builder.load_file('./eva_system_admin.kv')

Window.size=(197*5,110*5)

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # ボタン押下時に呼ばれる
    def on_press_report(self):
        print('report')

    def on_press_history(self):
        print('history')

class ColorLabel(BoxLayout):
    pass

class SystemInit(App):
    def __init__(self, **kwargs):
        super(SystemInit, self).__init__(**kwargs)
        self.title = 'Evacuation System'

    def build(self):
        return MainScreen()






# メインの定義
if __name__ == '__main__':
    SystemInit().run()
