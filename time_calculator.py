def add_time(start, duration, weekday=None):
    
    weekdays_dict = {"monday":0, "tuesday":1 ,"wednesday":2 ,"thursday":3 ,"friday":4,"saturday":5,"sunday":6}
    time_states = 'AM'  #set time state to 'AM' as default (change to PM later in codes)

    start_array = start.split(' ')
    start_time = start_array[0].split(':')

    duration_time = duration.split(':')


    #Add the hours together (start + end)
    add_hours = (int(start_time[0])+int(duration_time[0]))

    #Add 12 hours to the added hours in case it's 'PM' (so we can work with a 24h format and convert it back to 12h format) 
    if start_array[1] == "PM":
        add_hours += 12

    #Add the minutes together (start + end)
    add_mins = (int(start_time[1])+int(duration_time[1]))

    #If the sum of minutes > 59, add one hour to the added hours
    if(add_mins > 59):
        add_hours += 1

    #Calculate the ending minute
    end_min = add_mins % 60

    #Calculate the ending hour
    end_hour = add_hours % 24

    #If the ending hour reaches 12th hour or more, change 'AM' to 'PM'
    if end_hour > 11:
        time_states = 'PM'

    #Convert back to 12h format
    if end_hour > 12:
        end_hour -= 12
    elif end_hour == 0:     #in case it's midnight, convert it from 0 to 12
        end_hour = 12
    
    #Combine all the first extracted parts into one string
    end_time = str(end_hour) + ':' + str(end_min).zfill(2) + ' ' + time_states

    #Count the number of days passing after the specified duration
    day_num = int(add_hours//24)

    #If the weekday option is given, add the updated weekday to the string
    if weekday != None:
        weekday = weekday.lower()
        #Get value from the key for calculation of the number of days
        weekday_num = weekdays_dict[weekday]
        new_weekday_num = (day_num + weekday_num) % 7
        #Get key (which weekday) by its value
        new_weekday = list(weekdays_dict.keys())[list(weekdays_dict.values()).index(new_weekday_num)]
        end_time += ', ' + new_weekday.capitalize()

    #If the day has changed, add the correct the string value
    if day_num == 1:
        end_time += ' (next day)'
    elif day_num > 1:
        end_time += ' (' + str(day_num) + ' days later)'
    
    return end_time
