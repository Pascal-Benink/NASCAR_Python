import sys
import os

restart = "N"

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def commands():
    print("to get the current standings Use the command /Standings ")
    print("to close the app /exit ")

    command = input("Type Command here: ")

    if command == "/Standings" or command == "/exit":
        if command == "/Standings":
            print("The current NASCAR Standings are")
            commands()
        elif command == "/exit":
            print("program Offline")
    else:
        print("Command not found")
        commands()

print("Welcome to the Unofficial NASCAR info Python script")
commands()



