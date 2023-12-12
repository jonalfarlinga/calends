# from keys import HOLIDAY_API_KEY
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
        'Sunday': 'S',
        'Monday': 'M',
        'Tuesday': 'T',
        'Wednesday': 'W',
        'Thursday': 'R',
        'Friday': 'F',
        'Saturday': 'A',
    }
    date = start
    day = timedelta(days=1)
    calendar = {
        "dates": [],
        "topics": [],
        "holidays": [],
    }
    while date <= end:
        if week_to_day[date.strftime('%A')] in weekdays:
            calendar['dates'].append(date.strftime('%b %d'))
            calendar['topics'].append('')
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
                         " day, with no spaces: [SMTWRFA]\n")
        for char in weekdays:
            if char not in "SMTWRFA":
                print("Bad day codes")
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


def build_table(table, calendar):
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = hdr_cells[4].text = "Date"
    hdr_cells[1].text = hdr_cells[5].text = "Topics"
    hdr_cells[2].text = hdr_cells[6].text = "Assignments"
    if len(calendar['dates']) % 2 == 1:
        calendar['dates'].append("")
        calendar['topics'].append('')
        calendar['holidays'].append('')
    i = 0
    j = len(calendar['dates']) // 2
    while i < len(calendar['dates']) // 2:
        row_cells = table.add_row().cells
        row_cells[0].text = calendar['dates'][i]
        row_cells[4].text = calendar['dates'][j]
        row_cells[2].text = calendar['holidays'][i]
        row_cells[6].text = calendar['holidays'][j]
        i += 1
        j += 1


# ############
# MAIN TREE ##
# ############
if __name__ == "__main__":
    start, end, weekdays = get_input()  # get inputs
    class_dates = build_dates(start, end, weekdays)  # populate date list

    document = docx.Document('demo.docx')
    table = document.add_table(rows=1, cols=7)
    build_table(table, class_dates)
    document.save("demo.docx")
