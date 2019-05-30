"""CP1404 Extension and Practice Work
Check files for missing data
The song lyric text files should all have copyright information in them on a line that
starts with .i like:

.i (c) 2011 Thankyou Music (Admin. by Crossroad Distributors Pty. Ltd.)
Write a program that reports the names and directories of all of the files that are missing this line.

--- Version 2 ---

Automatically look up the copyright information from the Internet based on the song title and author,
then add the data to the file...
Good luck with that ;)
Assumes list of files. Not tree of subdirs
This program is designed for multiple directory tree structures.
"""

import os

ROOT = ".\\Lyrics"
SEARCH_TERM = ".i "
FULL_SEARCH_TERM = ".i ©"


def main():
    """Find all file with search term"""

    os.chdir(ROOT)
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
                line = f.read()
            if FULL_SEARCH_TERM not in line:
                files_missing.append(pathname)

    print("\nFiles missing: \n", files_missing)


if __name__ == "__main__":
    main()
    # print(os.path.splitext(".\\File.txt")[1])
    # splitext returns tuple of file, .ext
