import os
import sys
import requests
import datetime
from requests_html import HTML
import pandas as pd

now = datetime.datetime.now()
year = now.year 
url = "https://www.boxofficemojo.com/year/world/"
BASE_DIR = os.path.dirname(__file__)

#saving the data from the website
def url_to_file(url,filename='world',save=False):
    r = requests.get(url)
    if r.status_code == 200:
        if save:
            with open(f"{filename}-{year}.html",'w') as file_object:
                    file_object.write(r.text)
        return r.text
    return None        
def parse_and_extract(url,name):
    new_url = os.path.join(url,f'{name}')
    r_text = url_to_file(new_url) #r_text is a string 
    if r_text is None:
        return False
    html_text = HTML(html=r_text) #html_text is now a html object

    table_class = html_text.find('.imdb-scroll-table')
    #table_class is a list of all html elements
    rows = table_class[0].find("tr")

    header = rows[0]
    header_names = [col.text for col in header.find("th")]
    # print(header_names)

    #final table = list of lists
    table = []
    for row in rows[1:]:
        # print(row.text)
        cols = [col.text for col in row.find("td")]
        table.append(cols)
    # print(header.text)
    # for row in table:
    #     print(*row)
    path = os.path.join(BASE_DIR,'data')
    os.makedirs(path,exist_ok=True) 
    filepath = os.path.join(path,f'{name}.csv')
    df = pd.DataFrame(table,columns=header_names)
    df.to_csv(filepath,index=False)
    return True

def run(start_year=year,years=1):
    for x in range(years):
        year = start_year - x 
        finished =  parse_and_extract(url,year)
        if finished:
            print(f'{year} ','finished')
        else:
            print(f'{year} ','not finished')

if __name__ == '__main__':
    now = datetime.datetime.now()
    start_year,years = 2011,5 
    try:
        start_year = int(sys.argv[1])
    except:
        start_year = now.year
    try:
        years = int(sys.argv[2])
    except:
        years = 1
    run(start_year,years)