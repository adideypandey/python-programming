from datetime import datetime
today =datetime.now()
print(today)
dt=today.strftime("%B %d, %Y %H:%M:%S")
print("Current date and time : ",dt)