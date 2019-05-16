"""CP1404 Prac
Extend sort_files_1 to prompt for user categorising.
Assumes list of files. Not tree of subdirs"""

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

        # Check file extensions pass to list
        extensions = create_list_file(filenames)
        # Iterate through list and Prompt user for strings
        for ext in extensions:
            category = input("What category would you like to sort {} files into? ").format(ext)
            try:
                os.mkdir(os.path.join(root, category))
            except FileExistsError as error:
                print(error)
                # TODO: move files
            # for each ext, move file with ext in filename into category dir
            # move_files_to_dirs(root, dirname, filenames)

    print(extensions)


def create_list_file(filenames):
    extensions = []
    for name in filenames:
        filename, ext = name.split('.')
        if ext not in extensions:
            extensions.append(ext)
    return extensions


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


if __name__ == "__main__":
    main()
