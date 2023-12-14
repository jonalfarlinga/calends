#### Build Table
    table = document.add_table(rows=1, cols=3)

    hdr_cells = table.rows[0].cells

    hdr_cells[0].text = 'Qty'

    hdr_cells[1].text = 'Id'

    hdr_cells[2].text = 'Desc'

    for qty, id, desc in records:

        row_cells = table.add_row().cells

        row_cells[0].text = str(qty)

        row_cells[1].text = id

        row_cells[2].text = desc

    document.add_page_break()

    document.save('demo.docx')

#### etree / html

    >>> from lxml import html
    >>> from lxml import etree

    >>> page = html.fromsring(r.text)
    >>> for link in page.xpath("//a"):
    ...     print(link.text)
    ...

    >>> holi = [link for link in page.xpath("//div[@data-categories='Holidays']")]

    >>> holi = []
    >>> for td in page.xpath("//td"):
    ...     take = False
    ...     for div in td.xpath("//div[@data-categories='Holidays']"):
    ...             take = True
    ...     if take:
    ...             holi.append(td)
    ...
    >>> len(holi)
    2282
    >>> etree.tostring(holi[0], pretty_print=True)
    b'<td>\n
        <div class="date-column">\n
            <span class="event-cbx" data-value="155507014" tabindex="0" role="checkbox" aria-checked="false" aria-label="Select event: Registration Opens for Fall 2022"/>\n
            <div class="date">\n
                <span>March 28th</span>\n
                <div class="eventyear">Monday, 2022</div>\n
            </div>\n
        </div>\n
    </td>\n
    \n'
    >>>

#### Beautiful soup

    >>> from bs4 import BeautifulSoup as bs

    >>> soup = bs(r.content, "lxml")
    >>> holi = []
    >>> for td in soup.findAll('td'):
    >>>     if td.find('div', attrs = {'data-categories':'Holidays'}):
    >>>     holi.append(td)

    >>> holidays = []
    >>> for td in holi:
    >>>     holiday = {}
    >>>     holiday['name'] = td.find('div', attrs={'class':'event-title'}).text
    >>>     holiday['start'] = datetime.strptime(td.find('div', attrs={'class':'event-data'})['data-startdate'], "%Y-%m-%d")
    >>>     holiday['end'] = datetime.strptime(td.find('div', attrs={'class':'event-data'})['data-enddate'], "%Y-%m-%d")
    >>>     holidays.append(holiday)

## 2 Column table

    # take a 7 column Table and a class calendar,
    # fill in the table with the calendar info.
    def build_table_2_col(table, calendar):
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
