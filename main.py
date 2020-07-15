# Default template for XBee MicroPython projects

# Default template for XBee MicroPython projects
import urequests as requests

import ujson

import uftp
import sys
from datetime import datetime
print("Hello AirNow, I'm coming for yo data")
# API Parameters
# Your API Key: C8A2A7B9-E1A6-4D9E-B89C-88CF3E47B877




options = {}
# easier to read parts liek this
options["url"] = "https://airnowapi.org/aq/data/"
options["start_date"] = "2014-09-23"
options["start_hour_utc"] = "22"
options["end_date"] = "2014-09-23"
options["end_hour_utc"] = "23"
options["parameters"] = "o3,pm25"
options["bbox"] = "32.37,-104.261,32.39,-104.263" # minX,minY,maxX,maxY
options["data_type"] = "a"
options["format"] = "application/csv"
options["ext"] = "xml"
options["api_key"] = "C8A2A7B9-E1A6-4D9E-B89C-88CF3E47B877"

REQUEST_URL = options["url"] \
                  + "?startdate=" + options["start_date"] \
                  + "t" + options["start_hour_utc"] \
                  + "&enddate=" + options["end_date"] \
                  + "t" + options["end_hour_utc"] \
                  + "&parameters=" + options["parameters"] \
                  + "&bbox=" + options["bbox"] \
                  + "&datatype=" + options["data_type"] \
                  + "&format=" + options["format"] \
                  + "&api_key=" + options["api_key"]

try:
    # Request AirNowAPI data
    # User's home directory.
    # Perform the AirNow API data request
    api_data = requests.get(REQUEST_URL)
    data = api_data.getcode()
    print(api_data.content)
    print(api_data.text)
    # You can access .content multiple times of course
    print(api_data.content)
    print(api_data.json())
    # Download complete

except Exception as e:
    print("Unable perform AirNowAPI request. %s" % e)
    sys.exit(1)
url = options
def Get_AirNow():
    print("Reading data from Airnow")
