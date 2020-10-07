import requests
import pandas as pd


def web_scraper():
    df = pd.DataFrame(columns=['Name', 'Purpose'])
    for i in range(50):
        res = requests.get('http://3.95.249.159:8000/random_company').text
        split = res.split('<ol>')[1].split('</ol>')[0].split('<li>')
        d = {}
        for s in split:
            info = s.replace('\n', '').replace('</li>', '').strip(' ')
            if 'Name:' in info:
                d['Name'] = info.split('Name: ')[1]
            if 'Purpose:' in info:
                d['Purpose'] = info.split('Purpose: ')[1]
        df = df.append(d, ignore_index=True)
    # This writes a new file every time and overwrites if it exists. I did this on purpose as the results are subject
    # to change with each run.
    df.to_csv('companies.csv')


if __name__ == '__main__':
    web_scraper()