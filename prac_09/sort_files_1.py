"""CP1404 Prac
Walk given dir and Create dirs for file extensions, move files into
 respective dirs"""

import os
import shutil

START_DIR = "FilesToSort"


def main():
    """Main loop for dir creation and file move"""
    extensions = []

    os.chdir(START_DIR)
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        create_file_ext_directories(directory_name, extensions, filenames)

        move_files_to_ext_dirs(directory_name, filenames)

    print(extensions)


def move_files_to_ext_dirs(directory_name, filenames):
    for name in filenames:

        filename, ext = name.split(".")
        destination = os.path.join(directory_name, ext)
        print(destination)

        try:
            shutil.move(name, destination)
            print(name, " moved to ", destination)
        except FileNotFoundError as error:
            print(error)


def create_file_ext_directories(directory_name, extensions, filenames):
    for name in filenames:
        filename, ext = name.split('.')

        if ext not in extensions:
            extensions.append(ext)
            try:
                os.mkdir(os.path.join(directory_name, ext))
            except FileExistsError:
                pass


if __name__ == "__main__":
    main()
