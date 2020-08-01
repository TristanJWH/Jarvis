import os
import time

default_path = "/home/tristan/Sync/Jarvis/remote-command/"


def remote_command_read(computer):
    f = open(f"{computer}", "r")
    command_number = f.read()[0]
    f.close()
    if command_number == "0":
        pass
    elif command_number == "1":
        f = open(f"{computer}", "w")
        f.write("0")
        f.close()
        time.sleep(2)
        os.system("poweroff")


def remote_command_write(command, computer):
    # Please be aware that you must create the computer.txt file yourself
    f = open(f"{default_path}{computer}.txt", "w")
    if command == "poweroff":
        command_number = "1"
    f.write(command_number)
    f.close()
