from prac_06.programming_language import ProgrammingLanguage

# Create some instances
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(ruby)

# Create array
languages = [ruby, python, visual_basic]

# Filter language by is_dynamic()
dynamically_typed = [language for language in languages if language.is_dynamic()]

print("The dynamically typed languages are: ")
for typed in dynamically_typed:
    print(typed.name)
