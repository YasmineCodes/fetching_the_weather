from math import radians, cos, sin, asin, sqrt

# function to find distance between two points using their lat/lon


def haversine(lon1, lat1, lon2, lat2):
    # convert lats and lons from degrees to radians
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)
    # find difference between two lons and lats
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    # calculate distance using haversine formula
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distance = 2 * asin(sqrt(a)) * 6371  # 6371 is the radius of the Earth
    return distance