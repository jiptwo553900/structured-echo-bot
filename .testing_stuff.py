import os
from typing import AnyStr

# Default config values
FOLDER_ICON = "📁"
FILE_ICON = "📄"
INDENT = "│  "
ENTRY_INDENT = "├──"
LAST_ENTRY_INDENT = "└──"

# Current directory path
ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

# First string (print root directory)
print(f"{ENTRY_INDENT} {FOLDER_ICON} {os.path.basename(ROOT_PATH)}")


def print_tree(
        root_path: AnyStr | str = ROOT_PATH,
        folder: str = FOLDER_ICON,
        file: str = FILE_ICON,
        ind: str = INDENT,
        entry_ind: str = ENTRY_INDENT,
        last_ind: str = LAST_ENTRY_INDENT
) -> None:
    """
    Prints a tree

    :param root_path:   root path, defaults to current dir path
    :param folder:      folder icon
    :param file:        file icon
    :param ind:         general indent (from left side)
    :param entry_ind:   entry indent
    :param last_ind:    the last entry indent
    """
    files = list(os.scandir(root_path))
    for i, entry in enumerate(files):
        if i == len(files) - 1:
            entry_ind = last_ind

        if entry.is_file():
            print(f"{ind} {entry_ind} {file} {str(entry.name)}")
        else:
            print(f"{ind} {entry_ind} {folder} {str(entry.name)}")
            print_tree(
                root_path=f"{str(root_path)}/{str(entry.name)}",
                ind=ind + " " + INDENT
            )


print_tree()