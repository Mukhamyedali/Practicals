from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_text = StringProperty()

    def build(self):
        self.title = "Miles to Kilometres Converter"
        self.output_text = ''
        return Builder.load_file('convert_miles_km.kv')

    def handle_calculate(self):
        value = self.get_valid_number()
        self.output_text = str(value * MILES_TO_KM)

    def handle_increment(self, change):
        value = self.get_valid_number() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_valid_number(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0
