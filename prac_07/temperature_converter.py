from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout

class TemperatureConverter(App):

    def build(self):
        Window.size = (500, 500)
        self.title = "Temperature Converter"
        self.root = Builder.load_file("temp_converter.kv")
        return self.root

    def convert_fahrenheit_to_celsius(self, fahrenheit):
        """Convert fahrenheit to celsius from parameter"""
        celsius = 5 / 9 * (fahrenheit - 32)
        return celsius
        # return "Result: {:.2f} C".format(celsius)

    def convert_celsius_to_fahrenheit(self, celsius):
        """Convert celsius to fahrenheit from parameter"""
        fahrenheit = celsius * 9.0 / 5 + 32
        return fahrenheit
        # return "Result: {:.2f} F".format(fahrenheit)

    def handle_increment(self, n):
        if self.validate_text_input():
            value = int(self.root.ids.text_input.text)
            value += n
            self.root.ids.text_input.text = str(value)

    def handle_conversion(self):
        if self.validate_text_input():
            fahrenheit = int(self.root.ids.text_input.text)
            celsius = self.convert_fahrenheit_to_celsius(fahrenheit)
            self.root.ids.output_display.text = "{:.2f}".format(celsius)

    def validate_text_input(self):
        try:
            fahrenheit = int(self.root.ids.text_input.text)
            return True
        except ValueError:
            pass
        return False

TemperatureConverter().run()
