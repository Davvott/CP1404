"""Simple file folder restore"""
import os
import shutil

DIR = ".\FilesToSort"
BACKUP = ".\FilesToSort_backup"


def main():
    shutil.rmtree(DIR)
    os.mkdir(DIR)

    for firs, subdirs, files in os.walk(BACKUP):

        for file in files:  # file is string not path

            file_path = os.path.join(BACKUP, file)
            shutil.copy(file_path, ".\FilesToSort")

            print(file, " moved to ", BACKUP)


if __name__ == "__main__":
    main()
