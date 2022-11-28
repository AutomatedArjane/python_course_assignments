#Lab10 Tehtävä 03

# create variable
year = int(input("Insert year: "))

if year % 4 == 0: # is the year divisible by 4?
    if year % 100 == 0: # is the year a full century?
        if year % 400 == 0: # if yes, is the year divisible by 400?
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year!")            
    else:
        print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")