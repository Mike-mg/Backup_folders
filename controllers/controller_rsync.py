#! /usr/bin/env python3
# coding:utf-8

"""
Save and restore all folders user
"""

import os

import views
import data_base


class ControllerBackupFolders:
    """
    Class that save all folder (important) user
    """

    def __init__(self):

        os.system("clear")
        self.views = views.views_backup.ViewsToBackup()
        self.open_file = data_base.open_file.OpenFile()
        self.choice_menu = int()
        self.user = ""
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

                self.open_file.open_file_user_list()
                self.source_destination = self.open_file.open_file_lsblk_path()
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
