from keys import TXST_CALENDAR
import docx
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup as bs


# find class dates between start, end, only on weekdays
def build_dates(start, end, weekdays, holidays):
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
    date = start  # init date counter
    day = timedelta(days=1)  # incrementer for date
    calendar = {  # container for table data
        "dates": [],
        "topics": [],
        "holidays": [],
    }

    while date <= end:
        # only add a date if it's one of the user-submitted weekdays
        if week_to_day[date.strftime('%A')] in weekdays:
            holi = False  # true if I found a holiday

            # append this date to calendar['dates']
            calendar['dates'].append(date.strftime('%b %d'))

            # add 'final exams' on last day, or append placeholder for syllabus
            if date.date() == end.date():
                calendar['topics'].append("Final Exams")
            else:
                calendar['topics'].append('')

            # add holiday info if this date is a holiday
            for holiday in holidays:
                if holiday['start'] <= date <= holiday['end']:
                    calendar['holidays'].append(
                        f"Holiday - {holiday['name']}")
                    holi = True
                    break

            if not holi:  # append empty string if I didn't find a holiday
                calendar['holidays'].append('')  # add logic for holidays
        date += day  # increment date

    return calendar


# gets start(datetime(MM DD YY)) end(datetime(MM DD YY)) weekdays([uMTWhFS])
def get_input():
    weekdays = None
    start = None
    end = None

    # ask until I recieve good data - Class days
    while not weekdays:
        weekdays = input("\nWhich weekdays? Type a one letter code for each"
                         " day, with no spaces: [SMTWRFA]\n")
        for char in weekdays:
            if char not in "SMTWRFA":
                print("Bad day codes")
                weekdays = None

    # ask until I receive good data - first day of classes
    while not start:
        try:
            start = input("\nWhat is the first day of classes? MM DD YY\n")
            start = datetime.strptime(start, "%m %d %y")
        except ValueError:
            print("Bad Date")
            start = None

    # ask until I receive good data - final exam day
    while not end:
        try:
            end = input("\nWhat is the exam date? MM DD YY\n")
            end = datetime.strptime(end, "%m %d %y")
        except ValueError:
            print("Bad Date")
            start = None

    return start, end, weekdays


# scrape TXST academic calendar for holidays between start and end
def get_TXST_holidays(start, end):
    # get html from TXST website
    request = requests.get(TXST_CALENDAR)
    soup = bs(request.content, 'lxml')  # load html using Beautiful Soup

    holidays = []
    for td in soup.findAll('td'):
        # get all <td> if they contain a <div data-categories="Holidays">
        if td.find('div', attrs={'data-categories': 'Holidays'}):
            holiday = {}  # init a dict

            # pull name of holiday
            holiday['name'] = td.find(
                'div',
                attrs={'class': 'event-title'}
            ).text

            # pull start date
            holiday['start'] = datetime.strptime(td.find(
                'div',
                attrs={'class': 'event-data'}
            )['data-startdate'], "%Y-%m-%d")

            # pull end date
            holiday['end'] = datetime.strptime(td.find(
                'div',
                attrs={'class': 'event-data'}
            )['data-enddate'], "%Y-%m-%d")

            # append the details if the dates overlap with class dates
            if (start <= holiday['start'] <= end or
               start <= holiday['end'] <= end):
                holidays.append(holiday)

    return holidays


# take a 7 column table and a class calendar,
# fill in the table with the calendar info.
def build_table(table, calendar):
    # fill in the header row
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = hdr_cells[4].text = "Date"
    hdr_cells[1].text = hdr_cells[5].text = "Topics"
    hdr_cells[2].text = hdr_cells[6].text = "Assignments"
    # if the number of dates is odd, add a blank entry
    if len(calendar['dates']) % 2 == 1:
        calendar['dates'].append('')
        calendar['topics'].append('')
        calendar['holidays'].append('')

    # for each entry in half of list, append an entry each from
    # first and last half, as a new row, to the table.
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
    holidays = get_TXST_holidays(start, end)  # get observed holidays
    class_dates = build_dates(start, end, weekdays, holidays)  # populate list

    document = docx.Document()  # init output doc
    table = document.add_table(rows=1, cols=7)  # convert list to table
    build_table(table, class_dates)
    document.save("demo.docx")
