#! /usr/bin/env python3
# coding:utf-8

"""
Method views of Backup home folders
"""


import os


class ViewsToBackup:
    """
    Method for all view of Backup_home_folders
    """

    def __init__(self):
        self.nb_repeat = 100
        self.clear = os.system("clear")

    def _line(self, symbol: str = "", nb_up_1: str = "", nb_up_2: str = "") -> None:
        """
        Show an _line of symbol
        """

        print(f"{nb_up_1}{symbol * self.nb_repeat}{nb_up_2}")

    def select_choice_menu(self) -> int:
        """
        Select of the choice of menu
        """

        self._line("=", "\n", "\n")
        print(f"{'':<20}{'[ Synchronization and restoration of folders ]'}")
        self._line("=", "\n", "\n\n\n")

        select_choice_menu = int(
            input(
                f"{'Select option of type de synchronization :'}\n{'-' * 42}\n\n"
                f"{'[ 1 ] Synchronization of folders'}\n"
                f"{'[ 2 ] Quit'}\n\n"
                f"- Select option : "
            )
        )

        self._line("#", "\n", "\n")

        return select_choice_menu

    def select_choice_user(self, list_users: list({})) -> str:
        """
        Select user
        """
        user_selected = ""

        print(f"Select user for the synchronization : \n{'-' * 37}\n")

        for id_user in list_users:
            print(f"[ {id_user['number_id']} ] {id_user['name']}")

        select_choice_user = int(input("\n- Select user : "))

        for user_select in list_users:

            if select_choice_user == user_select["number_id"]:
                user_selected = user_select["name_id"]

        return user_selected

    def next_or_not(self) -> int:
        """
        Select if continue program
        """

        string_option_next = "Continue program or not :"

        select_next_option = int(
            input(
                f"{string_option_next}\n{'-' * len(string_option_next)}\n\n"
                f"{'[ 1 ] Yes'}\n"
                f"{'[ 2 ] No (Quit program)'}\n\n"
                f"- Select option : "
            )
        )

        os.system("clear")

        return select_next_option

    def folders_backup_selected(self, folder_source):
        """
        Select folder for sync
        """

        list_folders_of_path = os.listdir(folder_source)
        folders_for_sync = []
        folders_selected = []

        string_select_folder = "Which folders should be synchronized :"

        print(f"{string_select_folder}\n{'-' * len(string_select_folder)}\n")

        for folder in list_folders_of_path:
            if "." not in folder:
                folders_for_sync.append(folder)

        for index, folder in enumerate(folders_for_sync):
            print(f"[ {index} ] {folder}")

        print(f"[ {len(folders_for_sync)} ] All folders")

        choice_folders = input("\n\n- Selecting folders and files (Ex: 1,2,3,4): ")

        if int(choice_folders) == len(folders_for_sync):
            for folder in folders_for_sync:
                folders_selected.append(folder)

        else:
            choice_folders = choice_folders.split(",")

            for choice in choice_folders:
                folders_selected.append(folders_for_sync[int(choice)])

        self._line("#", "\n", "\n")

        return folders_selected

    def path_of_source_and_destination(self) -> list:
        """
        Get the destination path
        """

        all_path = []

        self._line("#", "\n", "\n")

        os.system("lsblk -f")

        source = input("\n\n- Source directory path : ")
        destination = input("- Destination directory path : ")

        all_path.append(source)
        all_path.append(destination)

        self._line("#", "\n", "\n")

        return all_path

    def select_option_rsync(self) -> int:
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

        self._line("#", "\n", "\n")

        return choice

    def folder_sync(self, folder) -> None:
        """
        Folder synchronized
        """

        self._line("=", "\n\n")

        path_folder = f"> Synchronisation of folder '{folder}'"

        print(f"{'':<25}{path_folder:<25}\n" f"{'':<25}{'-' * len(path_folder)}\n")
