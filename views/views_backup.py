#! /usr/bin/env python3
# coding:utf-8

import os


class ViewsToBackup:
    """
    Method for all view of Backup_home_folders
    """

    def __init__(self):
        self.f_string_head()

    def f_string_head(self) -> None:
        """
        Head string the program
        """

        self.f_string_line("=", "\n", "\n")
        print(f"[ Synchronisation of folder '/home/{os.getlogin()}/' ]")
        self.f_string_line("=", "\n", "\n")

    def f_string_line(self, symbol: str = "", n_1: str = "", n_2: str = "") -> None:
        print(f"{n_1}{symbol * 100}{n_2}")

    def backup_or_restore(self) -> int:

        choice_backup_or_restore = int(
            input(
                f"\n\n{'Select option of type de synchronisation :'}\n\n"
                f"\t{'[ 1 ] Backup of laptop to SSD'}\n"
                f"\t{'[ 2 ] Restore from SSD to laptop'}\n\n"
                f"- Select option : "
            )
        )

        self.f_string_line("#", "\n\n", "\n\n")

        return choice_backup_or_restore

    def f_string_path_of_destination(self, folders) -> str:
        """
        Get the destination path
        """

        os.system("lsblk -f")

        path = input("\n\n- Destination directory path : ")

        for folder in folders:
            folder = f"{path}/{os.getlogin()}/home_mike/{folder}/"
            os.makedirs(folder, exist_ok=True)

        self.f_string_line("#", "\n\n", "\n\n")

        return path

    def f_string_select_option_rsync(self) -> int:
        """
        Select option for rsync
        """

        select_option = "Select option for rsync :"

        choice = int(
            input(
                f"{select_option}\n{'-' * len(select_option)}\n\n"
                f"\t[ 1 ] Direct sync (Ext4)\n"
                f"\t[ 2 ] Dry-run sync (checking for differences) - (Ext4)\n"
                f"\t[ 3 ] Direct sync (Ntfs)\n"
                f"\t[ 4 ] Dry-run sync (checking for differences) - (Ntfs)\n\n"
                f"- Select option : "
            )
        )

        self.f_string_line("#", "\n\n", "\n\n")

        return choice

    def f_string_folder_sync(self, folder) -> None:
        """
        Folder synchronized
        """

        self.f_string_line("=", "\n\n")

        path_folder = f"> Synchronisation of folder '{folder}'"

        print(f"{'':<25}{path_folder:<25}\n" f"{'':<25}{'-' * len(path_folder)}\n")
