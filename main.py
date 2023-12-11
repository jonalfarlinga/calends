from keys import HOLIDAY_API_KEY
import docx
from datetime import datetime, timedelta


# find class dates between start, end, only on weekdays
def build_dates(start, end, weekdays):
    '''
    returns a dictionary
    {
        "dates": [
            "Mon 01",
            etc...
        ],
        "topic": [
            "blank",
            etc...
        ],
        "holidays": [
            "MLK Day",
            etc...
        ]
    }
    '''
    week_to_day = {
        'Sunday': 'u',
        'Monday': 'M',
        'Tuesday': 'T',
        'Wednesday': 'W',
        'Thursday': 'h',
        'Friday': 'F',
        'Saturday': 'S',
    }
    date = start
    day = timedelta(days=1)
    calendar = {
        "dates": ["Date"],
        "holidays": ["Holiday"],
    }
    while date <= end:
        if week_to_day[date.strftime('%A')] in weekdays:
            calendar['dates'].append(date.strftime('%b %d'))
            calendar['holidays'].append('')  # add logic for holidays
        date += day

    return calendar


# gets start(datetime(MM DD YY)) end(datetime(MM DD YY)) weekdays([uMTWhFS])
def get_input():
    weekdays = None
    start = None
    end = None

    while not weekdays:
        weekdays = input("\nWhich weekdays? Type a one letter code for each"
                         " day, with no spaces: [uMTWhFS]\n")
        for char in weekdays:
            if char not in "uMTWhFS":
                weekdays = None

    while not start:
        try:
            start = input("\nWhat is the first day of classes? MM DD YY\n")
            start = datetime.strptime(start, "%m %d %y")
        except ValueError:
            print("Bad Date")
            start = None

    while not end:
        try:
            end = input("\nWhat is the exam date? MM DD YY\n")
            end = datetime.strptime(end, "%m %d %y")
        except ValueError:
            print("Bad Date")
            start = None
    return start, end, weekdays


# ############
# MAIN TREE ##
# ############
if __name__ == "__main__":
    start, end, weekdays = get_input()  # get inputs
    class_dates = build_dates(start, end, weekdays)  # populate date list

    document = docx.Document('demo.docx')
    document.save("demo.docx")
