import sys
import os
from getinfo import get_info
from getinfo import get_info_from_name
from getinfo import get_info_best

restart = "N"

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def commands():
    print("for help do /help or /?")
    print("to close the app /exit ")

    command = input("Type Command here: ")

    if command == "/standings" or command == "/standings_name" or command == "/standings_best" or command == "/exit" or command == "/help" or command == "/?":
        if command == "/standings":
            get_info()
            commands()
        elif command == "/exit":
            print("program Offline")
        elif command == "/standings_name":
            searchname = input("Input driver name here: ")
            get_info_from_name(searchname)
            commands()
        elif command == "/standings_best":
            get_info_best()
            commands()
        elif command == "/help" or command == "/?":
            print("to get the current standings Use the command /standings ")
            print("to get the current standings filtered by name Use the command /standings_name ")
            print("to get the current standings with highest points Use the command /standings_best ")
            commands()
    else:
        print("Command not found")
        commands()

print("Welcome to the Unofficial NASCAR info Python script")
commands()
