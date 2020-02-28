import datetime

#Get birth date
birthday = int(input("Enter day of birth (1-31): "))
birthmonth = int(input("Enter month of birth (1-12): "))
birthyear = int(input("Enter year of birth (4-digit): "))

#Current Date 

currentday = datetime.date.today().day
currentmonth = datetime.date.today().month
currentyear = datetime.date.today().year



#Calculate Averages

day = 24*60*60
year = 52*day
avgyear = ((4*year)+ day)//4
avgmonth = avgyear//12

# Output

print ("number of seconds in day", day)
print ("number of seconds in month",avgmonth)
print ("number of seconds in a year", avgyear)

# Calculate age in seconds

dob = ((birthyear-1900)*avgyear)+ ((birthmonth-1)* avgmonth) + (birthday * day)

today = ((currentyear - 1900) * avgyear) + ((currentmonth - 1) * avgmonth) + (currentday * day)
print (today)
print (dob)

agesecs = today - dob

#
print ("You are approximately", agesecs, "seconds old")




