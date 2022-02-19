#! /usr/bin/env python3
# coding:utf-8

import os


class ViewsToBackup:
    """
    Method for all view of Backup_home_folders
    """

    def __init__(self):
        self.nb_lines = f"{'=' * 50}"

    def f_string_head(self) -> None:
        """
        Head string the program
        """

        print(
            f"\n{self.nb_lines}\n\n"
            f"[ Synchronisation of folder '/home/{os.getlogin()}/' ]\n\n"
            f"{self.nb_lines}\n\n"
        )

    def f_string_lines(self):
        print(f"\n{self.nb_lines}\n\n")

    def f_string_backup_or_restore(self) -> int:

        choice_backup_or_restore = int(
            input(
                f"{'Select option of type de synchronisation :'}\n\n"
                f"\t{'[ 1 ] Backup of laptop to SSD'}\n"
                f"\t{'[ 2 ] Restore from SSD to laptop'}\n\n"
                f"- Select option : "
            )
        )

        return choice_backup_or_restore

    def f_string_path_of_destination(self, folders) -> str:
        """
        Get the destination path
        """
        print("\n\n")
        os.system("lsblk -f")

        path = input("\n\n- Destination directory path : ")

        for folder in folders:
            folder = f"{path}/{os.getlogin()}/home_mike/{folder}/"
            os.makedirs(folder, exist_ok=True)

        return path

    def f_string_select_option_rsync(self) -> int:
        """
        Select option for rsync
        """

        select_option = "Select option for rsync :"

        choice = int(
            input(
                f"\n\n{select_option}\n{'-' * len(select_option)}\n\n"
                f"\t[ 1 ] Direct sync (Ext4)\n"
                f"\t[ 2 ] Dry-run sync (checking for differences) - (Ext4)\n"
                f"\t[ 3 ] Direct sync (Ntfs)\n"
                f"\t[ 4 ] Dry-run sync (checking for differences) - (Ntfs)\n\n"
                f"- Select option : "
            )
        )

        return choice

    def f_string_folder_sync(self, folder) -> None:
        """
        Folder synchronized
        """

        path_folder = f"> Synchronisation of folder '{folder}'"
        print(
            f"\n\n{self.nb_lines}\n"
            f"{path_folder}\n"
            f"{'-' * len(path_folder)}\n"
        )




