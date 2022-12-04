from kivy.app import App
from kivy.uix.label import Label

#GUI画面に”Hello World”と表示する
class HelloWorldApp(App):

    def build(self):
        return Label(text="Hello World")

if __name__=='__main__':
    HelloWorldApp().run()