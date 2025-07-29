from kivy.app import App
from kivy.lang import Builder

class SimpleApp(App):
    def build(self):
        self.title = "Kivy Demo"
        return Builder.load_file('kivy_layout.kv')

SimpleApp().run()
