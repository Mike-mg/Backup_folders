#! /usr/bin/env python3
# coding:utf-8

"""
Save and restore all folders user
"""

import os
import views


class ControllerBackupFolders:
    """
    Class that save all folder (important) user
    """

    def __init__(self):
        self.views = views.ViewsToBackup()
        self.name_home_user = f"/home/{os.getlogin()}/"
        self.path = ""
        self.rsync_option = ""
        self.type_synchronisation = int()
        self.folders = [
            "Documents",
            "GitHub",
            "Images",
            "Mes_projets",
            "OC_DA_Python",
            "Téléchargements",
            "Vidéos",
        ]
        self.views.f_string_head()

    def backup_or_restore(self) -> None:
        """
        Select option of type de synchronisation
        """
        self.type_synchronisation = self.views.f_string_backup_or_restore()

    def path_of_destination(self) -> None:
        """
        Get the destination path
        """
        self.path = self.views.f_string_path_of_destination(self.folders)

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
        Rsync the folder user (sync laptop to ssd disk) if self.type_synchronisation = 1
        Rsync the folder user (sync ssd disk to laptop) if self.type_synchronisation = 2
        """

        if self.rsync_option in ("-rtlogvh", "-rtlongvh"):
            self.folders.remove("Images")

        for folder in self.folders:

            self.views.f_string_folder_sync(folder)

            if self.type_synchronisation == 1:
                os.system(
                    f"rsync {self.rsync_option} --delete /home/{os.getlogin()}/{folder}/ "
                    f"{self.path}/{os.getlogin()}/home_mike/{folder}/"
                )

                self.views.f_string_lines()

            if self.type_synchronisation == 2:
                os.system(
                    f"rsync {self.rsync_option} {self.path}/{os.getlogin()}/home_mike/{folder}/ "
                    f"{self.name_home_user}/{folder}/"
                )

                self.views.f_string_lines()
