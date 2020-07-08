from requests import get
import json
from pprint import pprint
from haversine import haversine

# save url for sstations and weather reported
stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

# save local long and lat
my_lat = 40.7719900
my_long = -73.974810

# fetch stations using get from requests and turn into python dict
all_stations = get(stations).json()['items']

# loop through stations to find the closest station
# Initialize smallest variable to the max possible distance between 2 points on earth (20036km)


def find_closest():
    smallest = 20036
    # loop through stations updating smallest and saving station id
    for station in all_stations:
        station_long = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_long, my_lat, station_long, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station


closest_stn = find_closest()
# add closest stn stn id to weather url initialized abovr
weather = weather + str(closest_stn)
my_weather = get(weather).json()['items']
pprint(my_weather)
