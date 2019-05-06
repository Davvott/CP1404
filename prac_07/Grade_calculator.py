from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button


class GradeCalculator(App):

    def build(self):
        Window.size = (500, 500)
        self.title = "Grade Calculator"
        self.root = Builder.load_file('grade_calculator.kv')
        return self.root

    def handle_grade_score(self):
        score = self.root.ids.text_input.text
        try:
            score = int(score)
            grade = self.calculate_grade(score)
            self.root.ids.output_display.text = grade
        except ValueError:
            self.root.ids.output_display.text = 'Enter an integer'

    def calculate_grade(self, score):
        if score >= 85:
            grade = 'High Distinction'
        elif score >= 75:
            grade = 'Distinction'
        elif score >= 65:
            grade = 'Credit'
        elif score >= 50:
            grade = 'Pass'
        else:
            grade = 'Fail'
        return grade


# Create instance of GradeCalculator and run() it
GradeCalculator().run()
