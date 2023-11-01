import sys
from nascar_selenium import *
from getinfo import *

restart = "N"


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def custom_selecting():
    custom_select()


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


def update_standing():
    update()


def name_check():
    check_name()


def faker_null():
    insert_tester()


def updatecurrentstandings():
    getstandings_curent()


def updatecustomstandings():
    getstandings_custom()


# def deleteallstandings():
#     deleterallinfo()

def display_help():
    print("to get the current standings Use the command /standings ")
    print("to get the current standings filtered by name Use the command /standings_name ")
    print("to get the current standings with the highest points Use the command /standings_best ")
    print("to get the current standings with the chosen manufacturer /")
    print("Add a competitor to the database /add_comp ")
    print("Delete a competitor from the database /delete_standing ")
    print("Update a competitor from the database /update_standing ")
    print("to update the whole database with all the real information current please use /update_current_standings")
    print("to update the whole database with all the real information from a custom year please use "
          "/update_custom_standings")
    # print("to delete all standings use /delete_all_standings")
    print("Update a competitor from the database /update_standing ")
    print("to use multiple commands at a time type ; between the commands like /add_comp; /delete_standing")


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
    "/update_standing": update_standing,
    "/name_check": name_check,
    "/help": display_help,
    "/?": display_help,
    "/exit": exit_program,
    "/fakedata": faker_null,
    "/update_current_standings": updatecurrentstandings,
    "/update_custom_standings": updatecustomstandings,
    "/custom": custom_selecting,
    # "/delete_all_standings": deleteallstandings,
}


def commands():
    print("for help do /help or /?")
    print("to close the app /exit ")
    command = input("Type Command here: ")

    # Split the input into multiple commands using a delimiter (e.g., semicolon)
    commands_list = command.split(";")

    for single_command in commands_list:
        single_command = single_command.strip()  # Remove leading/trailing spaces

        # Execute each individual command
        command_function = commands_dict.get(single_command, None)
        if command_function:
            command_function()
        else:
            print(f"Command '{single_command}' not found")

    commands()


print("Welcome to the Unofficial NASCAR info Python script")
commands()
