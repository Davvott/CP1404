"""List Widget creator GUI. Create labels from text"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

canvas = "canvas:" \
         "  Color:" \
         "      rgba: (0, 0, 0, 1)" \
         "  Rectangle:" \
         "      pos: self.pos" \
         "      size: self.size"


class DynamicListApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    status_msg = StringProperty()

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
            temp_label = Button(text=string)


            self.root.ids.list_box.add_widget(temp_label)
            temp_label.bind(on_release=self.update_status)

    def clear_all(self):
        self.root.ids.list_box.clear_widgets()

    def update_status(self, instance):
        self.status_msg = instance.text

    def add_widget(self):
        if self.root.ids.text_input.text:

            self.strings.append(self.root.ids.text_input.text)
            self.create_widgets()
            self.root.ids.text_input.text = ""


DynamicListApp().run()
