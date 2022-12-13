from kivymd.app import MDApp as App
from kivymd.theming import ThemeManager
from kivymd.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
import requests


class RobotAppLayout(Widget):
    def send_comand(self, command:str):
        link = "http://127.0.0.1:5000/robot-com"
        data = {
            "nome":command,
            "estado":True
        }

        r = requests.patch(link, json = data)

class RobotApp(App):
    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"

        return RobotAppLayout()

if __name__ == '__main__':
    Builder.load_file('robot_app.kv')
    Window.size = (500, 700)

    RobotApp().run()