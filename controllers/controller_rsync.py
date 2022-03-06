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
        self.users_list = self.get_data_dict_users()
        self.user_selected = ""
        self.path_source_and_destination = []
        self.rsync_option = ""
        self.choice_menu = int()
        
    def menu(self) -> None:
        """
        Menu management
        """

        while True:
            
            self.choice_menu = self.views.select_choice_menu()

            if self.choice_menu == 1:
                self.user_selected = self.views.select_choice_user(self.users_list)
                self.path_source_and_destination = self.views.f_string_path_of_source_and_destination()
                self.path_source_and_destination[0] = f"{self.path_source_and_destination[0]}/{self.user_selected}/"
                self.path_source_and_destination[1] = f"{self.path_source_and_destination[1]}/{self.user_selected}/"
                self.select_option_rsync()
                self.synchronisation()

            if self.choice_menu == 2:
                break                

    def get_data_dict_users(self) -> list[dict]:
        """
        get users data base
        """

        users_list = []

        with open("bdd_users/list_users.json", "r", encoding='utf-8') as file:
            data = json.load(file)
            
            for user in data["users"]:
                users_list.append(user)

        return users_list

    def select_option_rsync(self) -> None:
        """
        Select option for rsync
        """

        choice = self.views.f_string_select_option_rsync()

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
        Synchronized the folders user
        """

        os.system(
            f"rsync {self.rsync_option} --delete --exclude='.*/' --exclude='.*' {self.path_source_and_destination[0]} "
            f"{self.path_source_and_destination[1]}"
                )

        self.views.f_string_line("=", "", "\n\n\n")
