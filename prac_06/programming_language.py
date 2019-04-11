
class ProgrammingLanguage:
    """Class that holds name, typing, reflection and year attributes
    Methods:

    is_dynamic()
    __str__() ; Custom print statement
    """
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing.lower()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return bool of self.typing"""
        return self.typing == "dynamic"

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing.title(), self.reflection, self.year)