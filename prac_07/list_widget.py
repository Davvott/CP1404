"""List Widget creator GUI. Create labels from text"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

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
        self.strings = []

    def build(self):
        """Build the Kivy GUI."""
        self.title = "List Widget"
        self.root = Builder.load_file('list_widget.kv')
        # Add initial widgets from default text in kv file
        self.create_widgets()
        return self.root

    def create_widgets(self):
        self.strings = []
        self.strings.append(self.root.ids.text_input.text)

        for string in self.strings:
            # Create a label and add_widget to id:list_box
            temp_label = Label(text=string)
            # temp_label.bind(on_release=self.press_entry)
            self.root.ids.list_box.add_widget(temp_label)

    def clear_all(self):
        self.root.ids.list_box.clear_widgets()

    def add_widget(self):
        self.strings.append(self.root.ids.text_input.text)
        self.root.ids.text_input.text = ""
        self.create_widgets()
        pass

DynamicListApp().run()
