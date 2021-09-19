def format_duration(seconds):
    if seconds == 0:
        return 'now'

    years, days, hours, mins, secs = 0, 0, 0, 0, 0

    years = seconds // (365 * 24 * 60 * 60)
    res = seconds - (years * 365 * 24 * 60 * 60)

    if res >= 86400:
        days = res // (24 * 60 * 60)
        res -= days * 24 * 60 * 60

    if res >= 3600:
        hours = res // (60 * 60)
        res -= hours * 60 * 60

    if res > 59:
        mins += res // 60
        secs = res % 60
    else:
        secs = res

    # time formatting

    lst = []
    if years >= 1:
        msg_years = f"{years} year{'s' if years > 1 else ''}"
        lst.append(msg_years)

    if days >= 1:
        msg_days = f"{days} day{'s' if days > 1 else ''}"
        lst.append(msg_days)

    if hours >= 1:
        msg_hours = f"{hours} hour{'s' if days > 1 else ''}"
        lst.append(msg_hours)

    if mins >= 1:
        msg_mins = f"{mins} minute{'s' if mins > 1 else ''}"
        lst.append(msg_mins)

    if secs >= 1:
        msg_secs = f"{secs} second{'s' if secs > 1 else ''}"
        lst.append(msg_secs)

    # display formatting
    msg = ''.join([(', ' if x != lst[-1] else ' and ') + str(x) for x in lst])

    return msg[2:]


# print(format_duration(3660))
print(format_duration(23423456))
