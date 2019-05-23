"""CP1404 Prac
Extend sort_files_1 to prompt for user categorising.
Assumes list of files. Not tree of subdirs
This program is designed for multiple directory tree structures.
"""

import os
import shutil

ROOT = ".\FilesToSort"


def main():
    """Find all file extensions, prompt for new dirs, move files"""
    extensions = []

    os.chdir(ROOT)
    root = "."
    file_path_list = []

    # Walk entire tree without changing cwd
    for dirname, subdirs, filenames in os.walk('.'):
        print("Directory:", dirname)
        print("\tcontains subdirectories:", subdirs)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # Check file extensions pass to list
        extensions = create_list_file(filenames)

        # create a list of dirname/filename for filename in filenames
        for file_name in filenames:
            file_path_list.append(str(os.path.join(dirname, file_name)))

    print(file_path_list)

    # Iterate through extensions and Prompt user for strings
    for ext in extensions:
        category = get_user_input(ext)
        category_path = os.path.join(root, category)
        try:
            # make dir in root
            os.mkdir(category_path)
        except FileExistsError as error:
            print(error, "mkdir error")
            # Does not delete existing folders in root
        # for each ext, move file with ext in filename into category dir
        move_files_to_dirs(root, ext, category_path, file_path_list)

    print(extensions)


def move_files_to_dirs(root, ext, destination, filenames):
    """Given a file with ext, move file to root\\ext"""
    for file in filenames:
        print(file)
        if os.path.splitext(file)[1] == ext:
            # shutil.move requires full path names
            # Destination in root\category dir

            print(destination)
            try:
                shutil.move(file, destination)
                print(file, " moved to ", destination)
            except FileNotFoundError as error:
                print(error, "move files error")
            except shutil.Error as error:  # package Error
                # File exists - will not duplicate
                print(error)


def create_list_file(filenames):
    """Return list of extensions from list of filenames"""
    extensions = []
    for name in filenames:
        _, ext = os.path.splitext(name)
        if ext not in extensions:
            extensions.append(ext)
    print(extensions)
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
