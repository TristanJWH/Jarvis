import re
import os
import random as rand

def relative_volume(querry, device):
    amount = querry.split("by")[-1]
    amount = amount.replace("percent", "")
    amount = amount.replace(" ", "")
    if re.search("up", querry) != None:
        command = f"pactl set-sink-volume {device} +{amount}"
        print(command)
        os.system(command)
    else:
        command = f"pactl set-sink-volume {device} -{amount}"
        print(command)
        os.system(command)
    random = rand.randint(0,2)
    if random == 0:
        return "done"
    elif random == 1:
        return "okay"
    elif random == 2:
        return "affirmative"

def absolute_volume(querry, device):
    amount = querry.split("to")[-1]
    amount = amount.replace("percent", "")
    amount = amount.replace(" ", "")
    os.system(f"pactl set-sink-volume {device} {amount}")
    print(f"pactl set-sink-volume {device} {amount}")
    random = rand.randint(0,2)
    if random == 0:
        return "done"
    elif random == 1:
        return "okay"
    elif random == 2:
        return "affirmative"