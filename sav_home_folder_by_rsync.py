#! /usr/bin/env python3
# coding:utf-8

"""
    Save all folders user on ssd backup
"""

import os


os.system("clear")
os.system("lsblk")


class BackupFolders:
    """
    Save all folders user
    """

    NB_LINES_1 = 60
    NB_LINES_2 = 45

    def __init__(self):
        self.path_destination = ""
        self.folders = [
            "Documents",
            "GitHub",
            "Images",
            "Mes_projets",
            "OC_DA_Python",
            "Téléchargements",
            "Vidéos",
        ]
        self.rsync_option = ""

    def f_string_head(self) -> None:
        """
        Head string the program
        """

        print(
            f"\n\n{'-' * self.NB_LINES_2}\n\n"
            f"[ Synchronisation du dossier '/home/{os.getlogin()}' ]\n\n"
        )

    def select_option(self) -> str:
        """
        Select options for rsync
        """

        choice = int(
            input(
                f"\n\nSelect option for rsync :\n{'-' * 25}\n\n"
                f"\t[ 1 ] Direct sync (Ext4)\n"
                f"\t[ 2 ] Dry-run sync (checking for differences) - (Ext4)\n"
                f"\t[ 3 ] Direct sync (Ntfs)\n"
                f"\t[ 4 ] Dry-run sync (checking for differences) - (Ntfs)\n\n"
                f"- Select your option : "
            )
        )

        if choice == 1:
            self.rsync_option = "-avh"
        elif choice == 2:
            self.rsync_option = "-navh"
        elif choice == 3:
            self.rsync_option = "-rtlogvh"
        elif choice == 4:
            self.rsync_option = "-rtlongvh"

        return self.rsync_option

    def path_of_destination_and_options(self) -> None:
        """
        Get the destination path
        """

        self.path_destination = input("- Destination directory path : ")

        for folder in self.folders:
            folder = f"{self.path_destination}/{os.getlogin()}/home_mike/{folder}/"
            os.makedirs(folder, exist_ok=True)

    def sync_laptop_to_ssd(self) -> None:
        """
        Rsync the folders user
        """

        if self.rsync_option in ("-rtlogvh", "-rtlongvh"):
            self.folders.remove("Images")

        for folder in self.folders:

            path_folder = f"> Synchronisation du dossier '{folder}'"

            print(
                f"\n\n{'=' * self.NB_LINES_1}\n"
                f"{path_folder}\n"
                f"{'-' * len(path_folder)}\n"
            )
            os.system(
                f"rsync {self.rsync_option} --delete /home/{os.getlogin()}/{folder}/ "
                f"{self.path_destination}/{os.getlogin()}/home_mike/{folder}/"
            )

            print(f"\n{'=' * self.NB_LINES_1}\n\n")


def main():
    """
    Execute the program
    """

    backup = BackupFolders()
    backup.f_string_head()
    backup.path_of_destination_and_options()
    backup.select_option()
    backup.sync_laptop_to_ssd()


if __name__ == "__main__":
    main()
