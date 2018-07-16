import csv

import requests
from bs4 import BeautifulSoup


def download_page():
    START_DATE = '20130428'
    END_DATE = '20180716'
    params = {
        'start': START_DATE,
        'end': END_DATE
    }
    url = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/'
    resp = requests.get(url, params=params)
    if resp.status_code != requests.codes.ok:
        raise RuntimeError('Bad response %s' % resp.text)

    return resp.text


HEADER = ['date', 'open', 'high', 'low', 'close']
FILENAME = 'bitcoin_prices.csv'


def parse_data(page):
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', class_='table')
    data = []
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if not cells:
            continue
        date_cell, open_cell, high_cell, low_cell, close_cell, *_ = cells
        data.append([
            date_cell.text,
            open_cell.text,
            high_cell.text,
            low_cell.text,
            close_cell.text,
        ])

    return data


def write_data(data):
    with open(FILENAME, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(HEADER)
        for row in data:
            writer.writerow(row)

    print('Done! Check your {} file'.format(FILENAME))


def main():
    page = download_page()
    data = parse_data(page)
    write_data(data)


if __name__ == '__main__':
    main()
