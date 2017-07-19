
1. This site is to show all the traffic cameras on the google map. The data is from https://data.austintexas.gov/api/views/b4k4-adkb/rows.json?accessType=DOWNLOAD

2. A background script (project2/daemon/get_camera_location.py) will download the data periodically and parse and process the data and store the data into a MYSQL database

3. The search form will send an ajax request to the server and display the result on the map

4. The python libraries used,

    django

    urllib2

    pandas

    sqlalchemy

5. The demo site,

    http://52.88.46.44/
