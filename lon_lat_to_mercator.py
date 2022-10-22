# Inspired from the answer to this question: https://gis.stackexchange.com/questions/298619/mercator-map-coordinates-transformation-formula

import math

def merc(lon, lat):
    """This function transforms longitude and latitude into a mercator coordinate system.
    
    Parameters:
        lon (float): float of the longitude
        lat (float): float of the lattitude
    
    Returns:
        x (float):
        y (float):
    """
    
    r_major = 6378137.000
    x = r_major * math.radians(lon)
    scale = x/lon
    y = 180.0/math.pi * math.log(math.tan(math.pi/4.0 + lat * (math.pi/180.0)/2.0)) * scale
    return (x, y)
