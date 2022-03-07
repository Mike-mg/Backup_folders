#! /usr/bin/env python3
# coding:utf-8

"""
Program entry point
"""


import controllers


def main():
    """
    Program entry point
    """
    start_main = controllers.ControllerBackupFolders()
    start_main.menu()


if __name__ == "__main__":
    main()
