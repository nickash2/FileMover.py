import errno
import sys
from os import environ, lstat, mkdir, path
from typing import List

from filemover.src.choice import Choice
from filemover.src.filter import FileFilter


def get_file_filters() -> List[Choice]:
    choices = []

    audio_filter = FileFilter(".mp3", ".wav", ".ogg", ".aac", ".wma", ".flac", ".m4a")
    image_filter = FileFilter(".jpg", ".png", ".gif", ".webp", ".tiff", ".psd", ".raw", ".bmp", ".heif", ".indd",
                              ".jpeg")
    text_filter = FileFilter(".txt", ".docx", ".rtf", ".pdf")
    excel_filter = FileFilter(".xlsx", ".xls", ".csv")
    program_filter = FileFilter(".exe", '.py')

    choices.append(Choice("Audio file", audio_filter))
    choices.append(Choice("Word processing file", text_filter))
    choices.append(Choice("Image file", image_filter))
    choices.append(Choice("Excel file", excel_filter))
    choices.append(Choice("Program file", program_filter))

    return choices


def get_choice(prompt: str, choices: List[Choice]) -> Choice:
    choice_string = f'{prompt}\n{list_to_string(choices)}'
    chosen_index = 0

    while chosen_index < 1 or chosen_index >= len(choices):
        print(choice_string)
        user_choice = input()

        if user_choice.isnumeric():
            chosen_index = int(user_choice)

    return choices[chosen_index - 1]


def list_to_string(options: List) -> str:
    output = ""
    for i, option in enumerate(options, 1):
        output += f"{i:>2}: {option}\n"

    return output


def get_input_path(prompt: str) -> str:
    user_path = input(prompt)

    while path.isdir(user_path) is False:
        print(f"{user_path} is not a directory")

        if path.exists(user_path):
            user_input = input("Enter a new path or press enter to use parent folder.\n")
            if user_input == "":
                user_path = path.dirname(user_path)
                break

        else:
            user_input = input("Enter a new path\n")

        user_path = user_input

    return path.abspath(user_path)


def get_output_path(prompt: str) -> str:
    while True:
        user_path = input(prompt)

        if path.isdir(user_path) is True:
            return path.abspath(user_path)

        if is_pathname_valid(user_path) is True:
            should_create_folders = get_user_confirmation(f"{user_path}\n"
                                                          f"Path does not exist, should it be created?")
            if should_create_folders is True:
                create_folders(user_path + "/")
                return path.abspath(user_path)


def create_folders(path_to_create) -> bool:
    folder_name = path.dirname(path_to_create)

    # parent folder
    if path.exists(folder_name):
        mkdir(path_to_create)
        return True

    # recursively create parent folder if missing
    create_folders(folder_name)
    if path.exists(path_to_create) is False:
        mkdir(path_to_create)
    return True


def get_user_confirmation(prompt: str) -> bool:
    user_input = input(prompt + " [y/n]\n")
    return user_input.lower() in {'y', 'yes', 'ye'}


def is_pathname_valid(pathname: str) -> bool:
    '''
    `True` if the passed pathname is a valid pathname for the current OS;
    `False` otherwise.
    '''
    # https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta
    # If this pathname is either not a string or is but is empty, this pathname
    # is invalid.
    try:
        if not isinstance(pathname, str) or not pathname:
            return False

        # Strip this pathname's Windows-specific drive specifier (e.g., `C:\`)
        # if any. Since Windows prohibits path components from containing `:`
        # characters, failing to strip this `:`-suffixed prefix would
        # erroneously invalidate all valid absolute Windows pathnames.
        _, pathname = path.splitdrive(pathname)

        # Directory guaranteed to exist. If the current OS is Windows, this is
        # the drive to which Windows was installed (e.g., the "%HOMEDRIVE%"
        # environment variable); else, the typical root directory.
        root_dirname = environ.get('HOMEDRIVE', 'C:') \
            if sys.platform == 'win32' else path.sep
        assert path.isdir(root_dirname)  # ...Murphy and her ironclad Law

        # Append a path separator to this directory if needed.
        root_dirname = root_dirname.rstrip(path.sep) + path.sep

        # Test whether each path component split from this pathname is valid or
        # not, ignoring non-existent and non-readable path components.
        for pathname_part in pathname.split(path.sep):
            try:
                lstat(root_dirname + pathname_part)
            # If an OS-specific exception is raised, its error code
            # indicates whether this pathname is valid or not. Unless this
            # is the case, this exception implies an ignorable kernel or
            # filesystem complaint (e.g., path not found or inaccessible).
            #
            # Only the following exceptions indicate invalid pathnames:
            #
            # * Instances of the Windows-specific "WindowsError" class
            #   defining the "winerror" attribute whose value is
            #   "ERROR_INVALID_NAME". Under Windows, "winerror" is more
            #   fine-grained and hence useful than the generic "errno"
            #   attribute. When a too-long pathname is passed, for example,
            #   "errno" is "ENOENT" (i.e., no such file or directory) rather
            #   than "ENAMETOOLONG" (i.e., file name too long).
            # * Instances of the cross-platform "OSError" class defining the
            #   generic "errno" attribute whose value is either:
            #   * Under most POSIX-compatible OSes, "ENAMETOOLONG".
            #   * Under some edge-case OSes (e.g., SunOS, *BSD), "ERANGE".
            except OSError as exc:
                if hasattr(exc, 'winerror'):
                    if exc.winerror == 123:
                        return False
                elif exc.errno in {errno.ENAMETOOLONG, errno.ERANGE}:
                    return False
    # If a "TypeError" exception was raised, it almost certainly has the
    # error message "embedded NUL character" indicating an invalid pathname.
    except TypeError as exc:
        return False
    # If no exception was raised, all path components and hence this
    # pathname itself are valid. (Praise be to the curmudgeonly python.)
    else:
        return True
    # If any other exception was raised, this is an unrelated fatal issue
    # (e.g., a bug). Permit this exception to unwind the call stack.
