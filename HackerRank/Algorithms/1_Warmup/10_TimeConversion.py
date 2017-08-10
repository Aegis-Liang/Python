time = "07:05:45PM"

result = ""
if time[-2:] == "PM":
    if time[0:2] == "12":
        result = time[0:-2]
    else:
        result = str(int(time[0:2])+12) + time[2:-2]
else:
    if time[0:2] == "12":
        result = "00" + time[2:-2]
    else:
        result = time[0:-2]
print result
    