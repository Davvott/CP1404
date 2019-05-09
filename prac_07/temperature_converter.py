"""GUI Temperature automatic converter Fahrenheit to Celsius"""
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty


class TemperatureConverter(App):

    display_text = StringProperty()
    convert_to_celsius = True

    def build(self):
        Window.size = (500, 500)
        self.title = "Temperature Converter"
        self.root = Builder.load_file("temp_converter.kv")
        return self.root

    def convert_fahrenheit_to_celsius(self, fahrenheit):
        """Convert fahrenheit to celsius from parameter"""
        celsius = 5 / 9 * (fahrenheit - 32)
        return celsius

    def convert_celsius_to_fahrenheit(self, celsius):
        """Convert celsius to fahrenheit from parameter"""
        fahrenheit = celsius * 9.0 / 5 + 32
        return fahrenheit

    def switch_units(self):
        """Switch selection criteria for conversion"""
        if self.convert_to_celsius:
            self.convert_to_celsius = False
        else:
            self.convert_to_celsius = True
        self.handle_conversion()

    def handle_increment(self, n):
        """Increments text_input +- 1"""
        if self.validate_text_input():
            # Need to convert to int before increment
            value = int(self.root.ids.text_input.text)
            value += n
            self.root.ids.text_input.text = str(value)

    def handle_conversion(self):
        """Called on_text input for automatic conversion"""
        if self.validate_text_input() and self.convert_to_celsius:
            fahrenheit = int(self.root.ids.text_input.text)
            celsius = self.convert_fahrenheit_to_celsius(fahrenheit)
            self.display_text = "{:.2f} *C".format(celsius)
        elif self.validate_text_input():
            celsius = int(self.root.ids.text_input.text)
            fahrenheit = self.convert_celsius_to_fahrenheit(celsius)
            self.display_text = "{:.2f} *F".format(fahrenheit)

    def validate_text_input(self):
        """Validate text_input as integer"""
        try:
            int(self.root.ids.text_input.text)
            return True
        except ValueError:
            pass
        return False


TemperatureConverter().run()
