def add_time(start, duration, starting_day=""):
    
    pieces = start.split() # pieces = 3:30 , PM
    time = pieces[0].split(":") # time = 3 , 30
    abbreviation = pieces[1] # abbreviation = PM

    # Calculate 24-hour clock format
    if abbreviation == "PM" :
        hour = int(time[0]) + 12 # Has to be int for calculations
        time[0] = str(hour)
    
    # Separate the duration into hours and minutes
    dur_time = duration.split(":") #Same we do in 'time'

    # Add hours and minutes
    new_hour = int(time[0]) + int(dur_time[0])
    new_minutes = int(time[1]) + int(dur_time[1])

    if new_minutes >= 60 :
        """ // -> Floor Division - The division of operands where the result is
        the quotient in which the digits after the decimal point are removed.
        But if one of the operands is negative, the result is floored."""
        hours_add = new_minutes // 60
        new_minutes -= hours_add * 60
        new_hour += hours_add

    days_add = 0
    if new_hour > 24 :
        days_add = new_hour // 24
        new_hour -= days_add * 24
    
    # Find AM and PM
    # When we have the operations done we return to 12-hour clock format
    if new_hour > 0 and new_hour < 12 :
        abbreviation = "AM"
    elif new_hour == 12 :
        abbreviation = "PM"
    elif new_hour > 12 :
        abbreviation = "PM"
        new_hour -= 12
    else : # new_hour == 0
        abbreviation = "AM"
        new_hour += 12

    if days_add > 0 :
        if days_add == 1 :
            days_later = " (next day)"
        else :
            days_later = " (" + str(days_add) + " days later)"
    else :
        days_later = ""

    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    if starting_day :
        weeks = days_add // 7
        i = week_days.index(starting_day.lower().capitalize()) + (days_add - 7 * weeks)
        if i > 6 :
            i -= 7
        day = ", " + week_days[i]
    else :
        day = ""
    
    new_time = str(new_hour) + ":" + \
        (str(new_minutes) if new_minutes > 9 else ("0" + str(new_minutes))) + \
        " " + abbreviation + day + days_later
    
    return new_time