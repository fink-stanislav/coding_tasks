
def timeConversion(s):
    hours = s[0:2]
    hours = int(hours)
    if 'PM' in s:
        if hours < 12:
            hours += 12
        s = str(hours) + s[2:]
    else:
        if hours == 12:
            s = "00" + s[2:]
    return s[:-2]
