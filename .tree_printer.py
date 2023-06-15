import os
from itertools import filterfalse

# Default config values
FOLDER_ICON = "📁"  # folder icon
FILE_ICON = "📄"  # file icon
INDENT = "│  "  # general indent (from left side)
ENTRY_INDENT = "├──"  # entry indent
LAST_ENTRY_INDENT = "└──"  # the last entry indent
SHOW_HIDDEN: bool = False  # if True: show hidden folders (.git, etc)
PRINT_ROOT: bool = True  # if True: print root directory

# Start parts of folder names we want to ignore
# when show_hidden is False.
HIDDEN: tuple[str, ...] = (".", "__pycache")

# Current directory path.
ROOT_PATH: str = os.path.dirname(os.path.realpath(__file__))


def is_hidden_folder(entry: os.DirEntry) -> bool:
    """Check if entry is folder and is hidden"""
    return (entry.is_dir()
            and entry.name.startswith(HIDDEN))


def print_tree(root_path: str = ROOT_PATH,
               folder: str = FOLDER_ICON,
               file: str = FILE_ICON,
               ind: str = INDENT,
               entry_ind: str = ENTRY_INDENT,
               last_ind: str = LAST_ENTRY_INDENT,
               show_hidden: bool = SHOW_HIDDEN,
               print_root: bool = PRINT_ROOT) -> None:
    """
    Prints a tree. Recursive.

    :param root_path:   root path, defaults to current dir path
    :param folder:      folder icon
    :param file:        file icon
    :param ind:         general indent (from left side)
    :param entry_ind:   entry indent
    :param last_ind:    the last entry indent
    :param show_hidden: if True: show hidden folders (.git, .idea, etc)
    :param print_root:  if True: print root directory
    """
    # First string (print root directory).
    if print_root:
        print(f"{entry_ind} {folder} {os.path.basename(root_path)}")

    # Check if show_hidden is False and filter entries.
    if not show_hidden:
        entries: list[os.DirEntry] = list(
            filterfalse(is_hidden_folder, os.scandir(root_path)))
    else:
        entries = list(os.scandir(root_path))

    for i, entry in enumerate(entries):

        # If the entry is last in folder: replace indent type.
        if i == len(entries) - 1:
            entry_ind = last_ind

        if entry.is_file():
            # If the entry is a file: print it and go on.
            print(f"{ind} {entry_ind} {file} {entry.name}")

        else:
            # If the entry is a folder: print it ...
            print(f"{ind} {entry_ind} {folder} {entry.name}")
            # ... and call of print_tree() for this folder.
            print_tree(
                root_path=f"{root_path}/{entry.name}",
                ind=(ind + " " + ind),
                print_root=False
            )


if __name__ == "__main__":
    print_tree()
