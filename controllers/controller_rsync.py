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

        self.views = views.ViewsToBackup()
        self.users_list = self._get_data_dict_users()
        self.source_destination = ()
        self.rsync_option = ""
        self.choice_menu = int()
        self.folders_selected = []

    def menu(self) -> None:
        """
        Menu management
        """

        while True:

            self.choice_menu = self.views.select_choice_menu()

            if self.choice_menu == 1:

                self.source_destination = self.views.get_user_user_and_path_source_and_destination(self.users_list)

                self.folders_selected = self.views.folders_backup_selected(
                    self.source_destination[0]
                )
                self._select_option_rsync()
                os.system('clear')
                self._synchronisation()
                
                self.choice_menu = self.views.next_or_not()
                if self.choice_menu == 1:
                    os.system('clear')
                    break

            if self.choice_menu == 2:
                break

    def _get_data_dict_users(self) -> list[dict]:
        """
        get users data base
        """

        users_list = []

        with open("data_base/list_users.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            for user in data["users"]:
                users_list.append(user)

        return users_list

    def _select_option_rsync(self) -> None:
        """
        Select option for rsync
        """

        choice = self.views.select_option_rsync()

        if choice == 1:
            self.rsync_option = "-avh"
        elif choice == 2:
            self.rsync_option = "-navh"
        elif choice == 3:
            self.rsync_option = "-rtlogvh"
        elif choice == 4:
            self.rsync_option = "-rtlongvh"

    def _synchronisation(self) -> None:
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

# nb line = 108