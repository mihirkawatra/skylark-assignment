from math import radians, cos, sin, asin, sqrt

def haversine(point1, point2, unit='km'):
    AVG_EARTH_RADIUS_KM = 6371.0088

    conversions = {'km': 1,
                   'm': 1000,
                   'mi': 0.621371192,
                   'nmi': 0.539956803,
                   'ft': 3280.839895013,
                   'in': 39370.078740158}

    avg_earth_radius = AVG_EARTH_RADIUS_KM * conversions[unit]

    lat1, lng1 = point1
    lat2, lng2 = point2

    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2

    return 2 * avg_earth_radius * asin(sqrt(d))
