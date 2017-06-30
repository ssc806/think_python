1. This project relies on Scrapy and Pillow.

2. This project is to download all the images from http://www.reddit.com/r/pics, it can set the min score and max date of the iamges. The setting is in scrapy_reddit/settings.py, the default setting is the min of score is 20 and the max of date is 6/20/2017.

3. The logfile is in directory logs/ and the downloaded images will be put into images/

4. How to run -

   #cd scrapy_reddit     (the top directory of the project code)

   #scrapy crawl reddit