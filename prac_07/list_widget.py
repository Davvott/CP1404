
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

canvas = "canvas:" \
         "  Color:" \
         "      rgba: (0, 0, 0, 1)" \
         "  Rectangle:" \
         "      pos: self.pos" \
         "      size: self.size"

class DynamicListApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data example - list of strings
        self.strings = ["this", "is", "my", "list"]
        print(self.strings)

    def build(self):
        """Build the Kivy GUI."""
        self.title = "List Widget"
        self.root = Builder.load_file('list_widget.kv')

        self.create_widgets()
        return self.root

    def create_widgets(self):
        for string in self.strings:
            temp_label = Label(text=string)
            # temp_label.bind(on_release=self.press_entry)
            self.root.ids.list_box.add_widget(temp_label)

DynamicListApp().run()