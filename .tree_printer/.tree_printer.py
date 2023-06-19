import os
from itertools import filterfalse

# Default config values
FOLDER_ICON: str = "📁"  # folder icon
FILE_ICON: str = "📄"  # file icon
INDENT: str = "│  "  # general indent (from left side)
ENTRY_INDENT: str = "├──"  # entry indent
LAST_ENTRY_INDENT: str = "└──"  # the last entry indent
SHOW_HIDDEN: bool = False  # if True: show hidden folders (.git, etc)
PRINT_ROOT: bool = True  # if True: print root directory

# Prefixes of folders we want to ignore when show_hidden is False.
HIDDEN: tuple[str, ...] = (".", "__pycache__")

# Current directory path.
ROOT_PATH: str = os.path.dirname(os.path.realpath(__file__))


def is_hidden_folder(entry: os.DirEntry) -> bool:
    """Check if entry is folder and is hidden"""
    return entry.is_dir() and entry.name.startswith(HIDDEN)


def print_tree(root_path: str = ROOT_PATH,
               ind: str | None = None,
               show_hidden: bool = SHOW_HIDDEN,
               print_root: bool = PRINT_ROOT) -> None:
    """
    Prints the folder tree. Recursive.

    :param root_path:   root path, defaults to current dir path
    :param ind:         ident (from left), must be None on first call
    :param show_hidden: if True: show hidden folders (.git, .idea, etc)
    :param print_root:  if True: print root directory
    """
    # As function is recursive, we need 'ind' to be None on the first call.
    if ind is None:
        ind = INDENT

    # Print the root directory.
    if print_root:
        print(f"{ENTRY_INDENT} {FOLDER_ICON} {os.path.basename(root_path)}")

    # Using os.scandir here to get an iterator of os.DirEntry objects.
    entries_iter = os.scandir(root_path)

    # Filter entries if show_hidden is False.
    if show_hidden:
        entries: list[os.DirEntry] = list(entries_iter)
    else:
        entries = list(filterfalse(is_hidden_folder, entries_iter))

    for i, entry in enumerate(entries):

        if i == len(entries) - 1:
            # If the entry is last in folder: use LAST_ENTRY_INDENT.
            entry_ind = LAST_ENTRY_INDENT
        else:
            # In other case: use ENTRY_INDENT.
            entry_ind = ENTRY_INDENT

        if entry.is_file():
            # If the entry is a file: print it and go on.
            print(f"{ind} {entry_ind} {FILE_ICON} {entry.name}")
        else:
            # If the entry is a folder: print it ...
            print(f"{ind} {entry_ind} {FOLDER_ICON} {entry.name}")
            # ... and call print_tree() for this folder.
            print_tree(root_path=f"{root_path}/{entry.name}",
                       ind=(ind + " " + INDENT),
                       show_hidden=show_hidden,
                       print_root=False)


if __name__ == "__main__":
    print_tree(root_path=os.path.realpath(".."))
