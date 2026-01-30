def convertSecondsSinceMidnight(secondsSinceMidnight):
    # Validate input
    if not isinstance(secondsSinceMidnight, int) or secondsSinceMidnight < 0 or secondsSinceMidnight >= 86400:
        return "Invalid input: seconds must be an integer between 0 and 86399"

    # Calculate hours, minutes, and seconds
    hours = secondsSinceMidnight // 3600
    remainingSeconds = secondsSinceMidnight % 3600
    minutes = remainingSeconds // 60
    seconds = remainingSeconds % 60

    # Determine AM or PM
    if hours < 12:
        period = "AM"
    else:
        period = "PM"

    # Convert 
    if hours == 0:
        displayHours = 12
    elif hours > 12:
        displayHours = hours - 12
    else:
        displayHours = hours

    return f"{displayHours} {minutes} {seconds} {period}"


def main():
    print(convertSecondsSinceMidnight(19067))  # Example


main()
