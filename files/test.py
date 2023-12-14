from main import build_dates, build_table, get_TXST_holidays
from docx import Document
from datetime import datetime

# test build_dates()

calendar = build_dates(
    datetime.strptime('01 01 24', "%m %d %y"),
    datetime.strptime("05 01 24", "%m %d %y"),
    "MWF",
    get_TXST_holidays(datetime.strptime('01 01 24', "%m %d %y"),
                      datetime.strptime("05 01 24", "%m %d %y"),)
)
print(calendar)

# output
# {'dates': ['Date', 'Jan 01', 'Jan 03', 'Jan 05', 'Jan 08', 'Jan 10', 'Jan 12', 'Jan 15', 'Jan 17', 'Jan 19', 'Jan 22', 'Jan 24', 'Jan 26', 'Jan 29', 'Jan 31', 'Feb 02', 'Feb 05', 'Feb 07', 'Feb 09', 'Feb 12', 'Feb 14', 'Feb 16', 'Feb 19', 'Feb 21', 'Feb 23', 'Feb 26', 'Feb 28'],
#  'holidays': ['Holiday', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']}

document = Document()
table = document.add_table(rows=1, cols=7)
build_table(table, calendar)
document.save('test.docx')
print(table)

print(get_TXST_holidays(datetime.strptime("2024-01-01", "%Y-%m-%d"),
                        datetime.strptime("2024-05-01", "%Y-%m-%d")))
