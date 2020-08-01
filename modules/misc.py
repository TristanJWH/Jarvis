import random as rand
import os
from modules.speak_listen import listen


def poweroff():
    # Returns one of a few powering off responses
    # NOTE: It does not actually poweroff the device
    random = rand.randint(0, 3)
    if random == 0:
        return "powering off"
    elif random == 1:
        return "okay"
    elif random == 2:
        return "affirmative"
    elif random == 3:
        return "check"


def go_to_sleep():
    # Puts the program to sleep so it refuses commands
    querry = ""
    while "awake" or "wake up" not in querry:
        # querry = listen()
        print("I am asleep")
        querry = listen()
        if "awake" in querry:
            random = rand.randint(0, 1)
            if random == 0:
                return "yes"
            elif random == 1:
                return "for you, always"
        if "wake up" in querry:
            return "waking up"


def os_command(program, workspace=None):
    random = 0
    if workspace != None:
        os.system(f"wmctrl -s {workspace}")
    os.system(f"{program}")
    random = rand.randint(0, 3)
    if random == 0:
        return "opening"
    elif random == 1:
        return "okay"
    elif random == 2:
        return "affirmative"
    elif random == 3:
        return "check"


def play_sound(path):
    random = rand.randint(0, 1)
    os.system(f"play {path}")
    if random == 0:
        return "okay"
    elif random == 1:
        return "affirmative"
