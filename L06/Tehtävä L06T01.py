#Lab06 Tehtävä 01

# calculate amount of hours, numbers and seconds
def showtime(time):
    hours = 0
    minutes = 0

    while time > 3600:
        time -= 3600
        hours += 1

    while time > 60:
        time -= 60
        minutes += 1

    seconds = time

#determine if hours and minutes are 10 or more 
    if hours >= 10 and minutes >= 10:
        print(f"{hours}:{minutes}:{seconds}")
    elif hours >= 10 and minutes <= 10:
        print(f"{hours}:0{minutes}:{seconds}")
    elif hours < 10 and minutes >= 10:
        print(f"0{hours}:{minutes}:{seconds}")
    else:
        print(f"0{hours}:0{minutes}:{seconds}")

#test the code
print(showtime(500))
print(showtime(10000))
print(showtime(121000))