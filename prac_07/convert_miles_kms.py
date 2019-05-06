from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

CONVERSION_NUM = 1.60934


class ConvertMilesKms(App):

    output_text = StringProperty()

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('convert_miles_kms.kv')
        return self.root

    def handle_increment(self, n):
        """Validates text then increments and calls handle_convert_units()"""
        if self.handle_int_check():
            unit = int(self.root.ids.text_input.text)
            unit += n
            # Update text input box
            self.root.ids.text_input.text = "{}".format(unit)
            # Auto convert unit
            self.handle_convert_units()

    def handle_convert_units(self):
        """Validates text, converts by constant, updates output_text"""
        if self.handle_int_check():
            unit = int(self.root.ids.text_input.text)
            unit *= CONVERSION_NUM
            self.output_text = str(unit)

    def handle_int_check(self):
        """Checks text_input.text is int and returns True, else False"""
        try:
            int(self.root.ids.text_input.text)
            return True
        except ValueError:
            self.output_text = "0.0"
            pass
        return False


ConvertMilesKms().run()
