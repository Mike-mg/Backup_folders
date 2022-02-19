#! /usr/bin/env python3
# coding:utf-8

import os


class ViewsBackup:
    """
    Method for all view of Backup_home_folders
    """

    def __init__(self):
        self.nb_lines = f"{'=' * 50}"

    def f_string_head(self) -> None:
        """
        Head string the program
        """

        print(
            f"\n\n{self.nb_lines}\n\n"
            f"[ Synchronisation of folder '/home/{os.getlogin()}/' ]\n\n"
            f"{self.nb_lines}\n\n"
        )

    def f_string_lines(self):
        print(f"\n{self.nb_lines}\n\n")

    def backup_or_restore(self) -> int:

        choice_backup_or_restore = int(
            input(
                f"{'Select option of type de synchronisation :'}\n\n"
                f"\t{'[ 1 ] Backup of laptop to SSD'}\n"
                f"\t{'[ 2 ] Restore from SSD to laptop'}\n\n"
                f"- Select option : "
            )
        )

        return choice_backup_or_restore
