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

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""

    # _ on Capitals for CamelCase
    underscore_indices = []
    file_name = filename.replace(".TXT", ".txt")
    for i, char in enumerate(file_name):
        if char.islower():
            try:
                next_char = file_name[i+1]
                if next_char.isupper():  # requires underscore @ i+1
                    underscore_indices.append(i+1)
            except IndexError:
                pass

    # add "_" at indices
    result = list(file_name)
    for i in underscore_indices:
        result[i] = "_{}".format(result[i])

    new_name = "".join(result)
    return new_name


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
            new_name = get_fixed_filename(name)
            # join pathnames for rename
            old_pathname = os.path.join(directory_name, name)
            new_pathname = os.path.join(directory_name, new_name)
            print(old_pathname, new_pathname)
            # Rename
            os.rename(old_pathname, new_pathname)

# main()
# demo_walk()

test = "SilentNightTonight.TXT"
t = get_fixed_filename(test)
print(t)
