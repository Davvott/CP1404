
class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing.lower()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "dynamic"

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing.title(), self.reflection, self.year)