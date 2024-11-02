def timeConversion(s):
    # Extract the period (AM/PM)
    period = s[-2:]  # Last two characters
    # Extract the hour, minute, and second
    hour = int(s[:2])  # First two characters
    minute = s[3:5]
    second = s[6:8]

    # Convert hour based on AM/PM
    if period == 'AM':
        if hour == 12:
            hour = 0  # Midnight case
    else:  # PM case
        if hour != 12:
            hour += 12  # Convert to 24-hour format

    # Format hour to always have two digits
    military_time = f"{hour:02}:{minute}:{second}"
    return military_time


# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example


# Return '12:01:00'.


# Return '00:01:00'.

# Function Description

# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

# timeConversion has the following parameter(s):

# string s: a time in  hour format
# Returns

# string: the time in  hour format
# Input Format

# A single string  that represents a time in -hour clock format (i.e.:  or ).

# Constraints

# All input times are valid
# Sample Input

# 07:05:45PM
# Sample Output

# 19:05:45