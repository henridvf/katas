def format_duration(seconds):

    if seconds == 0:
        return 'now'

    years, days, hours, mins, secs = 0, 0, 0, 0, 0

    years = seconds // (365 * 24 * 60 * 60)
    res = seconds - (years * 365 * 24 * 60 * 60)

    if res > 86400:
        days = res // (24 * 60 * 60)
        res -= days * 24 * 60 * 60

    if res > 3600:
        hours = res // (60 * 60)
        res -= hours * 60 * 60

    if res > 0:
        mins = res // 60
        res -= mins * 60

    if res > 59:
        mins += res // 60
        secs = res % 60
    else:
        secs = res

    # time formatting
    msg_years, msg_days, msg_hours, msg_mins, msg_secs = '','','','',''
    has_years, has_days, has_hours, has_mins, has_secs = False, False, False, False, False

    if years >= 1:
        msg_years = f"{years} year{'s' if years > 1 else ''}"
        has_years = True;

    if days >= 1:
        msg_days = f"{days} day{'s' if days > 1 else ''}"
        has_days = True

    if hours >= 1:
        msg_hours = f"{hours} hour{'s' if days > 1 else ''}"
        has_hours = True

    if mins >= 1:
        msg_mins = f"{mins} minute{'s' if mins > 1 else ''}"
        has_mins = True

    if secs >= 1:
        msg_secs = f"{secs} second{'s' if secs > 1 else ''}"
        has_secs = True


    # display formatting

    msg = f"{msg_years}, {msg_days}, {msg_hours}, {msg_mins}, {msg_secs}"

    return msg, years, days, hours, mins, secs


print(format_duration(90062))
