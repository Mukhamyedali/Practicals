from kivy.app import App
from kivy.lang import Builder


class SquaringApp(App):
    def build(self):
        self.title = "Squaring Numbers"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_square(self):
        try:
            value = int(self.root.ids.input_number.text)
            self.root.ids.output_label.text = str(value ** 2)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"
