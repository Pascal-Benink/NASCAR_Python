# import sys
# import os
# from getinfo import *
#
# restart = "N"
#
# def restart_program():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)
#
#
# def commands():
#     print("for help do /help or /?")
#     print("to close the app /exit ")
#
#     command = input("Type Command here: ")
#
#     if command == "/standings" or command == "/standings_name" or command == "/standings_best" or command == "/exit" or command == "/help" or command == "/?" or command == '/standings_manufacturer':
#         if command == "/standings":
#             get_info()
#             commands()
#         elif command == "/exit":
#             print("program Offline")
#         elif command == "/standings_name":
#             searchname = input("Input driver name here: ")
#             get_info_from_name(searchname)
#             commands()
#         elif command == "/standings_best":
#             get_info_best()
#             commands()
#         elif command == "/standings_manufacturer":
#             searchname = input("Input driver name here: ")
#             get_info_manufacturer()
#             commands()
#         elif command == "/help" or command == "/?":
#             print("to get the current standings Use the command /standings ")
#             print("to get the current standings filtered by name Use the command /standings_name ")
#             print("to get the current standings with highest points Use the command /standings_best ")
#             print("to get the current standings filtered by manufacturer Use the command /standings_manufacturer ")
#             commands()
#     else:
#         print("Command not found")
#         commands()
#
# print("Welcome to the Unofficial NASCAR info Python script")
# commands()

import sys
import os
from getinfo import *
restart = "N"
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def delete():
    delete_stand()
def get_standings():
    get_info()
def get_standings_name():
    searchname = input("Input driver name here: ")
    get_info_from_name(searchname)
def get_standings_best():
    get_info_best()
def get_standings_manufacturer():
    get_info_driver_manufacturer()
def add_comp():
    add_competitor()
def display_help():
    print("to get the current standings Use the command /standings ")
    print("to get the current standings filtered by name Use the command /standings_name ")
    print("to get the current standings with highest points Use the command /standings_best ")
    print("to get the current standings with the chosen manufacturer /standings_manufacturer ")
    print("Add a competitor to the database /add_comp ")
    print("Delete a competitor from the database /delete_standing ")
def exit_program():
    print("Program Offline")
    sys.exit()
commands_dict = {
    "/standings": get_standings,
    "/standings_name": get_standings_name,
    "/standings_best": get_standings_best,
    "/standings_manufacturer": get_standings_manufacturer,
    "/delete_standing": delete,
    "/add_comp": add_comp,
    "/help": display_help,
    "/?": display_help,
    "/exit": exit_program
}
def commands():
    print("for help do /help or /?")
    print("to close the app /exit ")
    command = input("Type Command here: ")
    command_function = commands_dict.get(command, None)
    if command_function:
        command_function()
        commands()
    else:
        print("Command not found")
        commands()
print("Welcome to the Unofficial NASCAR info Python script")
commands()