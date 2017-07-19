import time
import json
import pandas as pd
from urllib2 import urlopen, Request

import sqlalchemy

DB_HOST = '127.0.0.1'
DB_USERNAME = 'think_python'
DB_PASSWORD = 'Firewall1'
DB_NAME = 'think_python'

SOURCE_URL = 'https://data.austintexas.gov/api/views/b4k4-adkb/rows.json?accessType=DOWNLOAD'

def get_camera_location(url=SOURCE_URL):
    db_engine = sqlalchemy.create_engine('mysql://%s:%s@%s/%s' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_NAME),\
                                         pool_size=20, max_overflow=0)

    try:
        request = Request(url)
        lines = urlopen(request, timeout = 60).read()
        if len(lines) < 15: #no data
            return None
    except Exception as e:
        print e
    else:
        response = json.loads(lines)

    #Only need the address, longitude and latitude
    filtered_response = list()
    for i in response['data']:
        item = [i[0], i[19], i[30], i[31]]
        filtered_response.append(item)

    #Convert the list to a Dataframe
    columns = ['camera_id', 'address', 'latitude', 'longitude']
    df = pd.DataFrame.from_records(filtered_response, columns=columns)

    #Delete duplicated rows
    df.drop_duplicates()

    #Delete nan rows
    df.dropna(axis=0, how='any')

    #Dump to database
    if df is not None:
        df.to_sql('camera_location', con=db_engine, if_exists='replace')
    print df

if __name__ == '__main__':
    while 1:
        get_camera_location()
        time.sleep(30*60)


