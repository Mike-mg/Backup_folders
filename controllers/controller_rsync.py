#! /usr/bin/env python3
# coding:utf-8

"""
Save and restore all folders user
"""

import json
import os

import views


class ControllerBackupFolders:
    """
    Class that save all folder (important) user
    """

    def __init__(self):

        os.system("clear")
        self.views = views.ViewsToBackup()
        self.choice_menu = int()
        self.user = ""
        self.user_list = []
        self.source_destination = ()
        self.rsync_option = ""
        self.folders_selected = []

    def menu(self) -> None:
        """
        Menu management
        """

        while True:

            self.choice_menu = self.views.select_choice_menu()

            if self.choice_menu == 1:
                self.user = self.views.get_users(self.get_data_dict_users())
                self.source_destination = self.views.get_path_source_and_destination()
                self.folders_selected = self.views.folders_backup_selected(
                    self.source_destination[0]
                )
                self.select_option_rsync()
                self.synchronisation()
                if self.views.next_or_not() == 1:
                    break
                os.system("clear")

            elif self.choice_menu == 2:
                break

    def get_data_dict_users(self) -> list[dict]:
        """
        get users data base
        """

        with open("data_base/list_users.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            for user in data["users"]:
                self.user_list.append(user)

        return self.user_list

    def select_option_rsync(self) -> None:
        """
        Select option for rsync
        """

        choice = self.views.select_option_rsync()

        if choice == 0:
            self.rsync_option = "-avh"
        elif choice == 1:
            self.rsync_option = "-navh"
        elif choice == 2:
            self.rsync_option = "-rtlogvh"
        elif choice == 3:
            self.rsync_option = "-rtlongvh"

    def synchronisation(self) -> None:
        """
        Synchronized the folders user
        """

        for folder in self.folders_selected:
            if " " in folder:
                folder = f"'{folder}'"
            self.views.folder_sync(folder)

            os.system(
                f"rsync {self.rsync_option} --delete "
                f"{self.source_destination[0]}/{folder}/ {self.source_destination[1]}/{folder}/"
            )


# nb line = 108, 98
