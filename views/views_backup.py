#! /usr/bin/env python3
# coding:utf-8

"""
Method views of Backup home folders
"""

import os

import controllers


class ViewsToBackup:
    """
    Method for all view of Backup_home_folders
    """

    def __init__(self):
        self.nb_repeat = 100
        self.clear = os.system("clear")

    def f_string_line(self, symbol: str = "", nb_up_1: str = "", nb_up_2: str = "") -> None:
        """
        Show an line of symbol
        """

        print(f"{nb_up_1}{symbol * self.nb_repeat}{nb_up_2}")

    def select_choice_menu(self) -> int:
        """
        Select of the choice of menu
        """

        self.f_string_line("=", "\n", "\n")
        print(f"{'':<20}{'[ Synchronization and restoration of folders ]'}")
        self.f_string_line("=", "\n", "\n\n\n")

        select_choice_menu = int(
            input(
                f"{'Select option of type de synchronization :'}\n{'-' * 42}\n\n"
                f"{'[ 1 ] Synchronization of folders'}\n"
                f"{'[ 2 ] Quit'}\n\n"
                f"- Select option : "
            )
        )

        self.f_string_line("#", "\n", "\n")

        return select_choice_menu

    def select_choice_user(self, list_users: list(dict())) -> str:
        """
        Select user
        """
        user_selected = ""

        print(f"Select user for the synchronization : \n{'-' * 37}\n")
        
        for id_user in list_users:
            print(f"[ {id_user['number_id']} ] {id_user['name']}")
        
        select_choice_user = int(input(f"\n- Select user : "))

        for user_select in list_users:
            
            if select_choice_user == user_select['number_id']:
                user_selected = user_select['name_id']

        return user_selected

    def f_string_path_of_source_and_destination(self) -> list:
        """
        Get the destination path
        """

        all_path = []

        self.f_string_line("#", "\n", "\n")

        os.system("lsblk -f")

        source = input("\n\n- Source directory path : ")
        destination = input("- Destination directory path : ")

        all_path.append(source)
        all_path.append(destination)

        self.f_string_line("#", "\n", "\n")

        return all_path

    def f_string_select_option_rsync(self) -> int:
        """
        Select option for rsync
        """

        select_option = "Select option for rsync :"

        choice = int(
            input(
                f"{select_option}\n{'-' * len(select_option)}\n\n"
                f"[ 1 ] Direct sync (Ext4)\n"
                f"[ 2 ] Dry-run sync (checking for differences) - (Ext4)\n"
                f"[ 3 ] Direct sync (Ntfs)\n"
                f"[ 4 ] Dry-run sync (checking for differences) - (Ntfs)\n\n"
                f"- Select option : "
            )
        )

        self.f_string_line("#", "\n", "\n")

        return choice

    def f_string_folder_sync(self, folder) -> None:
        """
        Folder synchronized
        """

        self.f_string_line("=", "\n\n")

        path_folder = f"> Synchronisation of folder '{folder}'"

        print(f"{'':<25}{path_folder:<25}\n" f"{'':<25}{'-' * len(path_folder)}\n")
        