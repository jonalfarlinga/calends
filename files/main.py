import docx
from datetime import datetime, timedelta
from calendar_fetch import get_TXST_holidays, get_SUU_holidays
import os
from pathlib import Path
from json import load
import subprocess
OUT_PATH = None
GETTER = None


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
    format = None

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
            end = input("\nWhat is the last day of class? MM DD YY\n")
            end = datetime.strptime(end, "%m %d %y")
        except ValueError:
            print("Bad Date")
            start = None

    while not format:
        format = input("\nWhat format would you like to use?\n"
                       "(press enter to accept no formatting)\n"
                       "(type 1 to use Light Shading format)\n")
    if format == "":
        format = None
    elif format == "1":
        format = "Light Shading"

    return start, end, weekdays, format


# take a 3 column table and a class calendar,
# fill in the table with the calendar info.
def build_table(table, calendar, format):
    # styling the table
    if format:
        table.columns[0].width = docx.shared.Inches(1).emu
        table.columns[1].width = docx.shared.Inches(2.5).emu
        table.columns[2].width = docx.shared.Inches(2.5).emu
        try:
            table.style = format
        except KeyError:
            print(f"There is no '{format}' format. Using default format.")

    # fill in the header row
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = "Date"
    hdr_cells[1].text = "Topics"
    hdr_cells[2].text = "Assignments"

    # for each entry in the list, append an entry to the table
    i = 0
    while i < len(calendar['dates']):
        row_cells = table.add_row().cells
        row_cells[0].text = calendar['dates'][i]
        row_cells[2].text = calendar['holidays'][i]
        i += 1


def load_config():
    try:
        file = open('files/config.json', 'r')
        config = load(file)
        file.close()
        global OUT_PATH
        OUT_PATH = Path(config['OUT_PATH'])
        global GETTER
        GETTER = config['GETTER']
    except Exception as e:
        print("Failed to load config.json")
        print(e)


##############
# MAIN TREE ##
##############
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    load_config()
    print("\n                   ######################\n"
          "                   # Welcome to Calends #\n"
          "                   #      version 0.10  #\n"
          "                   ######################\n\n")

    # get table data
    start, end, weekdays, format = get_input()  # get inputs
    holidays = GETTER(start, end)  # get observed holidays
    class_dates = build_dates(start, end, weekdays, holidays)  # populate list

    # create .docx table
    document = docx.Document()  # init output doc
    table = document.add_table(rows=1, cols=3)  # convert list to table
    table.autofit = False
    build_table(table, class_dates, format)

    # save document to file.
    file_name = 'calends-output.docx'
    filepath = os.path.join(OUT_PATH, file_name)
    try:
        document.save(filepath)

        # open explorer to the new file and say goodbye
        subprocess.Popen(fr'explorer /select,"{str(filepath)}')
        print(f"\nPrinted calendar to {filepath}\nGoodbye!\n")
    except PermissionError:
        print("Failed to print to {filepath}")
