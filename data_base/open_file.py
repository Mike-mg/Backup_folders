#! /usr/bin/env python3
# coding:utf-8

"""
Class for read the file of data_base
"""

import json
import os


class OpenFile:

    """
    Class for read the file of data_base

    """

    def __init__(self) -> None:
        self.user = ""
        self.path_source = ""
        self.path_destination = ""
        self.list_users = "data_base/list_users.json"
        self.lsblk = "data_base/lsblk.json"

    def open_file_lsblk_path(self):
        """
        Read the informations of file
        """

        print(f"\n\n{'#' * 100}\n\n")

        while True:

            os.system("lsblk -J > data_base/lsblk.json")

            disk_mount = []

            with open("data_base/lsblk.json", "r", encoding="UTF-8") as file:
                data = json.load(file)

                for disk in data["blockdevices"]:

                    if "sd" in disk["name"]:
                        for index, path_disk in enumerate(disk["children"]):
                            if path_disk["mountpoints"][0] == "/home":
                                disk_mount.append(
                                    f"{path_disk['mountpoints'][0]}/{self.user}"
                                )

                            elif path_disk["mountpoints"][0] is not None:
                                disk_mount.append(path_disk["mountpoints"][0])

            string_select_folder = "Source and destination path : "
            print(f"{string_select_folder}\n{'-' * len(string_select_folder)}\n")

            for index, path_disk_mount in enumerate(disk_mount):
                print(f"[ {index} ] {path_disk_mount}")

            choice_path_source = int(input("\n- Select the source : "))
            choice_path_destination = int(input("- Select the destination : "))

            self.path_source = disk_mount[choice_path_source]
            self.path_destination = disk_mount[choice_path_destination]
            print(f"\n\n{'#' * 100}\n\n")

            return f"{self.path_source}", f"{self.path_destination}/{self.user}"

    def open_file_user_list(self) -> str:
        """
        get user
        """
        title = "Selected an user of the list users :"

        print(f"{title}\n{'-' * len(title)}\n")

        with open(self.list_users, "r", encoding="utf-8") as file:
            data = json.load(file)

            for index, user in enumerate(data["users"]):
                print(f"[ {index} ] {user['name']}")

            choice_user_name = int(input("\nSelected user : "))
            self.user = data["users"][choice_user_name]["name_id"]

        return self.user
