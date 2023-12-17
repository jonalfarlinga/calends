import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import re
import csv


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
    SUU_FALL_CAL = "https://www.suu.edu/provost/calendar/fall.html"
    SUU_SUMM_CAL = "https://www.suu.edu/provost/calendar/summer.html"
    SUU_SPRG_CAL = "https://www.suu.edu/provost/calendar/spring.html"
    req_fall = requests.get(SUU_FALL_CAL)
    req_summ = requests.get(SUU_SUMM_CAL)
    req_sprg = requests.get(SUU_SPRG_CAL)
    soup_fall = bs(req_fall.content, 'lxml')  # load html using Beautiful Soup
    soup_summ = bs(req_summ.content, 'lxml')
    soup_sprg = bs(req_sprg.content, 'lxml')

    holidays = []
    for soup in [soup_fall, soup_summ, soup_sprg]:
        headline = soup.find('h1').text
        year_span = re.search(r'\d{4}', headline).span()
        year = headline[year_span[0]:year_span[1]]
        for tr in soup.findAll('tr'):
            # get all <td> if they contain a <div data-categories="Holidays">
            if tr(text="No classes"):
                holiday = {}  # init a dict

                td = tr.find('td')

                # pull start date

                date = td.text
                if "thru" in date:
                    start_date, end_date = date.split("thru")
                    start_date = start_date.strip() + " " + year
                    end_date = end_date.strip() + " " + year
                else:
                    start_date = end_date = date + " " + year

                holiday['start'] = datetime.strptime(
                    start_date,
                    "%A, %B %d %Y"
                )
                holiday['end'] = datetime.strptime(
                    end_date,
                    "%A, %B %d %Y"
                )
                td = td.find_next()

                # pull name of holiday
                holiday['name'] = td.text

                # append the details if the dates overlap with class dates
                if (start <= holiday['start'] <= end or
                   start <= holiday['end'] <= end):
                    holidays.append(holiday)

    return holidays


def get_CSV_holidays(start, end):
    with open('files/holidays.csv', 'r', encoding="utf_8_sig") as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
        file.close()
    holidays = []
    for holiday in data:
        holiday['start'] = datetime.strptime(holiday['start'], "%m/%d/%Y")
        holiday['end'] = datetime.strptime(holiday['end'], "%m/%d/%Y")
        # append the details if the dates overlap with class dates
        if (start <= holiday["start"] <= end or
           start <= holiday['end'] <= end):
            holiday = {
                "name": holiday['name'],
                "start": holiday['start'],
                "end": holiday['end']
            }
            holidays.append(holiday)

    return holidays
