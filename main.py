#! /usr/bin/env python3
# coding:utf-8

import os
import sav_home_folder_by_rsync


def main():
    """
    Program entry point
    """

    os.system("clear")

    backup = sav_home_folder_by_rsync.BackupFolders()
    backup.backup_or_restore()
    backup.path_of_destination()
    backup.select_option_rsync()
    backup.synchronisation()


if __name__ == "__main__":
    main()
