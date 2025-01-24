MINUTES_IN_A_DAY = 1440
MINUTES_IN_AN_HOUR = 60

def modify(num):
    return f"{'0' if num < 10 else ''}{num}"

def get_total_minutes(val):
    return val % MINUTES_IN_A_DAY

def time_of_day(num):
    total_minutes = get_total_minutes(num)
    hours = total_minutes // MINUTES_IN_AN_HOUR
    minutes = total_minutes - (hours * MINUTES_IN_AN_HOUR)
    return f"{modify(hours)}:{modify(minutes)}"


print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True