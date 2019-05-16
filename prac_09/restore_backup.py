"""Simple file/folder restore
Note: On networks change to folders may not be updated by Pycharm"""
import os
import shutil

DIRECTORY = ".\FilesToSort"
BACKUP = ".\FilesToSort_backup"


def main():
    """Main program to 'erase' dir, and copy backup to dir"""
    shutil.rmtree(DIRECTORY)
    os.mkdir(DIRECTORY)

    for dirs, subdirs, files in os.walk(BACKUP):
        # Assumes just files in BACKUP
        copy_files_to_dir(files)


def copy_files_to_dir(files):
    for file in files:  # file is string not path

        file_path = os.path.join(BACKUP, file)
        shutil.copy(file_path, DIRECTORY)

        print(file, " moved to ", DIRECTORY)


if __name__ == "__main__":
    print(os.getcwd())
    main()

