duration = int(input("Please enter a duration in seconds "))
hours = duration // 3600
minutes = (duration - (hours * 3600)) // 60
seconds = (duration - (hours * 3600) - (minutes * 60))
print("%d hour(s) %d minute(s) %d sec(s)" % (hours, minutes, seconds))
