def milsec_to_hour(milsec):
    sec = milsec // 1000
    sec, min = sec % 60, sec // 60
    min, hour= min % 60, min // 60
    result = f"{bool(hour) * str(hour)}{bool(hour) * ' hour/s '}\
{bool(min) * str(min)}{bool(min) * ' minute/s '}\
{bool(sec) * str(sec)}{bool(sec) * ' second/s'}"

    return f'just {milsec} milisecond/s' if milsec < 1000 else result

print(milsec_to_hour(999))