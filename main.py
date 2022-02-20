#! /usr/bin/env python3
# coding:utf-8

"""
Program entry point
"""

import os
import controllers


def main():
    """
    Program entry point
    """

    os.system("clear")

    backup = controllers.ControllerBackupFolders()
    backup.backup_or_restore()
    backup.path_of_destination()
    backup.select_option_rsync()
    backup.synchronisation()


if __name__ == "__main__":
    main()
