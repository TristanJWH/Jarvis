import modules.time_date

def left(file_path):
    # Append to a csv file with a time date stamp and leaving
    record = open(file_path, "r")
    leaving_record = record.read()
    record.close()
    if leaving_record.split("\n")[-1] == "":
        time = f"{time_date()[0]},{time_date()[1]},{time_date()[3]},{time_date()[7]},{time_date()[8]},"
        record = open(file_path, "a")
        record.write(f"Leaving,{time}")
        record.close()
        random = rand.randint(0,3)
        if random == 0:
            return "recorded"
        elif random == 1:
            return "okay"
        elif random == 2:
            return "affirmative"
        elif random == 3:
            return "done"
    else:
        return "You are not recorded as being back yet"

def back(file_path):
    # Append to a csv file with a time date stamp and back
    record = open(file_path, "r")
    leaving_record = record.read()
    record.close()
    if "Leaving" in leaving_record.split("\n")[-1]:
        time = f"{time_date()[0]},{time_date()[1]},{time_date()[3]},{time_date()[7]},{time_date()[8]}\n"
        record = open(file_path, "a")
        record.write(f"Back,{time}")
        record.close()
        random = rand.randint(0,3)
        if random == 0:
            return "recorded"
        elif random == 1:
            return "okay"
        elif random == 2:
            return "affirmative"
        elif random == 3:
            return "done"
    else:
        return "You are not recorded as having left"