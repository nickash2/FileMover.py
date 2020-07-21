from os import listdir, path
from shutil import move
from typing import Optional

from .filter import FileFilter
from .util import get_choice, get_file_filters, get_input_path, get_user_confirmation


class FileMover:

    def __init__(self, input_path: Optional[str] = None, output_path: Optional[str] = None):
        self.input_path: str = input_path
        self.output_path: str = output_path
        self.file_filter: FileFilter

        filters_options = get_file_filters()
        self.selected_choice = get_choice("What type of files do you want to move?", filters_options)
        self.file_filter = self.selected_choice.value
        self.main()

    def main(self):
        if self.input_path is None:
            self.input_path = get_input_path("Where do you want to move files from?\n")

        if self.output_path is None:
            self.get_output_path("Where do you want to move the files to?\n")

        should_move_files = get_user_confirmation(f"{self.selected_choice.string_representation} from:\n"
                                                  f"{self.input_path}\n"
                                                  f"TO -------->\n"
                                                  f"{self.output_path}\n"
                                                  f"Do you wish to continue?")
        if should_move_files is True:
            self.move_files()

    def move_files(self):
        for full_file_name in listdir(self.input_path):
            file_name, extension = path.splitext(full_file_name)

            # Alternatively move with wildcards and loop over selected file extensions
            if extension in self.file_filter:
                file_path = path.join(self.input_path, full_file_name)
                move(file_path, self.output_path)
