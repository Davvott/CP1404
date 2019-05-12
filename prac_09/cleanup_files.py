"""
CP1404/CP5632 Practical
Use existing functions and loops for file cleanup
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    try:
        os.mkdir('temp')
    except FileExistsError as error:
        print(error)
    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = fix_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def fix_filename(filename):
    """Return a 'fixed' version of filename."""
    try:
        file_name, ext = filename.split(".")
    except ValueError as err:
        print(err)
        ext = "TXT"
        file_name = filename

    file_name = file_name.replace(" ", "_")

    previous_char = "A"
    fixed_filename = ""
    for i, char in enumerate(file_name):
        # ItIs --> It_Is
        if char.isupper() and previous_char.islower():
            fixed_filename += "_" + char
        # ILove --> I_Love
        elif i != 0 and previous_char.isupper() and char.isupper():
            fixed_filename += "_" + char

        else:
            fixed_filename += char
        previous_char = char

    fixed_filename = "_".join([name.title() for name in fixed_filename.split("_")])
    fixed_filename += "." + ext.replace("TXT", "txt")

    return fixed_filename


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # Fix filenames in each directory
        for name in filenames:
            # generate new_name
            new_name = fix_filename(name)
            # join pathnames for rename
            old_pathname = os.path.join(directory_name, name)
            new_pathname = os.path.join(directory_name, new_name)
            print(old_pathname, new_pathname)
            # Rename
            os.rename(old_pathname, new_pathname)

# main()
if __name__ == "__main__":
    demo_walk()
