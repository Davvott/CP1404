"""Iterate through a list of test names for cleaning"""

from prac_09.cleanup_files import fix_filename

tests = ["Isaiah53_6.txt", "O little town of bethlehem.TXT", "ItIsWell (oh my soul).txt"]

for test in tests:
    print("Test string: " + test)
    t = fix_filename(test)
    print("Fixed string: " + t)

