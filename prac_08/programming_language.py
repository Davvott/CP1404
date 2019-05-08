
class ProgrammingLanguage:
    """Class that holds name, typing, reflection and year attributes
    Methods:

    is_dynamic()
    __str__() ; Custom print statement
    """
    def __init__(self, name, typing, reflection, year, pointer_artimetic):
        self.name = name
        self.typing = typing.lower() == "dynamic"
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_artimetic

    def is_dynamic(self):
        """Return bool of self.typing"""
        return self.typing

    def __str__(self):
        typed = "Dynamic" if self.is_dynamic() else "Static"
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, typed, self.reflection, self.year)
