"""CP1404 Prac
Walk given dir and Create dirs from file extensions in root;
 Move files into respective dirs"""

import os
import shutil

ROOT = ".\FilesToSort"


def main():
    """Main loop for dir creation and file move"""
    extensions = []

    os.chdir(ROOT)
    root = "."

    for dirname, subdirs, filenames in os.walk('.'):
        print("Directory:", dirname)
        print("\tcontains subdirectories:", subdirs)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # Not efficient. is called in every subdirectory.
        create_file_ext_directories(root, extensions, filenames)
        # Tries to move files to non-existent dir
        move_files_to_ext_dirs(root, dirname, filenames)

    print(extensions)


def move_files_to_ext_dirs(root, dirname, filenames):
    """Given a dir with name==ext, move file there"""
    for name in filenames:

        filename, ext = name.split(".")

        # shutil.move requires full path names
        filename = os.path.join(dirname, name)
        destination = os.path.join(root, ext)
        print(destination)

        try:
            shutil.move(filename, destination)
            print(name, " moved to ", destination)
        except FileNotFoundError as error:
            print(error)
        except shutil.Error as error:  # package Error
            # File exists - will not duplicate
            print(error)


def create_file_ext_directories(root, extensions, filenames):
    """From os.walk() create dirs from set of extensions in dir"""
    for name in filenames:
        filename, ext = name.split('.')

        if ext not in extensions:
            extensions.append(ext)
            try:
                os.mkdir(os.path.join(root, ext))
            except FileExistsError:
                pass


if __name__ == "__main__":
    main()
