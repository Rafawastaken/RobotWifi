from kivymd.app import MDApp as App
from kivymd.theming import ThemeManager
from kivymd.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('robot_app.kv')

class RobotAppLayout(Widget):
    pass

class RobotApp(App):
    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"

        return RobotAppLayout()

if __name__ == '__main__':
    RobotApp().run()