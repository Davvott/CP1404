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
        if self.handle_int_check():
            unit = int(self.root.ids.text_input.text)
            unit += n
            self.root.ids.text_input.text = "{}".format(unit)
            self.handle_convert_units()

    def handle_convert_units(self):
        if self.handle_int_check():
            unit = int(self.root.ids.text_input.text)
            unit *= CONVERSION_NUM
            self.output_text = str(unit)

    def handle_int_check(self):
        # Try for int
        try:
            int(self.root.ids.text_input.text)
            return True
        except ValueError as err:
            self.root.ids.display_text.text = "0.0"
            pass
        return False


ConvertMilesKms().run()
