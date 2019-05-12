"""Simple file/folder restore"""
import os
import shutil

DIR = ".\FilesToSort"
BACKUP = ".\FilesToSort_backup"


def main():
    """Main program to 'erase' dir, and copy backup to dir"""
    shutil.rmtree(DIR)
    os.mkdir(DIR)

    for dirs, subdirs, files in os.walk(BACKUP):
        # Assumes just files in BACKUP
        copy_files_to_dir(files)


def copy_files_to_dir(files):
    for file in files:  # file is string not path

        file_path = os.path.join(BACKUP, file)
        shutil.copy(file_path, DIR)

        print(file, " moved to ", BACKUP)


if __name__ == "__main__":
    main()
