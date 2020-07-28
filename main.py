import file_sorter
import time
import os


def main():
    root = file_sorter.Root_Directory("template.txt")
    root.update_child_directories()
    root.sort_files()
    number_of_files = len(os.listdir(root.base_path))
    while True:
        # sort if a new file is detected
        if len(os.listdir(root.base_path)) != number_of_files:
            root.sort_files()
        time.sleep(2)

if __name__ == "__main__":
    main()