#! /usr/bin/env python3
# coding:utf-8

"""
Method views of Backup home folders
"""


import json
import os


class ViewsToBackup:
    """
    Method for all view of Backup_home_folders
    """

    def __init__(self):
        self.nb_repeat = 100
        self.user = os.getlogin()
        self.path_source = ""
        self.path_destination = ""
        self.folders_selected = []

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

        self._line("#", "\n\n", "\n\n")

        return select_choice_menu

    def sub_menu(self, title_sub_menu: str, *args: str) -> int:
        """
        show sub menu
        """

        self._line("#", "\n\n", "\n\n")

        string_sub_menu = title_sub_menu
        sub_text = args
        nb_range = len(sub_text)
        print(f"{string_sub_menu}\n{'-' * len(string_sub_menu)}\n")

        for i in range(0, nb_range):
            print(f"[ {i} ] {sub_text[i]}")

        choice_sub_menu = int(input("- Select option : "))

        self._line("#", "\n\n", "\n\n")

        return choice_sub_menu

    def next_or_not(self) -> int:
        """
        Select if continue program
        """

        return self.sub_menu(
            "Continue program or not :",
            "Yes",
            "No (Quit program)\n",
        )

    def folders_backup_selected(self, folder_source) -> list:
        """
        Select folder for sync
        """

        list_folders_of_path = os.listdir(folder_source)
        folders_for_sync = []
        string_select_folder = "Which folders should be synchronized :"

        print(f"{string_select_folder}\n{'-' * len(string_select_folder)}\n")

        for folder in list_folders_of_path:
            if "." not in folder:
                folders_for_sync.append(folder)

        for index, folder in enumerate(folders_for_sync):
            print(f"[ {index} ] {folder}")

        print(f"[ {len(folders_for_sync)} ] All folders")

        choice_folders = input("\n- Selecting folders and files (Ex: 1,2,3,4): ")
        choice_folders = choice_folders.split(",")
        choice_folders = [int(i) for i in choice_folders]

        if choice_folders[0] == len(folders_for_sync):
            self.folders_selected = folders_for_sync
        else:
            for folder in choice_folders:
                self.folders_selected.append(folders_for_sync[folder])

        return self.folders_selected

    def get_users(self, list_users: list({})):
        """
        Get users
        """

        print(f"Select user for the synchronization : \n{'-' * 37}\n")

        for id_user in list_users:
            print(f"[ {id_user['number_id']} ] {id_user['name']}")

        select_choice_user = int(input("\n- Select user : "))

        for user_select in list_users:

            if select_choice_user == user_select["number_id"]:
                self.user = user_select["name_id"]
        return self.user

    def get_path_source_and_destination(self) -> tuple:
        """
        Get users and the source/destination path
        """

        while True:

            self._line("#", "\n\n", "\n\n")

            os.system("lsblk -J > data_base/lsblk.json")

            disk_mount = []
            with open("data_base/lsblk.json", "r", encoding="UTF-8") as file:
                data = json.load(file)

                for disk in data["blockdevices"]:

                    if "sd" in disk["name"]:
                        for index, path_disk in enumerate(disk["children"]):
                            if path_disk["mountpoints"][0] == "/home":
                                disk_mount.append(
                                    f"{path_disk['mountpoints'][0]}/{self.user}"
                                )

                            elif path_disk["mountpoints"][0] is not None:
                                disk_mount.append(path_disk["mountpoints"][0])

            string_select_folder = "Source and destination path : "
            print(f"{string_select_folder}\n{'-' * len(string_select_folder)}\n")

            for index, path_disk_mount in enumerate(disk_mount):
                print(f"[ {index} ] {path_disk_mount}")

            choice_path_source = int(input("\n- Select the source : "))
            choice_path_destination = int(input("- Select the destination : "))

            self.path_source = disk_mount[choice_path_source]
            self.path_destination = disk_mount[choice_path_destination]
            self._line("#", "\n\n", "\n\n")

            return f"{self.path_source}", f"{self.path_destination}/{self.user}"

    def select_option_rsync(self) -> int:
        """
        Select option for rsync
        """

        return self.sub_menu(
            "Select option for rsync :",
            "Direct sync (Ext4)",
            "Dry-run sync (checking for differences) - (Ext4)",
            "Direct sync (Ntfs)",
            "Dry-run sync (checking for differences) - (Ntfs)\n",
        )

    def folder_sync(self, folder) -> None:
        """
        Folder synchronized
        """

        self._line("=", "\n\n")

        path_folder = f"> Synchronisation of folder '{folder}'"

        print(f"{'':<25}{path_folder:<25}\n" f"{'':<25}{'-' * len(path_folder)}\n")


# nb line = 180, 194
