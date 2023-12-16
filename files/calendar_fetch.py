import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime


# scrape TXST academic calendar for holidays between start and end
def get_TXST_holidays(start, end):
    # get html from TXST website
    TXST_CALENDAR = "https://www.registrar.txst.edu/registration/ac/academic-calendar.html"  # noqa:E501
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


# scrape TXST academic calendar for holidays between start and end
def get_SUU_holidays(start, end):
    # get html from TXST website
    SUU_CALENDAR = "https://calendar.google.com/calendar/u/0/embed?src=suu.edu_tjl05mhr4lldjqhph0lasfmqk8@group.calendar.google.com&ctz=America/Denver&mode=AGENDA"  # noqa:E501
    request = requests.get(SUU_CALENDAR)
    soup = bs(request.content, 'lxml')  # load html using Beautiful Soup

    holidays = []
    for div in soup.findAll('td', {'text': 'No Class'}):
        # get all <td> if they contain a <div data-categories="Holidays">
        if div.find('div', attrs={'class': 'day'}):
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
