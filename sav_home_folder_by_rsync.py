#! /usr/bin/env python3
# coding:utf-8

"""
Save and restore all folders user
"""

import os


class BackupFolders:
    """
    Save all folder (important) user
    """

    def __init__(self):
        self.home_name = f"/home/{os.getlogin()}/"
        self.path_destination = ""
        self.rsync_option = ""
        self.type_synchronisation = int()
        self.nb_lines = f"{'=' * 50}"
        self.folders = [
            "Documents",
            "GitHub",
            "Images",
            "Mes_projets",
            "OC_DA_Python",
            "Téléchargements",
            "Vidéos",
        ]

    def f_string_head(self) -> None:
        """
        Head string the program
        """

        print(
            f"\n\n{self.nb_lines}\n\n"
            f"[ Synchronisation of folder '/home/{os.getlogin()}/' ]\n\n"
            f"{self.nb_lines}\n\n"
        )

    def f_string_path_folder(self, folder) -> None:
        """
        Show folder synchronized
        """

        path_folder = f"> Synchronisation of folder '{folder}'"
        print(f"\n\n{self.nb_lines}\n" f"{path_folder}\n" f"{'-' * len(path_folder)}\n")

    def backup_or_restore(self) -> None:
        """
        Select option of type de synchronisation
        """

        choice_backup_or_restore = int(
            input(
                f"Select option of type de synchronisation :\n\n"
                f"\t [ 1 ] Backup of laptop to SSD\n"
                f"\t [ 2 ] Restore from SSD to laptop\n\n"
                f"- Select option : "
            )
        )

        self.type_synchronisation = choice_backup_or_restore

    def path_of_destination(self) -> None:
        """
        Get the destination path
        """

        print("\n\n")

        os.system("lsblk -f")

        self.path_destination = input("\n\n- Destination directory path : ")

        for folder in self.folders:
            folder = f"{self.path_destination}/{os.getlogin()}/home_mike/{folder}/"
            os.makedirs(folder, exist_ok=True)

    def select_option_rsync(self) -> str:
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

        if choice == 1:
            self.rsync_option = "-avh"
        elif choice == 2:
            self.rsync_option = "-navh"
        elif choice == 3:
            self.rsync_option = "-rtlogvh"
        elif choice == 4:
            self.rsync_option = "-rtlongvh"

    def synchronisation(self) -> None:
        """
        Rsync the folder user (sync laptop to ssd disk) if self.type_synchronisation = 1
        Rsync the folder user (sync ssd disk to laptop) if self.type_synchronisation = 2
        """

        if self.rsync_option in ("-rtlogvh", "-rtlongvh"):
            self.folders.remove("Images")

        for folder in self.folders:

            self.f_string_path_folder(folder)

            if self.type_synchronisation == 1:
                os.system(
                    f"rsync {self.rsync_option} --delete /home/{os.getlogin()}/{folder}/ "
                    f"{self.path_destination}/{os.getlogin()}/home_mike/{folder}/"
                )

                print(f"\n{self.nb_lines}\n\n")

            if self.type_synchronisation == 2:
                os.system(
                    f"rsync {self.rsync_option} {self.path_destination}/{os.getlogin()}/home_mike/{folder}/ "
                    f"{self.home_name}/{folder}/"
                )

                print(f"\n{self.nb_lines}\n\n")


def main():
    """
    Execute the program
    """

    os.system("clear")

    backup = BackupFolders()
    backup.f_string_head()
    backup.backup_or_restore()
    backup.path_of_destination()
    backup.select_option_rsync()
    backup.synchronisation()


if __name__ == "__main__":
    main()
