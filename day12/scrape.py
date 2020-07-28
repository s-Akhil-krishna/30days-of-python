
import requests
import datetime
from requests_html import HTML
import pandas as pd

now = datetime.datetime.now()
year = now.year 
url = "https://www.boxofficemojo.com/year/world/"

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
    r_text = url_to_file(url+'/'+f'{name}') #r_text is a string 
    html_text = HTML(html=r_text) #html_text is now a html object

    table_class = html_text.find('.imdb-scroll-table')
    #table_class is a list of all html elements
    rows = table_class[0].find("tr")

    header = rows[0]
    header_names = [col.text for col in header.find("th")]
    print(header_names)

    #final table = list of lists
    table = []
    for row in rows[1:]:
        # print(row.text)
        cols = [col.text for col in row.find("td")]
        table.append(cols)
    # print(header.text)
    # for row in table:
    #     print(*row)

    df = pd.DataFrame(table,columns=header_names)
    df.to_csv(f'data/{name}.csv',index=False)

parse_and_extract(url,2016)
