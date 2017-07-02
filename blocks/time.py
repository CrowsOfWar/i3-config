import datetime
now = datetime.datetime.now()
format = now.strftime('%I:%M %p')
print(format)