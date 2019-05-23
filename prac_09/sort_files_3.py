"""CP1404 Extension and Practice Work
Check files for missing data
The song lyric text files should all have copyright information in them on a line that
starts with .i like:

.i (c) 2011 Thankyou Music (Admin. by Crossroad Distributors Pty. Ltd.)
Write a program that reports the names and directories of all of the files that are missing this line.

--- Version 2 ---

Automatically look up the copyright information from the Internet based on the song title and author, then add the data to the file...
Good luck with that ;)
Assumes list of files. Not tree of subdirs
This program is designed for multiple directory tree structures.
"""

import os
import shutil

ROOT = ".\Lyrics"
SEARCH_TERM = ".i "
t = ".i ©"

def main():
    """Find all file extensions, prompt for new dirs, move files"""
    extensions = []

    os.chdir(ROOT)
    root = "."
    files_missing = []

    # Walk entire tree without changing cwd
    for dirname, subdirs, filenames in os.walk('.'):
        print("Directory:", dirname)
        print("\tcontains subdirectories:", subdirs)
        # print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # Scan files for ".i (c)" in file_line
        for file in filenames:
            pathname = os.path.join(dirname, file)
            with open(pathname) as f:
                # TODO: unicode error
                line = f.read()
            try:
                if SEARCH_TERM not in line:
                    files_missing.append(pathname)
            # exception?
            except:
                pass
    print("\nFiles missing: \n", files_missing)


        # open file
        # readline()
        # check for string in line
        # if not: report dir and file name


def create_list_file(filenames):
    """Return list of extensions from list of filenames"""
    extensions = []
    for name in filenames:
        _, ext = os.path.splitext(name)
        if ext not in extensions:
            extensions.append(ext)
    return extensions


def get_user_input(ext):
    category = input("What category would you like to sort {} files into? ".format(ext))
    while not category.isalnum():
        print("Please enter a directory name of at least one digit")
        category = input("What category would you like to sort {} files into? ".format(ext))
    return category


if __name__ == "__main__":
    main()
    # print(os.path.splitext(".\\File.txt")[1])
    # splitext returns tuple of file, .ext
