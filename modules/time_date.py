import time


def time_date():
    days_of_the_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    month_of_the_year = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October ",
        "November",
        "December",
    ]
    current_time = []
    list = str(time.localtime(time.time()))
    list = list.replace("tm_", "")
    list = list.replace("time.struct_time(", "")
    list = list.replace(", isdst=1)", "")
    list = list.split(", ")
    for item in list:
        current_time.append(item.split("="))
    year = int(current_time[0][1])
    month_num = int(current_time[1][1])
    month = month_of_the_year[month_num - 1]
    mday = int(current_time[2][1])
    wday = int(current_time[6][1])
    day = days_of_the_week[wday]
    yday = int(current_time[7][1])
    hour = int(current_time[3][1])
    min = int(current_time[4][1])
    sec = int(current_time[5][1])
    current_time = []
    current_time.append(year)
    current_time.append(month_num)
    current_time.append(month)
    current_time.append(mday)
    current_time.append(wday)
    current_time.append(day)
    current_time.append(yday)
    current_time.append(hour)
    current_time.append(min)
    current_time.append(sec)
    # Returns a list with the time and date in all useful formats
    return current_time


def current_time():
    hour = int(time_date()[7])
    minute = int(time_date()[8])
    # Turning 8 to 08
    if minute < 10:
        minute = f"0{minute}"
    # Change to 12 hour time format
    if hour > 12:
        hour = hour - 12
        current_time = f"Currently it's is {str(hour)} {minute} P M"
    elif hour == 12:
        current_time = f"Currently it's is {str(hour)} {minute} P M"
    else:
        current_time = f"Currently it's {str(hour)} {minute} A M"
    # Returns the time in a 12 hour format
    return current_time


def current_date():
    nday = int(time_date()[3])
    if nday == 1:
        nday = "first"
    if nday == 2:
        nday = "second"
    if nday == 3:
        nday = "third"
    if nday == 4:
        nday = "forth"
    if nday == 5:
        nday = "fifth"
    if nday == 6:
        nday = "sixth"
    if nday == 7:
        nday = "seventh"
    if nday == 8:
        nday = "eighth"
    if nday == 9:
        nday = "ninth"
    if nday == 10:
        nday = "tenth"
    if nday == 11:
        nday = "eleventh"
    if nday == 12:
        nday = "twelfth"
    if nday == 13:
        nday = "thirteenth"
    if nday == 14:
        nday = "fourteenth"
    if nday == 15:
        nday = "fifteenth"
    if nday == 16:
        nday = "sixteenth"
    if nday == 17:
        nday = "seventeenth"
    if nday == 18:
        nday = "eighteenth"
    if nday == 19:
        nday = "nineteenth"
    if nday == 20:
        nday = "twentieth"
    if nday == 21:
        nday = "twenty first"
    if nday == 22:
        nday = "twenty second"
    if nday == 23:
        nday = "twenty third"
    if nday == 24:
        nday = "twenty forth"
    if nday == 25:
        nday = "twenty fifth"
    if nday == 26:
        nday = "twentysixth "
    if nday == 27:
        nday = "twenty seventh"
    if nday == 28:
        nday = "twenty eighth"
    if nday == 29:
        nday = "twenty ninth"
    if nday == 30:
        nday = "thirtieth"
    if nday == 31:
        nday = "thirty first"
    current_date = f"Currently it's {time_date()[5]} the {nday} of {time_date()[2]}"
    # Returns the date using a format with both date formats and month
    return current_date
