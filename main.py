#! /usr/bin/env python3
# coding:utf-8

"""
Program entry point
"""


import controllers


class Main:
    """
    Entry point
    """

    def __init__(self):
        self.controllers = controllers.ControllerBackupFolders()


    def main(self):
        """
        Program entry point
        """
        
        self.controllers.menu()


if __name__ == "__main__":
    main = Main()
    main.main()