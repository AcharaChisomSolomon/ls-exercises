DEGREE = "\u00B0"

def modify(num):
    return f"{num}" if num >= 10 else f"0{num}"

def dms(angle):
    degree = angle // 1
    degree_rem = angle - degree
    minutes_ = degree_rem * 60
    minutes = minutes_ // 1
    minutes_rem = minutes_ - minutes
    seconds_ = minutes_rem * 60
    seconds = seconds_ // 1

    return f"{int(degree)}{DEGREE}{modify(int(minutes))}'{modify(int(seconds))}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")