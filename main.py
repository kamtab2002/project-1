from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class HelloWorldApp(App):
    def build(self):
        return HelloWorldLayout()


class HelloWorldLayout(BoxLayout):
    pass


if __name__ == "__main__":
    HelloWorldApp().run()
